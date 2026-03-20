# Task Manager CLI

Um gerenciador de tarefas em linha de comando, feito em Python, com armazenamento local em JSON.

O projeto foi pensado para ser simples de usar e facil de evoluir, mantendo o codigo organizado e a persistencia de dados entre execucoes.

## Sobre o Projeto

O `Task Manager CLI` permite:

- Adicionar novas tarefas
- Listar todas as tarefas
- Listar apenas tarefas pendentes
- Listar apenas tarefas concluidas
- Marcar uma tarefa como concluida
- Reabrir uma tarefa concluida
- Remover tarefas
- Registrar automaticamente a data e hora de criacao
- Salvar os dados em `tarefas.json`

Além disso, o programa trata cenarios basicos de erro, como arquivo JSON invalido, titulo vazio e IDs inexistentes.

## Tecnologias Utilizadas

- Python 3
- Biblioteca padrao:
  - `json`
  - `os`
  - `datetime`

## Estrutura do Projeto

```text
ProjetoPY/
|-- task_manager.py
|-- README.md
`-- tarefas.json
```

O arquivo `tarefas.json` e criado automaticamente quando necessario.

## Como Executar

No terminal, dentro da pasta do projeto:

```bash
python task_manager.py
```

## Menu Atual

Ao iniciar o programa, o menu disponivel e:

```text
1 - Adicionar tarefa
2 - Listar todas as tarefas
3 - Listar tarefas pendentes
4 - Listar tarefas concluidas
5 - Concluir tarefa
6 - Reabrir tarefa
7 - Remover tarefa
8 - Sair
```

## Exemplo de Uso

Fluxo comum:

1. Adicionar uma tarefa com titulo e descricao.
2. Listar as tarefas pendentes.
3. Concluir uma tarefa pelo ID.
4. Reabrir ou remover uma tarefa quando necessario.

## Licenca

Distribuido sob a licenca MIT.
