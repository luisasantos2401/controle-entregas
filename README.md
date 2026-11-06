# Controle de Entregas

![versão](https://img.shields.io/badge/vers%C3%A3o-v0.1.0-blue)
![licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green)
![testes](https://github.com/luisasantos2401/controle-entregas/actions/workflows/tests.yml/badge.svg)

Aplicação de linha de comando para registrar atividades acadêmicas e acompanhar seus prazos.

## O problema

Cada disciplina passa atividades por um canal diferente e os prazos se acumulam. Este projeto concentra tudo em um só lugar: você cadastra a entrega, vê o que está atrasado ou perto de vencer e marca como concluída. Os dados ficam num banco SQLite local.

## Funcionalidades

| ID | Funcionalidade | Comando | Status |
|----|----------------|---------|--------|
| RF01 | Cadastrar entrega | `cadastrar` | Implementada |
| RF02 | Listar por prazo | `listar` | Implementada |
| RF03 | Filtrar por status/disciplina | `listar --status`, `--disciplina` | Planejada |
| RF04 | Concluir entrega | `concluir` | Planejada |
| RF05 | Editar entrega | `editar` | Planejada |
| RF06 | Remover entrega | `remover` | Planejada |
| RF07 | Atrasadas e próximas do prazo | `prazos` | Planejada |

Fora do escopo desta versão: interface gráfica, múltiplos usuários, lembretes e exportação de dados.

## Como executar

Requisitos: Python 3.9 ou superior e Git. Não há dependências externas.

```bash
git clone https://github.com/luisasantos2401/controle-entregas.git
cd controle-entregas
python src/main.py --help
```

No Windows, use `python` ou `py`; no Linux/macOS, `python3`.

### Exemplos

```bash
python src/main.py cadastrar "Matriz de Ideia" "Ética" 20/11/2026 -d "Primeiro processo avaliativo"
python src/main.py listar
python src/main.py listar --status pendente --disciplina "Ética"
python src/main.py concluir 1
python src/main.py editar 1 --prazo 25/11/2026
python src/main.py prazos --dias 10
python src/main.py remover 1
```

Por padrão o banco fica em `~/.controle-entregas/entregas.db`. Para usar outro arquivo, defina a variável de ambiente `ENTREGAS_DB`.

### Testes

```bash
python -m unittest discover -s tests -v
```

## Documentação

- [Termo de abertura (project charter)](docs/project-charter.md)
- [Requisitos funcionais e não funcionais](docs/requisitos.md)
- [Casos de uso](docs/casos-de-uso.md)
- [Histórias de usuário](docs/user-stories.md)
- [Modelo de dados e organização do código](docs/modelo-de-dados.md)

## Fluxo de branches

| Branch | Função | Regra |
|--------|--------|-------|
| `main` | Código estável, cada ponto relevante recebe uma tag SemVer | Sem commits diretos; só recebe merge de `develop` via Pull Request |
| `develop` | Integração do trabalho em andamento | Recebe as branches de feature via Pull Request |
| `feature/issue-NN-descricao` | Uma branch por issue | Criada a partir de `develop`; o PR referencia a issue com `Closes #NN` |

Commits seguem o padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/) (`feat`, `fix`, `docs`, `test`, `chore`, `ci`) com o número da issue no fim, por exemplo `feat(service): cadastrar entrega com validação (#9)`.

Versões: `v0.1.0` documentação e persistência · `v0.2.0` cadastrar, listar, filtrar e concluir · `v0.3.0` editar, remover e prazos · `v1.0.0` testes de integração e CI.

## Licença

MIT. Veja o arquivo [LICENSE](LICENSE).
