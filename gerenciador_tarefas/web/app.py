from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user
)
from werkzeug.security import generate_password_hash, check_password_hash

from core.repository import Repository
from core.models import Tarefa

app = Flask(__name__)
app.secret_key = "supersegredo_tech_saas_2024"  # Necessário para flash messages e login

repo = Repository()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return repo.buscar_usuario_por_id(int(user_id))

# =======================
# AUTENTICAÇÃO
# =======================

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Preencha todos os campos.", "error")
            return redirect(url_for("cadastrar"))

        pw_hash = generate_password_hash(password)
        user_id = repo.criar_usuario(username, pw_hash)

        if user_id:
            flash("Conta criada com sucesso! Faça login.", "success")
            return redirect(url_for("login"))
        else:
            flash("Este nome de usuário já está em uso.", "error")

    return render_template("cadastrar.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = repo.buscar_usuario_por_username(username)

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash("Usuário ou senha inválidos.", "error")

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# =======================
# SISTEMA DE TAREFAS
# =======================

@app.route("/")
@login_required
def index():
    tarefas = repo.carregar_tarefas(current_user.id)
    total = len(tarefas)
    concluidas = sum(1 for t in tarefas if t.concluida)
    progresso = int((concluidas / total * 100)) if total > 0 else 0
    
    return render_template(
        "index.html", 
        tarefas=tarefas, 
        total=total,
        concluidas=concluidas,
        progresso=progresso,
        user=current_user
    )


@app.route("/adicionar", methods=["POST"])
@login_required
def adicionar():
    titulo = request.form.get("titulo")
    descricao = request.form.get("descricao")
    prioridade = request.form.get("prioridade", "média")

    nova = Tarefa(
        id=None,
        user_id=current_user.id,
        titulo=titulo,
        descricao=descricao,
        prioridade=prioridade
    )
    repo.adicionar_tarefa(nova)

    return redirect(url_for("index"))


@app.route("/concluir/<int:id>")
@login_required
def concluir(id):
    t = repo.buscar_tarefa(id, current_user.id)
    if t:
        t.concluir()
        repo.atualizar_tarefa(t)

    return redirect(url_for("index"))


@app.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar(id):
    tarefa = repo.buscar_tarefa(id, current_user.id)

    if not tarefa:
        return redirect(url_for("index"))

    if request.method == "POST":
        tarefa.titulo = request.form.get("titulo")
        tarefa.descricao = request.form.get("descricao")
        tarefa.prioridade = request.form.get("prioridade")
        repo.atualizar_tarefa(tarefa)
        return redirect(url_for("index"))

    return render_template("editar.html", tarefa=tarefa)


@app.route("/excluir/<int:id>")
@login_required
def excluir(id):
    repo.excluir_tarefa(id, current_user.id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)