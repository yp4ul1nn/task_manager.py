def proximo_id(tarefas):
    if not tarefas:
        return 1
    return max(t.id for t in tarefas) + 1