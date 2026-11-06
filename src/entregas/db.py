"""Conexão com o SQLite e criação da tabela."""
import os
import sqlite3
from pathlib import Path

CAMINHO_PADRAO = Path.home() / ".controle-entregas" / "entregas.db"

SQL_TABELA = """
CREATE TABLE IF NOT EXISTS entregas (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo     TEXT NOT NULL,
    disciplina TEXT NOT NULL,
    descricao  TEXT NOT NULL DEFAULT '',
    prazo      TEXT NOT NULL,
    status     TEXT NOT NULL DEFAULT 'pendente'
               CHECK (status IN ('pendente', 'concluida'))
)
"""


def get_connection(caminho=None):
    """Abre (e cria, se preciso) o banco. Use ':memory:' nos testes."""
    caminho = str(caminho or os.environ.get("ENTREGAS_DB") or CAMINHO_PADRAO)
    if caminho != ":memory:":
        Path(caminho).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(caminho)
    conn.row_factory = sqlite3.Row
    conn.execute(SQL_TABELA)
    conn.commit()
    return conn
