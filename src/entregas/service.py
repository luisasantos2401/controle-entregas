"""Regras de negócio do controle de entregas."""
from datetime import datetime

PENDENTE = "pendente"
CONCLUIDA = "concluida"


class ErroValidacao(ValueError):
    """Dado de entrada inválido."""


class EntregaNaoEncontrada(LookupError):
    """Não existe entrega com o id informado."""


def _obrigatorio(valor, nome):
    valor = (valor or "").strip()
    if not valor:
        raise ErroValidacao(f"O campo '{nome}' é obrigatório.")
    return valor


def _normalizar_prazo(texto):
    texto = (texto or "").strip()
    for formato in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(texto, formato).date().isoformat()
        except ValueError:
            continue
    raise ErroValidacao("Prazo inválido. Use AAAA-MM-DD ou DD/MM/AAAA.")


def buscar(conn, id_entrega):
    linha = conn.execute(
        "SELECT * FROM entregas WHERE id = ?", (id_entrega,)
    ).fetchone()
    if linha is None:
        raise EntregaNaoEncontrada(f"Entrega {id_entrega} não encontrada.")
    return linha


# --- RF01: cadastrar ---
def cadastrar(conn, titulo, disciplina, prazo, descricao=""):
    titulo = _obrigatorio(titulo, "título")
    disciplina = _obrigatorio(disciplina, "disciplina")
    prazo = _normalizar_prazo(prazo)
    cur = conn.execute(
        "INSERT INTO entregas (titulo, disciplina, descricao, prazo, status) "
        "VALUES (?, ?, ?, ?, ?)",
        (titulo, disciplina, (descricao or "").strip(), prazo, PENDENTE),
    )
    conn.commit()
    return cur.lastrowid


# --- RF02: listar ---
def listar(conn):
    cur = conn.execute("SELECT * FROM entregas ORDER BY prazo, id")
    return cur.fetchall()
