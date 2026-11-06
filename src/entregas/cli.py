"""Interface de linha de comando."""
import argparse
import sys
from datetime import date

from . import service
from .db import get_connection


def _br(iso):
    return date.fromisoformat(iso).strftime("%d/%m/%Y")


# --- RF02: listar (tabela) ---
def _imprimir_tabela(entregas):
    if not entregas:
        print("Nenhuma entrega encontrada.")
        return
    print(f"{'ID':<4} {'PRAZO':<11} {'STATUS':<10} {'DISCIPLINA':<18} TÍTULO")
    for e in entregas:
        print(
            f"{e['id']:<4} {_br(e['prazo']):<11} {e['status']:<10} "
            f"{e['disciplina'][:17]:<18} {e['titulo']}"
        )


# --- RF01: cadastrar ---
def cmd_cadastrar(args, conn):
    novo_id = service.cadastrar(
        conn, args.titulo, args.disciplina, args.prazo, args.descricao
    )
    print(f"Entrega {novo_id} cadastrada.")


# --- RF02: listar ---
def cmd_listar(args, conn):
    _imprimir_tabela(service.listar(conn, args.status, args.disciplina))


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

    # --- RF02 ---
    p = sub.add_parser("listar", help="lista as entregas por prazo")
    # --- RF03 ---
    p.add_argument("--status", help="pendente ou concluida")
    p.add_argument("--disciplina", help="mostra só uma disciplina")
    p.set_defaults(func=cmd_listar)

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
