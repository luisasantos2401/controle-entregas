import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from entregas import service
from entregas.db import get_connection


class Base(unittest.TestCase):
    def setUp(self):
        self.conn = get_connection(":memory:")

    def nova(self, titulo="Atividade 1", disciplina="Coding", prazo="2026-11-10"):
        return service.cadastrar(self.conn, titulo, disciplina, prazo)


# --- RF01 ---
class TestCadastrar(Base):
    def test_cadastra_com_status_pendente(self):
        id_ = self.nova()
        e = service.buscar(self.conn, id_)
        self.assertEqual(e["status"], "pendente")
        self.assertEqual(e["titulo"], "Atividade 1")

    def test_aceita_data_no_formato_brasileiro(self):
        id_ = self.nova(prazo="10/11/2026")
        self.assertEqual(service.buscar(self.conn, id_)["prazo"], "2026-11-10")

    def test_titulo_vazio_e_recusado(self):
        with self.assertRaises(service.ErroValidacao):
            self.nova(titulo="  ")

    def test_prazo_invalido_e_recusado(self):
        with self.assertRaises(service.ErroValidacao):
            self.nova(prazo="31/02/2026")


# --- RF02 ---
class TestListar(Base):
    def test_lista_ordenada_por_prazo(self):
        self.nova("B", prazo="2026-11-20")
        self.nova("A", prazo="2026-11-08")
        titulos = [e["titulo"] for e in service.listar(self.conn)]
        self.assertEqual(titulos, ["A", "B"])

    def test_lista_vazia(self):
        self.assertEqual(service.listar(self.conn), [])


# --- RF03 ---
class TestFiltrar(Base):
    def test_filtra_por_disciplina_sem_diferenciar_maiusculas(self):
        self.nova("A", disciplina="Ética")
        self.nova("B", disciplina="Coding")
        titulos = [e["titulo"] for e in service.listar(self.conn, disciplina="ética")]
        self.assertEqual(titulos, ["A"])

    def test_filtra_por_status(self):
        self.nova("A")
        self.assertEqual(len(service.listar(self.conn, status="pendente")), 1)
        self.assertEqual(service.listar(self.conn, status="concluida"), [])

    def test_status_invalido_e_recusado(self):
        with self.assertRaises(service.ErroValidacao):
            service.listar(self.conn, status="xyz")


# --- RF04 ---
class TestConcluir(Base):
    def test_conclui_entrega(self):
        id_ = self.nova()
        service.concluir(self.conn, id_)
        self.assertEqual(service.buscar(self.conn, id_)["status"], "concluida")

    def test_nao_conclui_duas_vezes(self):
        id_ = self.nova()
        service.concluir(self.conn, id_)
        with self.assertRaises(service.ErroValidacao):
            service.concluir(self.conn, id_)

    def test_id_inexistente(self):
        with self.assertRaises(service.EntregaNaoEncontrada):
            service.concluir(self.conn, 99)
