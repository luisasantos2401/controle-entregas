# Histórias de Usuário

## US01 — Cadastrar entrega (RF01)

**Como** estudante, **quero** cadastrar uma entrega com disciplina e prazo **para que** eu não esqueça de entregá-la.

```gherkin
Cenário: Cadastro com dados válidos
  Dado que informo título "Matriz de Ideia", disciplina "Ética" e prazo "20/11/2026"
  Quando executo o comando cadastrar
  Então a entrega é gravada com status "pendente"
  E o sistema mostra o id gerado

Cenário: Título vazio
  Dado que informo um título em branco
  Quando executo o comando cadastrar
  Então o sistema mostra uma mensagem de erro
  E nenhuma entrega é gravada

Cenário: Prazo inexistente
  Dado que informo o prazo "31/02/2026"
  Quando executo o comando cadastrar
  Então o sistema recusa o prazo e nada é gravado
```

## US02 — Listar entregas (RF02)

**Como** estudante, **quero** ver todas as minhas entregas ordenadas por prazo **para que** eu saiba o que vence primeiro.

```gherkin
Cenário: Listagem ordenada
  Dado que existem entregas com prazos 20/11 e 08/11
  Quando executo o comando listar
  Então a entrega de 08/11 aparece antes da de 20/11

Cenário: Nenhuma entrega
  Dado que não há entregas cadastradas
  Quando executo o comando listar
  Então o sistema mostra "Nenhuma entrega encontrada."
```

## US03 — Filtrar entregas (RF03)

**Como** estudante, **quero** filtrar por status ou disciplina **para que** eu veja só o que me interessa no momento.

```gherkin
Cenário: Filtro por status
  Dado que há uma entrega pendente e outra concluída
  Quando executo listar --status pendente
  Então só a entrega pendente aparece

Cenário: Filtro por disciplina sem diferenciar maiúsculas
  Dado que há entregas de "Ética" e de "Coding"
  Quando executo listar --disciplina ética
  Então só as entregas de Ética aparecem
```

## US04 — Concluir entrega (RF04)

**Como** estudante, **quero** marcar uma entrega como concluída **para que** ela saia da minha lista de pendências.

```gherkin
Cenário: Concluir entrega pendente
  Dado que a entrega 1 está pendente
  Quando executo concluir 1
  Então o status da entrega 1 passa a ser "concluida"

Cenário: Concluir duas vezes
  Dado que a entrega 1 já está concluída
  Quando executo concluir 1
  Então o sistema informa que ela já está concluída

Cenário: Id inexistente
  Dado que não existe a entrega 99
  Quando executo concluir 99
  Então o sistema informa que a entrega não foi encontrada
```

## US05 — Editar entrega (RF05)

**Como** estudante, **quero** corrigir os dados de uma entrega **para que** mudanças de prazo ou de título fiquem refletidas.

```gherkin
Cenário: Alterar o prazo
  Dado que a entrega 1 tem prazo 10/11/2026
  Quando executo editar 1 --prazo 15/11/2026
  Então o prazo da entrega 1 passa a ser 15/11/2026

Cenário: Editar sem informar campos
  Dado que a entrega 1 existe
  Quando executo editar 1 sem nenhuma opção
  Então o sistema pede ao menos um campo para alterar
```

## US06 — Remover entrega (RF06)

**Como** estudante, **quero** remover uma entrega cadastrada por engano **para que** minha lista fique correta.

```gherkin
Cenário: Remover entrega existente
  Dado que a entrega 1 existe
  Quando executo remover 1
  Então a entrega 1 não aparece mais na listagem

Cenário: Remover id inexistente
  Dado que não existe a entrega 99
  Quando executo remover 99
  Então o sistema informa que a entrega não foi encontrada
```

## US07 — Consultar prazos (RF07)

**Como** estudante, **quero** ver o que está atrasado e o que vence em breve **para que** eu priorize meu tempo.

```gherkin
Cenário: Entregas atrasadas
  Dado que hoje é 05/11/2026 e há uma entrega pendente com prazo 01/11/2026
  Quando executo prazos
  Então ela aparece no grupo "Atrasadas"

Cenário: Concluídas não entram
  Dado que há uma entrega concluída com prazo vencido
  Quando executo prazos
  Então ela não aparece em nenhum grupo

Cenário: Janela de dias
  Dado que há entregas pendentes em 12/11 e em 30/11
  Quando executo prazos --dias 7
  Então só a de 12/11 aparece em "Próximos 7 dias"
```
