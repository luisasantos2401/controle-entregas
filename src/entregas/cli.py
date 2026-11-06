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


# --- RF04: concluir ---
def cmd_concluir(args, conn):
    service.concluir(conn, args.id)
    print(f"Entrega {args.id} concluída.")


# --- RF05: editar ---
def cmd_editar(args, conn):
    service.editar(
        conn, args.id, args.titulo, args.disciplina, args.prazo, args.descricao
    )
    print(f"Entrega {args.id} atualizada.")


# --- RF06: remover ---
def cmd_remover(args, conn):
    service.remover(conn, args.id)
    print(f"Entrega {args.id} removida.")


# --- RF07: atrasadas e próximas ---
def cmd_atrasadas(args, conn):
    _imprimir_tabela(service.atrasadas(conn))


def cmd_proximas(args, conn):
    _imprimir_tabela(service.proximas(conn, args.dias))


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

    # --- RF04 ---
    p = sub.add_parser("concluir", help="marca uma entrega como concluída")
    p.add_argument("id", type=int)
    p.set_defaults(func=cmd_concluir)

    # --- RF05 ---
    p = sub.add_parser("editar", help="altera dados de uma entrega")
    p.add_argument("id", type=int)
    p.add_argument("--titulo")
    p.add_argument("--disciplina")
    p.add_argument("--prazo", help="AAAA-MM-DD ou DD/MM/AAAA")
    p.add_argument("--descricao")
    p.set_defaults(func=cmd_editar)

    # --- RF06 ---
    p = sub.add_parser("remover", help="apaga uma entrega")
    p.add_argument("id", type=int)
    p.set_defaults(func=cmd_remover)

    # --- RF07 ---
    p = sub.add_parser("atrasadas", help="lista pendentes com prazo vencido")
    p.set_defaults(func=cmd_atrasadas)

    p = sub.add_parser("proximas", help="lista pendentes que vencem em breve")
    p.add_argument("--dias", type=int, default=7, help="janela em dias (padrão 7)")
    p.set_defaults(func=cmd_proximas)

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
