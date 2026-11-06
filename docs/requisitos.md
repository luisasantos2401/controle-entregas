# Requisitos — Controle de Entregas

## Requisitos Funcionais

| ID | Descrição | Prioridade |
|----|-----------|-----------|
| RF01 | O sistema deve permitir cadastrar uma entrega com título, disciplina, prazo e descrição opcional. | Alta |
| RF02 | O sistema deve listar todas as entregas ordenadas pelo prazo. | Alta |
| RF03 | O sistema deve permitir filtrar a listagem por status e por disciplina. | Média |
| RF04 | O sistema deve permitir marcar uma entrega como concluída. | Alta |
| RF05 | O sistema deve permitir editar título, disciplina, prazo e descrição de uma entrega. | Média |
| RF06 | O sistema deve permitir remover uma entrega. | Média |
| RF07 | O sistema deve exibir as entregas pendentes atrasadas e as que vencem nos próximos N dias (padrão: 7). | Alta |

## Requisitos Não Funcionais

| ID | Categoria | Descrição |
|----|-----------|-----------|
| RNF01 | Persistência | Os dados devem ser gravados em um banco SQLite local e permanecer entre execuções. |
| RNF02 | Portabilidade | Deve rodar em Windows, Linux e macOS com Python 3.9+, sem dependências externas. |
| RNF03 | Desempenho | Qualquer comando deve responder em menos de 1 segundo com até 1.000 entregas. |
| RNF04 | Usabilidade | Mensagens e ajuda em português; datas exibidas como DD/MM/AAAA. |
| RNF05 | Usabilidade | Entradas de data aceitas em AAAA-MM-DD e DD/MM/AAAA. |
| RNF06 | Segurança | Consultas SQL parametrizadas, sem concatenar entrada do usuário. |
| RNF07 | Confiabilidade | Erros de validação devem exibir mensagem clara e encerrar com código de saída 1, sem derrubar o programa com traceback. |
| RNF08 | Manutenibilidade | Regras de negócio separadas da interface (`service.py` e `cli.py`) e cobertas por testes unitários. |

## Regras de Negócio

| ID | Regra |
|----|-------|
| RN01 | Título e disciplina são obrigatórios e não podem ser vazios. |
| RN02 | O prazo deve ser uma data de calendário válida. |
| RN03 | Toda entrega nasce com status `pendente`. |
| RN04 | Uma entrega já concluída não pode ser concluída novamente. |
| RN05 | Uma entrega está atrasada quando está pendente e o prazo é anterior à data de hoje. |

## Matriz de rastreabilidade

| Requisito | Caso de uso | História | Issue |
|-----------|-------------|----------|-------|
| RF01 | UC01 | US01 | #9 |
| RF02 | UC02 | US02 | #10 |
| RF03 | UC02 | US03 | #11 |
| RF04 | UC03 | US04 | #12 |
| RF05 | UC04 | US05 | #13 |
| RF06 | UC05 | US06 | #14 |
| RF07 | UC06 | US07 | #15 |
