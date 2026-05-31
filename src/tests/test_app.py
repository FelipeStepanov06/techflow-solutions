import pytest  
from src.app import GerenciadorTarefas  
  
def test_criar_tarefa_sucesso():  
    gerenciador = GerenciadorTarefas()  
    tarefa = gerenciador.criar_tarefa("Despacho de Carga A", "Rota Litoral")  
      
    assert tarefa["id"] == 1  
    assert tarefa["titulo"] == "Despacho de Carga A"  
    assert len(gerenciador.listar_tarefas()) == 1  

def test_criar_tarefa_sem_titulo_deve_falhar():  
    gerenciador = GerenciadorTarefas()  
    with pytest.raises(ValueError) as erro:  
        gerenciador.criar_tarefa("", "Sem título")  
          
    assert str(erro.value) == "O título da tarefa não pode estar vazio."