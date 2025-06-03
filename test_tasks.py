import pytest
from tasks import TaskManager, Task

def test_add_task():
    manager = TaskManager()
    task = manager.add_task("Teste", "Descrição teste", "alta")
    assert task.name == "Teste"
    assert task.description == "Descrição teste"
    assert task.priority == "alta"
    assert task.completed == False
    assert len(manager.tasks) == 1

def test_list_tasks():
    manager = TaskManager()
    manager.add_task("Teste", "Descrição teste", "alta")
    tasks = manager.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].name == "Teste"

def test_complete_task():
    manager = TaskManager()
    manager.add_task("Teste", "Descrição teste", "alta")
    task = manager.complete_task("Teste")
    assert task.completed == True
    assert manager.complete_task("Inexistente") is None

def test_remove_task():
    manager = TaskManager()
    manager.add_task("Teste", "Descrição teste", "alta")
    task = manager.remove_task("Teste")
    assert len(manager.tasks) == 0
    assert manager.remove_task("Inexistente") is None