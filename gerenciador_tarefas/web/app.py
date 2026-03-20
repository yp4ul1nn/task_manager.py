from flask import Flask, render_template, request, redirect
from core.repository import TarefaRepository
from core.models import Tarefa
from core.utils import proximo_id

app = Flask(__name__)

repo = TarefaRepository()


@app.route("/")
def index():
    tarefas = repo.carregar()
    return render_template("index.html", tarefas=tarefas)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    tarefas = repo.carregar()

    nova = Tarefa(
        id=proximo_id(tarefas),
        titulo=request.form["titulo"],
        descricao=request.form["descricao"],
        prioridade=request.form["prioridade"]
    )

    tarefas.append(nova)
    repo.salvar(tarefas)

    return redirect("/")


@app.route("/concluir/<int:id>")
def concluir(id):
    tarefas = repo.carregar()

    for t in tarefas:
        if t.id == id:
            t.concluir()

    repo.salvar(tarefas)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)