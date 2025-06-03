from tasks import TaskManager

def print_menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")

def main():
    manager = TaskManager()
    while True:
        print_menu()
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            name = input("Nome da tarefa: ")
            description = input("Descrição: ")
            priority = input("Prioridade (alta, média, baixa): ")
            manager.add_task(name, description, priority)
            print("Tarefa adicionada!")
        
        elif choice == "2":
            tasks = manager.list_tasks()
            if not tasks:
                print("Nenhuma tarefa encontrada.")
            for task in tasks:
                status = "Concluída" if task.completed else "Pendente"
                print(f"{task.name} - {task.description} ({task.priority}) - {status}")
        
        elif choice == "3":
            name = input("Nome da tarefa a concluir: ")
            task = manager.complete_task(name)
            print("Tarefa concluída!" if task else "Tarefa não encontrada.")
        
        elif choice == "4":
            name = input("Nome da tarefa a remover: ")
            task = manager.remove_task(name)
            print("Tarefa removida!" if task else "Tarefa não encontrada.")
        
        elif choice == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()