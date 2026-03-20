# 🚀 Task Manager CLI

Um **Gerenciador de Tarefas em Linha de Comando (CLI)** desenvolvido em Python, com persistência de dados em JSON.

Projeto focado em boas práticas de organização de código, manipulação de arquivos e estruturação modular.

---

## 📌 Sobre o Projeto

O **Task Manager CLI** permite que o usuário:

- ✅ Adicione tarefas  
- 📄 Liste tarefas cadastradas  
- ✔️ Marque tarefas como concluídas  
- 💾 Armazene dados de forma persistente  
- 🕒 Registre data e hora de criação automaticamente  

O sistema mantém os dados mesmo após o encerramento do programa, utilizando armazenamento local em JSON.

---

## 🛠 Tecnologias Utilizadas

- **Python 3**
- Biblioteca padrão:
  - `json`
  - `os`
  - `datetime`

---

## 📂 Estrutura do Projeto

```
task_manager/
│
├── task_manager.py
└── tarefas.json (gerado automaticamente)
```

---

## ▶️ Como Executar

```bash
python task_manager.py
```

---

## 📄 Licença

Distribuído sob a licença MIT.