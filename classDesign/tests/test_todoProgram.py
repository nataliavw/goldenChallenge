import pytest
from lib.todoProgram import *

def test_add_display_single():
    tasks = Todo()
    tasks.add("Bake cookies")
    assert tasks.display() == ["Bake cookies"]

def test_add_empty():
    tasks = Todo()
    tasks.add("")
    assert tasks.display() == [""]

def test_error_for_display_nothing():
    tasks = Todo()
    with pytest.raises(Exception) as e:
        tasks.display()
    error = str(e.value)
    assert error == "No tasks in list."

def test_remove_first_item():
    tasks = Todo()
    tasks.add("Bake cookies")
    tasks.add("Walk dog")
    tasks.remove(0) # returns "Removed 'Bake cookies' from the list."
    assert tasks.display() == ["Walk dog"]

def test_error_remove_from_empty_list():
    tasks = Todo()
    with pytest.raises(Exception) as e:
        tasks.remove(0) 
    error = str(e.value)
    assert error == "Index not found."