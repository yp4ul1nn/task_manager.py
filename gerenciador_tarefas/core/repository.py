import sqlite3
import os
from core.models import Tarefa, Usuario

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "app.db")

class Repository:
    def __init__(self):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        self._init_db()

    def _get_conn(self):
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        with self._get_conn() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    titulo TEXT NOT NULL,
                    descricao TEXT,
                    prioridade TEXT,
                    prazo TEXT,
                    criada_em TEXT,
                    concluida INTEGER DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES usuarios (id)
                )
            ''')

    # --- USUARIOS ---
    def criar_usuario(self, username, password_hash):
        with self._get_conn() as conn:
            try:
                cursor = conn.execute("INSERT INTO usuarios (username, password_hash) VALUES (?, ?)", 
                                      (username, password_hash))
                return cursor.lastrowid
            except sqlite3.IntegrityError:
                return None  # Username já existe

    def buscar_usuario_por_username(self, username):
        with self._get_conn() as conn:
            row = conn.execute("SELECT * FROM usuarios WHERE username = ?", (username,)).fetchone()
            if row:
                return Usuario(row["id"], row["username"], row["password_hash"])
            return None

    def buscar_usuario_por_id(self, user_id):
        with self._get_conn() as conn:
            row = conn.execute("SELECT * FROM usuarios WHERE id = ?", (user_id,)).fetchone()
            if row:
                return Usuario(row["id"], row["username"], row["password_hash"])
            return None

    # --- TAREFAS ---
    def carregar_tarefas(self, user_id):
        with self._get_conn() as conn:
            rows = conn.execute("SELECT * FROM tarefas WHERE user_id = ?", (user_id,)).fetchall()
            return [Tarefa(
                id=r["id"],
                user_id=r["user_id"],
                titulo=r["titulo"],
                descricao=r["descricao"],
                prioridade=r["prioridade"],
                prazo=r["prazo"],
                criada_em=r["criada_em"],
                concluida=bool(r["concluida"])
            ) for r in rows]

    def buscar_tarefa(self, id, user_id):
        with self._get_conn() as conn:
            r = conn.execute("SELECT * FROM tarefas WHERE id = ? AND user_id = ?", (id, user_id)).fetchone()
            if r:
                return Tarefa(
                    id=r["id"], user_id=r["user_id"], titulo=r["titulo"],
                    descricao=r["descricao"], prioridade=r["prioridade"],
                    prazo=r["prazo"], criada_em=r["criada_em"], concluida=bool(r["concluida"])
                )
            return None

    def adicionar_tarefa(self, tarefa):
        with self._get_conn() as conn:
            conn.execute('''
                INSERT INTO tarefas (user_id, titulo, descricao, prioridade, prazo, criada_em, concluida)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (tarefa.user_id, tarefa.titulo, tarefa.descricao, tarefa.prioridade, 
                  tarefa.prazo, tarefa.criada_em, int(tarefa.concluida)))

    def atualizar_tarefa(self, tarefa):
        with self._get_conn() as conn:
            conn.execute('''
                UPDATE tarefas 
                SET titulo=?, descricao=?, prioridade=?, concluida=?
                WHERE id=? AND user_id=?
            ''', (tarefa.titulo, tarefa.descricao, tarefa.prioridade, 
                  int(tarefa.concluida), tarefa.id, tarefa.user_id))

    def excluir_tarefa(self, id, user_id):
        with self._get_conn() as conn:
            conn.execute("DELETE FROM tarefas WHERE id=? AND user_id=?", (id, user_id))