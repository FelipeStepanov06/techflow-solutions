class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.id_atual = 1

    def criar_tarefa(self, titulo, descricao, prioridade="Normal"):
        if not titulo:
            raise ValueError("O título da tarefa não pode estar vazio.")
        
        tarefa = {
            "id": self.id_atual,
            "titulo": titulo,
            "descricao": descricao,
            "status": "A Fazer",
            "prioridade": prioridade
        }
        self.tarefas.append(tarefa)
        self.id_atual += 1
        return tarefa

    def listar_tarefas(self):
        return self.tarefas