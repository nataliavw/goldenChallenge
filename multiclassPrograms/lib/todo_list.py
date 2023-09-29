# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.todoList = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todoList.append({"task": todo.task, "status": todo.complete})

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        result = []
        for item in self.todoList:
            index = self.todoList.index(item)
            if self.todoList[index].get("status") == False:
                result.append(item.get("task"))
                
        return result

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        result = []
        for item in self.todoList:
            index = self.todoList.index(item)
            if self.todoList[index].get("status") == True:
                result.append(item.get("task"))
                
        return result

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for item in self.todoList:
            item["status"] = True


