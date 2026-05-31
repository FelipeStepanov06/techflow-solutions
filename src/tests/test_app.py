class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.id_atual = 1

    # --- C: CREATE (Criar) ---
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

    # --- R: READ (Ler/Listar) ---
    def listar_tarefas(self):
        return self.tarefas

    # --- U: UPDATE (Atualizar) ---
    def atualizar_tarefa(self, id_tarefa, novo_status=None, nova_prioridade=None):
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                if novo_status:
                    tarefa["status"] = novo_status
                if nova_prioridade:
                    tarefa["prioridade"] = nova_prioridade
                return tarefa
        raise ValueError("Tarefa não encontrada no sistema.")

    # --- D: DELETE (Eliminar) ---
    def deletar_tarefa(self, id_tarefa):
        for i, tarefa in enumerate(self.tarefas):
            if tarefa["id"] == id_tarefa:
                return self.tarefas.pop(i)
        raise ValueError("Tarefa não encontrada no sistema.")


# =========================================================
# Execução Manual para Demonstração (Para o Vídeo Pitch)
# =========================================================
if __name__ == "__main__":
    sistema = GerenciadorTarefas()

    print("\n=== Iniciando TechFlow Solutions ===")
    
    print("\n[+] CREATE: A registar novas tarefas logísticas...")
    sistema.criar_tarefa("Despacho Carga A", "Rota Litoral", "Alta")
    sistema.criar_tarefa("Manutenção Frota", "Revisão do camião 04", "Normal")
    sistema.criar_tarefa("Auditoria Interna", "Verificar guias de transporte", "Baixa")
    
    print("\n[+] READ: Lista inicial:")
    for t in sistema.listar_tarefas():
        print(f" -> ID: {t['id']} | {t['titulo']} | Status: {t['status']} | Prioridade: {t['prioridade']}")
        
    print("\n[+] UPDATE: A alterar o status da Tarefa 1 para 'Em Progresso'...")
    sistema.atualizar_tarefa(1, novo_status="Em Progresso")
    
    print("\n[+] DELETE: A eliminar a Tarefa 3 (Cancelada)...")
    sistema.deletar_tarefa(3)
    
    print("\n=== Ponto de Situação Final (Após as operações CRUD) ===")
    for t in sistema.listar_tarefas():
        print(f" -> ID: {t['id']} | {t['titulo']} | Status: {t['status']} | Prioridade: {t['prioridade']}")
        
    print("\n=== Sistema Encerrado ===\n")