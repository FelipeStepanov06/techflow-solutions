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


if __name__ == "__main__":
    sistema = GerenciadorTarefas()

    print("=== Iniciando TechFlow Solutions ===")
    

    print("\nAdicionando tarefas ao sistema...")
    t1 = sistema.criar_tarefa("Despacho Carga A", "Rota Litoral", "Alta")
    t2 = sistema.criar_tarefa("Manutenção Frota", "Revisão do caminhão 04")
    

    print("\n=== Lista de Tarefas Atuais ===")
    lista = sistema.listar_tarefas()
    for tarefa in lista:
        print(f"ID: {tarefa['id']} | Título: {tarefa['titulo']} | Prioridade: {tarefa['prioridade']}")