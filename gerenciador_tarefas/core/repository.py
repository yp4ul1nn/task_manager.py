import json
import os
from core.models import Tarefa

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ARQUIVO = os.path.join(BASE_DIR, "data", "tarefas.json")


class TarefaRepository:

    def carregar(self):
        if not os.path.exists(ARQUIVO):
            return []

        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return [Tarefa(**t) for t in dados]

    def salvar(self, tarefas):
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(
                [t.to_dict() for t in tarefas],
                f,
                indent=4,
                ensure_ascii=False
            )