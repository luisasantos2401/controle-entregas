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
