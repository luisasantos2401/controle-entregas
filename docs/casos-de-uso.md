# Casos de Uso

## Atores

| Ator | Descrição |
|------|-----------|
| Estudante | Usuário que registra e acompanha suas entregas pela linha de comando. |
| Sistema | Valida os dados e grava no banco SQLite. |

## UC01 — Cadastrar entrega

**Ator:** Estudante
**Pré-condição:** nenhuma.

**Fluxo principal**
1. O estudante executa `cadastrar` informando título, disciplina e prazo.
2. O sistema valida os dados (RN01, RN02).
3. O sistema grava a entrega com status `pendente` (RN03).
4. O sistema informa o id da nova entrega.

**Fluxo alternativo**
- A1. O estudante informa a descrição com `-d`; o sistema a grava junto.
- A2. O prazo vem em DD/MM/AAAA; o sistema converte para o formato interno.

**Fluxo de exceção**
- E1. Título ou disciplina vazios: o sistema exibe erro e não grava nada.
- E2. Prazo inválido: o sistema exibe erro e não grava nada.

## UC02 — Listar e filtrar entregas

**Ator:** Estudante
**Pré-condição:** nenhuma.

**Fluxo principal**
1. O estudante executa `listar`.
2. O sistema busca as entregas ordenadas por prazo.
3. O sistema exibe uma tabela com id, prazo, status, disciplina e título.

**Fluxo alternativo**
- A1. O estudante usa `--status` e/ou `--disciplina`; o sistema exibe só as entregas que atendem aos filtros.
- A2. Não há entregas (ou nenhuma atende ao filtro): o sistema exibe "Nenhuma entrega encontrada."

**Fluxo de exceção**
- E1. Status diferente de `pendente`/`concluida`: o sistema recusa o comando e informa as opções válidas.

## UC03 — Concluir entrega

**Ator:** Estudante
**Pré-condição:** a entrega existe.

**Fluxo principal**
1. O estudante executa `concluir <id>`.
2. O sistema altera o status para `concluida`.
3. O sistema confirma a operação.

**Fluxo de exceção**
- E1. Id inexistente: o sistema informa que a entrega não foi encontrada.
- E2. Entrega já concluída: o sistema informa e não altera nada (RN04).

## UC04 — Editar entrega

**Ator:** Estudante
**Pré-condição:** a entrega existe.

**Fluxo principal**
1. O estudante executa `editar <id>` com um ou mais campos (`--titulo`, `--disciplina`, `--prazo`, `--descricao`).
2. O sistema valida apenas os campos informados.
3. O sistema atualiza esses campos e confirma.

**Fluxo de exceção**
- E1. Nenhum campo informado: o sistema pede ao menos um campo.
- E2. Id inexistente, título/disciplina vazios ou prazo inválido: o sistema exibe erro e não altera a entrega.

## UC05 — Remover entrega

**Ator:** Estudante
**Pré-condição:** a entrega existe.

**Fluxo principal**
1. O estudante executa `remover <id>`.
2. O sistema exclui a entrega e confirma.

**Fluxo de exceção**
- E1. Id inexistente: o sistema informa que a entrega não foi encontrada.

## UC06 — Consultar prazos

**Ator:** Estudante
**Pré-condição:** nenhuma.

**Fluxo principal**
1. O estudante executa `prazos`, com `--dias N` opcional (padrão 7).
2. O sistema busca as entregas pendentes com prazo anterior a hoje (RN05).
3. O sistema busca as pendentes que vencem entre hoje e hoje + N dias.
4. O sistema exibe os dois grupos separadamente.

**Fluxo alternativo**
- A1. Um dos grupos está vazio: o sistema exibe "Nenhuma entrega encontrada." nele.

**Fluxo de exceção**
- E1. `--dias` negativo: o sistema exibe erro.
