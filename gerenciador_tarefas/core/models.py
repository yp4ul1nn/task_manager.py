from datetime import datetime
from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

class Tarefa:
    def __init__(self, id, user_id, titulo, descricao,
                 prioridade="média",
                 prazo=None,
                 criada_em=None,
                 concluida=False):

        self.id = id
        self.user_id = user_id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.criada_em = criada_em or datetime.now().strftime("%d/%m/%Y %H:%M")
        self.concluida = concluida

    def concluir(self):
        self.concluida = True

    def reabrir(self):
        self.concluida = False

    def to_dict(self):
        return self.__dict__