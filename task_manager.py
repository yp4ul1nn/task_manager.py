import json
import os
from datetime import datetime

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)
            return tarefas if isinstance(tarefas, list) else []
    except (json.JSONDecodeError, OSError):
        print("Aviso: não foi possível ler o arquivo de tarefas. Uma lista vazia será usada.")
        return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


def proximo_id(tarefas):
    if not tarefas:
        return 1
    return max(tarefa["id"] for tarefa in tarefas) + 1


def buscar_tarefa_por_id(tarefas, id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            return tarefa
    return None


def ler_id_tarefa(mensagem):
    try:
        return int(input(mensagem))
    except ValueError:
        print("Digite um número válido.")
        return None


def adicionar_tarefa(tarefas):
    titulo = input("Título da tarefa: ").strip()
    descricao = input("Descrição: ").strip()

    if not titulo:
        print("O título da tarefa não pode ficar vazio.")
        return

    tarefa = {
        "id": proximo_id(tarefas),
        "titulo": titulo,
        "descricao": descricao or "Sem descrição.",
        "criada_em": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "concluida": False,
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")


def listar_tarefas(tarefas, filtro="todas"):
    tarefas_filtradas = []

    for tarefa in tarefas:
        if filtro == "pendentes" and tarefa["concluida"]:
            continue
        if filtro == "concluidas" and not tarefa["concluida"]:
            continue
        tarefas_filtradas.append(tarefa)

    if not tarefas_filtradas:
        print("Nenhuma tarefa encontrada para esse filtro.")
        return

    for tarefa in tarefas_filtradas:
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"[{status}] {tarefa['id']} - {tarefa['titulo']}")
        print(f"    {tarefa['descricao']}")
        print(f"    Criada em: {tarefa['criada_em']}")
        print("-" * 40)


def concluir_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    listar_tarefas(tarefas, filtro="pendentes")
    id_tarefa = ler_id_tarefa("Digite o ID da tarefa para concluir: ")

    if id_tarefa is None:
        return

    tarefa = buscar_tarefa_por_id(tarefas, id_tarefa)
    if tarefa is None:
        print("ID não encontrado.")
        return

    if tarefa["concluida"]:
        print("Essa tarefa já está concluída.")
        return

    tarefa["concluida"] = True
    salvar_tarefas(tarefas)
    print("Tarefa concluída com sucesso!")


def reabrir_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    listar_tarefas(tarefas, filtro="concluidas")
    id_tarefa = ler_id_tarefa("Digite o ID da tarefa para reabrir: ")

    if id_tarefa is None:
        return

    tarefa = buscar_tarefa_por_id(tarefas, id_tarefa)
    if tarefa is None:
        print("ID não encontrado.")
        return

    if not tarefa["concluida"]:
        print("Essa tarefa já está pendente.")
        return

    tarefa["concluida"] = False
    salvar_tarefas(tarefas)
    print("Tarefa reaberta com sucesso!")


def remover_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    listar_tarefas(tarefas)
    id_tarefa = ler_id_tarefa("Digite o ID da tarefa para remover: ")

    if id_tarefa is None:
        return

    tarefa = buscar_tarefa_por_id(tarefas, id_tarefa)
    if tarefa is None:
        print("ID não encontrado.")
        return

    tarefas.remove(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa removida com sucesso!")


def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\n==== GERENCIADOR DE TAREFAS ====")
        print("1 - Adicionar tarefa")
        print("2 - Listar todas as tarefas")
        print("3 - Listar tarefas pendentes")
        print("4 - Listar tarefas concluídas")
        print("5 - Concluir tarefa")
        print("6 - Reabrir tarefa")
        print("7 - Remover tarefa")
        print("8 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            listar_tarefas(tarefas, filtro="pendentes")
        elif opcao == "4":
            listar_tarefas(tarefas, filtro="concluidas")
        elif opcao == "5":
            concluir_tarefa(tarefas)
        elif opcao == "6":
            reabrir_tarefa(tarefas)
        elif opcao == "7":
            remover_tarefa(tarefas)
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
