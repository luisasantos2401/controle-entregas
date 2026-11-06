# Termo de Abertura do Projeto — Controle de Entregas

**Autora:** Luisa Santos
**Disciplina:** Análise e Desenvolvimento de Sistemas — SENAC Pernambuco
**Versão do documento:** 1.0

## 1. Visão geral e justificativa

Em um curso com várias disciplinas, as atividades chegam por canais diferentes (Teams, e-mail, grupos de mensagem) e cada uma tem seu próprio prazo. É fácil perder o controle do que já foi entregue, do que vence esta semana e do que já está atrasado.

O **Controle de Entregas** é uma aplicação de linha de comando que concentra essas atividades em um só lugar: o estudante cadastra a entrega com disciplina e prazo, acompanha o que está pendente e marca como concluída quando terminar. Os dados ficam em um banco SQLite local, sem necessidade de conta ou conexão com a internet.

Por ser pequeno, o projeto também serve para praticar o ciclo completo de engenharia: especificação, backlog, Git Flow, commits atômicos e versionamento semântico.

## 2. Objetivos SMART

| # | Objetivo | Como medir | Prazo |
|---|----------|-----------|-------|
| 1 | Implementar as 7 funcionalidades RF01–RF07 acessíveis por linha de comando | Cada RF funcionando e demonstrável no README | Prazo da atividade (novembro/2026) |
| 2 | Cobrir as regras de negócio com testes automatizados | Fluxo principal e erros de validação de cada RF testados; testes rodando no GitHub Actions a cada push | Prazo da atividade |
| 3 | Manter rastreabilidade entre documentação e código | Mínimo de 15 issues, cada uma com critérios de aceite; cada Pull Request fecha uma issue | Durante todo o desenvolvimento |
| 4 | Publicar versões estáveis com SemVer | Tags anotadas v0.1.0, v0.2.0, v0.3.0 e v1.0.0 | Conforme os marcos da seção 6 |

## 3. Escopo preliminar

**Dentro do escopo**

- Cadastro, listagem, filtro, conclusão, edição e remoção de entregas.
- Consulta de entregas atrasadas e das que vencem nos próximos dias.
- Persistência local em SQLite.
- Documentação em `docs/`, testes automatizados e pipeline simples de CI.

**Fora do escopo**

- Interface gráfica ou web.
- Múltiplos usuários, login ou sincronização na nuvem.
- Notificações e lembretes automáticos.
- Anexos de arquivos e integração com o Teams.
- Exportação de dados (CSV/PDF).

## 4. Stakeholders e público-alvo

| Parte interessada | Papel | Interesse |
|-------------------|-------|-----------|
| Luisa Santos | Desenvolvedora e product owner | Entregar o projeto e praticar o fluxo de trabalho |
| Professor da disciplina | Avaliador | Verificar documentação, backlog, histórico Git e versionamento |
| Estudantes de graduação (público-alvo) | Usuários finais | Não perder prazos de atividades |

## 5. Premissas e restrições

- Python 3.9 ou superior, usando apenas a biblioteca padrão.
- Desenvolvimento individual, em uma semana.
- Uso em computador pessoal, via terminal.

## 6. Marcos e versões

| Versão | Conteúdo |
|--------|----------|
| v0.1.0 | Documentação completa e camada de persistência |
| v0.2.0 | Cadastrar, listar, filtrar e concluir entregas |
| v0.3.0 | Editar, remover e consultar prazos |
| v1.0.0 | Testes de integração da CLI e CI configurado |
