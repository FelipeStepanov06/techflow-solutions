import pytest  
from src.app import GerenciadorTarefas  

def test_criar_tarefa_sucesso():  
    gerenciador = GerenciadorTarefas()  
    tarefa = gerenciador.criar_tarefa("Despacho de Carga A", "Rota Litoral")  

    assert tarefa["id"] == 1  
    assert tarefa["titulo"] == "Despacho de Carga A"  
    assert len(gerenciador.listar_tarefas()) == 1