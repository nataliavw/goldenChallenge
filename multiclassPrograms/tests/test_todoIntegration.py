from lib.todo import *
from lib.todo_list import *

# check return incomplete
def test_return_incomplete():
    test = Todo("Walk the dog")
    testList = TodoList()
    testList.add(test)
    assert testList.incomplete() == ["Walk the dog"]

# check mark complete
def test_return_complete():
    test = Todo("Walk the dog")
    test.mark_complete()
    testList = TodoList()
    testList.add(test)
    assert testList.complete() == ["Walk the dog"]

#  check return incomplete with multiple entries
def test_return_incomplete_multiple():
    test1 = Todo("Walk the dog")
    test2 = Todo("Bake some cookies")
    testList = TodoList()
    testList.add(test1)
    testList.add(test2)
    assert testList.incomplete() == ["Walk the dog", "Bake some cookies"]

#  check return complete with multiple entries
def test_return_complete_multiple():
    test1 = Todo("Walk the dog")
    test2 = Todo("Bake some cookies")
    testList = TodoList()
    test2.mark_complete()
    testList.add(test1)
    testList.add(test2)
    assert testList.complete() == ["Bake some cookies"]

# check give_up marks all complete
def test_give_up_marks_all():
    test1 = Todo("Walk the dog")
    test2 = Todo("Bake some cookies")
    test3 = Todo("Paint the ceiling")

    testList = TodoList()
    testList.add(test1)
    testList.add(test2)
    testList.add(test3)

    testList.give_up()
    assert testList.incomplete() == []

# check give_up marks all complete when some entries are already completed
def test_give_up_marks_all():
    test1 = Todo("Walk the dog")
    test2 = Todo("Bake some cookies")
    test3 = Todo("Paint the ceiling")
    test3.mark_complete()

    testList = TodoList()
    testList.add(test1)
    testList.add(test2)
    testList.add(test3)

    testList.give_up()
    assert testList.incomplete() == []