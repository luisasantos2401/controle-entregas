import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from entregas.db import get_connection


class TestDb(unittest.TestCase):
    def test_cria_tabela_entregas(self):
        conn = get_connection(":memory:")
        colunas = [c["name"] for c in conn.execute("PRAGMA table_info(entregas)")]
        self.assertEqual(
            colunas, ["id", "titulo", "disciplina", "descricao", "prazo", "status"]
        )


if __name__ == "__main__":
    unittest.main()
