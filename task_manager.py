import json
import os
from datetime import datetime

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)


def adicionar_tarefa(tarefas):
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição: ")
    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "criada_em": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "concluida": False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada!")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for tarefa in tarefas:
        status = "✔" if tarefa["concluida"] else "✖"
        print(f"[{status}] {tarefa['id']} - {tarefa['titulo']}")
        print(f"    {tarefa['descricao']}")
        print(f"    Criada em: {tarefa['criada_em']}")
        print("-" * 40)


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        id_tarefa = int(input("Digite o ID da tarefa para concluir: "))
        for tarefa in tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["concluida"] = True
                salvar_tarefas(tarefas)
                print("🎉 Tarefa concluída!")
                return
        print("ID não encontrado.")
    except ValueError:
        print("Digite um número válido.")


def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\n==== GERENCIADOR DE TAREFAS ====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()