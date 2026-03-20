from core.repository import TarefaRepository
from core.models import Tarefa
from core.utils import proximo_id


class GerenciadorCLI:

    def __init__(self):
        self.repo = TarefaRepository()
        self.tarefas = self.repo.carregar()

    def adicionar(self):
        titulo = input("Título: ").strip()
        descricao = input("Descrição: ").strip()
        prioridade = input("Prioridade (baixa/média/alta): ").strip() or "média"

        tarefa = Tarefa(
            id=proximo_id(self.tarefas),
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade
        )

        self.tarefas.append(tarefa)
        self.repo.salvar(self.tarefas)
        print("✔ Tarefa adicionada!")

    def listar(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        for t in self.tarefas:
            status = "✔" if t.concluida else " "
            print(f"[{status}] {t.id} - {t.titulo} ({t.prioridade})")

    def concluir(self):
        id_tarefa = int(input("ID da tarefa: "))
        for t in self.tarefas:
            if t.id == id_tarefa:
                t.concluir()
                self.repo.salvar(self.tarefas)
                print("Tarefa concluída!")

    def executar(self):
        while True:
            print("\n1-Adicionar | 2-Listar | 3-Concluir | 4-Sair")
            op = input("Escolha: ")

            if op == "1":
                self.adicionar()
            elif op == "2":
                self.listar()
            elif op == "3":
                self.concluir()
            elif op == "4":
                break


if __name__ == "__main__":
    GerenciadorCLI().executar()