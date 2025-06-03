# Roteiro para Coding Dojo: Programação com VS Code e GitHub Copilot

## Objetivo
Ensinar desenvolvedores a utilizar o Visual Studio Code (VS Code) com GitHub Copilot para criar códigos mais eficientes, promovendo aprendizado colaborativo e resultando em um software funcional (um gerenciador de tarefas simples em Python com interface CLI). Nesta dinâmica, apenas um piloto codifica por vez, com o copiloto sendo sempre um facilitador da organização.

## Público-Alvo
Desenvolvedores iniciantes e intermediários com noções básicas de programação em Python.

## Duração
2 horas

## Requisitos
- Computadores com VS Code instalado.
- Extensão GitHub Copilot instalada e configurada no VS Code.
- Python 3.x instalado.
- Conta no GitHub para autenticação do Copilot.
- Conhecimento básico de Python (listas, dicionários, funções).
- Um ou mais facilitadores da organização para atuar como copilotos.

## Estrutura da Dinâmica
A dinâmica segue o formato de Coding Dojo com práticas de TDD (Test-Driven Development), com um único piloto por vez e um facilitador da organização como copiloto, utilizando o Copilot para acelerar o desenvolvimento.

### 1. Abertura (10 minutos)
- **Apresentação do Objetivo**: Explicar o que é um Coding Dojo e o propósito da dinâmica: construir um gerenciador de tarefas CLI usando Python e Copilot.
- **Introdução ao GitHub Copilot**:
  - Explicar como o Copilot sugere código, completa linhas e ajuda na depuração.
  - Mostrar configurações básicas no VS Code (ativar/desativar sugestões, aceitar sugestões com `Tab`).
- **Demonstração Rápida**: Facilitador cria uma função simples (ex.: `somar(a, b)`) com Copilot para mostrar como ele sugere código.
- **Explicação do Formato**: Esclarecer que apenas um participante será o piloto por vez, com um facilitador da organização como copiloto, orientando e revisando as sugestões do Copilot.

### 2. Configuração do Ambiente (10 minutos)
- **Instruções**:
  - Garantir que todos os participantes tenham o VS Code e o Copilot configurados.
  - Criar um novo projeto com a estrutura:
    ```
    todo_app/
    ├── main.py
    ├── tasks.py
    ├── tests/
    │   └── test_tasks.py
    └── requirements.txt
    ```
  - Instalar dependências: `pytest` para testes (`pip install pytest`).
- **Atividade Prática**: Cada participante cria o projeto e testa a execução de `python main.py`.

### 3. Coding Dojo: Desenvolvimento do Gerenciador de Tarefas (90 minutos)
- **Formato**: Um único piloto (participante) codifica por vez, com um facilitador da organização como copiloto. A cada 7 minutos, um novo participante assume o papel de piloto, enquanto o facilitador (copiloto) permanece o mesmo ou é substituído por outro facilitador, conforme disponibilidade.
- **Metodologia**: TDD com ciclos de "escrever teste → falhar → implementar → passar".
- **Funcionalidades do Software**:
  1. Adicionar uma tarefa (nome, descrição, prioridade).
  2. Listar todas as tarefas.
  3. Marcar tarefa como concluída.
  4. Remover uma tarefa.
- **Passos**:
  1. **Escrever Testes**:
     - O piloto, com orientação do facilitador (copiloto), escreve um teste no arquivo `tests/test_tasks.py` usando `pytest`.
     - Exemplo: Teste para adicionar uma tarefa.
  2. **Implementar com Copilot**:
     - O piloto usa o Copilot para sugerir implementações no arquivo `tasks.py`.
     - O facilitador (copiloto) revisa as sugestões do Copilot, sugere ajustes e garante boas práticas (ex.: legibilidade, modularização).
  3. **Revisão em Grupo**:
     - A cada 15 minutos, pausar para revisar o código implementado com todos os participantes, destacando como o Copilot ajudou e o que foi ajustado pelo facilitador.
- **Dicas para o Facilitador (Copiloto)**:
  - Oriente o piloto a usar comentários para guiar o Copilot (ex.: `# Função para adicionar tarefa com nome e prioridade`).
  - Revise sugestões do Copilot em tempo real, sugerindo melhorias (ex.: tratamento de erros, otimização).
  - Mantenha o ritmo, garantindo que o piloto avance sem se prender a detalhes excessivos.

### 4. Integração e Interface CLI (20 minutos)
- **Atividade**: O piloto, com apoio do facilitador (copiloto), cria um menu interativo em `main.py` para chamar as funções do `tasks.py`.
- **Exemplo de Código com Copilot**:
  - O piloto escreve um comentário como `# Criar menu CLI para gerenciar tarefas` e deixa o Copilot sugerir o código.
  - O facilitador revisa e ajusta o menu para incluir opções como: `1. Adicionar Tarefa`, `2. Listar Tarefas`, etc.
- **Teste Final**: Executar o programa (`python main.py`) e testar todas as funcionalidades.

### 5. Encerramento e Reflexão (10 minutos)
- **Apresentação do Software**: O último piloto, com apoio do facilitador, demonstra o gerenciador de tarefas funcionando.
- **Discussão**:
  - Como o Copilot impactou a produtividade?
  - Como a interação com o facilitador (copiloto) ajudou no processo?
  - Quais foram os desafios ao usar IA para codar?
- **Próximos Passos**:
  - Sugerir práticas para continuar usando Copilot (ex.: projetos pessoais, integração com Git).
  - Compartilhar o repositório com o código final no GitHub.

## Resultado Esperado
Um gerenciador de tarefas CLI funcional em Python, com testes unitários e interface amigável, desenvolvido colaborativamente com auxílio do GitHub Copilot e orientação de facilitadores.

## Exemplo de Código Final
Abaixo está o código que os participantes devem produzir, inalterado da versão anterior, pois as mudanças são apenas no formato da dinâmica:

<xaiArtifact artifact_id="36cb343c-9ced-46b3-9e6b-74130d2fdebe" artifact_version_id="00738e53-8ed4-45ec-8f92-94a127eb13d2" title="tasks.py" contentType="text/python">
class Task:
    def __init__(self, name, description, priority, completed=False):
        self.name = name
        self.description = description
        self.priority = priority
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description, priority):
        task = Task(name, description, priority)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return task
        return None

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                return task
        return None