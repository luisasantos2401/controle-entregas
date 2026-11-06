"""Interface de linha de comando."""
import argparse
import sys

from . import service
from .db import get_connection


# --- RF01: cadastrar ---
def cmd_cadastrar(args, conn):
    novo_id = service.cadastrar(
        conn, args.titulo, args.disciplina, args.prazo, args.descricao
    )
    print(f"Entrega {novo_id} cadastrada.")


def montar_parser():
    parser = argparse.ArgumentParser(
        prog="entregas", description="Controle de entregas acadêmicas."
    )
    sub = parser.add_subparsers(dest="comando", required=True)

    # --- RF01 ---
    p = sub.add_parser("cadastrar", help="cadastra uma nova entrega")
    p.add_argument("titulo")
    p.add_argument("disciplina")
    p.add_argument("prazo", help="AAAA-MM-DD ou DD/MM/AAAA")
    p.add_argument("-d", "--descricao", default="")
    p.set_defaults(func=cmd_cadastrar)

    return parser


def main(argv=None, conn=None):
    args = montar_parser().parse_args(argv)
    conn = conn or get_connection()
    try:
        args.func(args, conn)
    except (service.ErroValidacao, service.EntregaNaoEncontrada) as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        return 1
    return 0
