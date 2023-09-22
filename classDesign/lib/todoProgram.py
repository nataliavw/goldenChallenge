class Todo():
    def __init__(self):
        self.todo = []

    def add(self, task):
        self.todo.append(task)
    
    def display(self):
        if self.todo != []:
            return self.todo
        else: 
            raise Exception("No tasks in list.")
    
    def remove(self, index):
        if len(self.todo) < index or self.todo == []:
            raise Exception("Index not found.")
        else:
            return f"Removed '{self.todo.pop(index)}' from the list."