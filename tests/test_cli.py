import io
import os
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from entregas.cli import main
from entregas.db import get_connection


class TestCli(unittest.TestCase):
    def setUp(self):
        self.conn = get_connection(":memory:")

    def rodar(self, *argv):
        saida, erro = io.StringIO(), io.StringIO()
        with redirect_stdout(saida), redirect_stderr(erro):
            codigo = main(list(argv), conn=self.conn)
        return codigo, saida.getvalue(), erro.getvalue()

    def test_cadastrar_e_listar(self):
        codigo, saida, _ = self.rodar("cadastrar", "Relatório", "Coding", "10/11/2026")
        self.assertEqual(codigo, 0)
        self.assertIn("Entrega 1 cadastrada.", saida)
        _, saida, _ = self.rodar("listar")
        self.assertIn("Relatório", saida)
        self.assertIn("10/11/2026", saida)

    def test_titulo_vazio_retorna_erro(self):
        codigo, _, erro = self.rodar("cadastrar", "", "Coding", "10/11/2026")
        self.assertEqual(codigo, 1)
        self.assertIn("obrigatório", erro)

    def test_prazo_invalido_retorna_erro(self):
        codigo, _, erro = self.rodar("cadastrar", "A", "Coding", "31/02/2026")
        self.assertEqual(codigo, 1)
        self.assertIn("Prazo inválido", erro)

    def test_concluir_e_filtrar_por_status(self):
        self.rodar("cadastrar", "Relatório", "Coding", "10/11/2026")
        self.assertEqual(self.rodar("concluir", "1")[0], 0)
        _, saida, _ = self.rodar("listar", "--status", "concluida")
        self.assertIn("Relatório", saida)
        _, saida, _ = self.rodar("listar", "--status", "pendente")
        self.assertIn("Nenhuma entrega encontrada.", saida)

    def test_filtrar_por_disciplina(self):
        self.rodar("cadastrar", "A", "Ética", "10/11/2026")
        self.rodar("cadastrar", "B", "Coding", "11/11/2026")
        _, saida, _ = self.rodar("listar", "--disciplina", "ética")
        self.assertIn("A", saida)
        self.assertNotIn("Coding", saida)

    def test_editar_sem_campos_retorna_erro(self):
        self.rodar("cadastrar", "A", "Coding", "10/11/2026")
        codigo, _, erro = self.rodar("editar", "1")
        self.assertEqual(codigo, 1)
        self.assertIn("ao menos um campo", erro)

    def test_remover_e_remover_de_novo(self):
        self.rodar("cadastrar", "A", "Coding", "10/11/2026")
        self.assertEqual(self.rodar("remover", "1")[0], 0)
        codigo, _, erro = self.rodar("remover", "1")
        self.assertEqual(codigo, 1)
        self.assertIn("não encontrada", erro)

    def test_prazos_mostra_os_dois_grupos(self):
        self.rodar("cadastrar", "Velha", "Coding", "01/01/2020")
        codigo, saida, _ = self.rodar("prazos")
        self.assertEqual(codigo, 0)
        self.assertIn("Atrasadas", saida)
        self.assertIn("Próximos 7 dias", saida)
        self.assertIn("Velha", saida)

    def test_prazos_com_dias_negativos_retorna_erro(self):
        codigo, _, erro = self.rodar("prazos", "--dias", "-1")
        self.assertEqual(codigo, 1)
        self.assertIn("negativo", erro)
