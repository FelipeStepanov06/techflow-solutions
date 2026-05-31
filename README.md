Objetivo do Projeto
# TechFlow Solutions - Gerenciador Ágil de Tarefas  
  
## Objetivo do Projeto  
Sistema de gerenciamento de tarefas desenvolvido para uma startup de logística, visando o acompanhamento dinâmico do fluxo de trabalho e priorização em tempo real de demandas logísticas.  
  
## Metodologia e Estrutura  
- **Gestão:** Quadro Kanban gerenciado ativamente via GitHub Projects.  
- **Desenvolvimento:** Sistema backend CRUD.  
- **Qualidade:** Pipeline de CI/CD via GitHub Actions e testes unitários.  
  
## Estrutura de Diretórios  
- `/src` -> Lógica principal do sistema.  
- `/src/tests` -> Suíte de testes automatizados.  
- `.github/workflows` -> Configuração de integração contínua.  
  
## Gestão de Mudanças Documentada  
**Feature Adicional / Mudança de Escopo:** Implementação de prioridade de tarefas. Devido à urgência relatada pela equipe de logística em sinalizar rotas prioritárias, o escopo foi readaptado e foi adicionado um campo de prioridade obrigatório no CRUD, com atualização direta no Kanban.  
