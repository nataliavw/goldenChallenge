## 1. Describe the Problem

    As a user
    So that I can keep track of my tasks
    I want a program that I can add todo tasks to and see a list of them.

    As a user
    So that I can focus on tasks to complete
    I want to mark tasks as complete and have them disappear from the list.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class Todo:

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   instantialises an empty list
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to self.list
        pass # No code here yet

    def display(self):
        # Returns:
        #   The list of tasks
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

    def remove(self, index):
        #Parameters:
        #   the index of the task to be removed
        # Returns:
        #   Confirmation that the list item was removed
        # Side-effects:
        #   Throws an exception if that task isn't in the list
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

tasks = Todo()
tasks.add("Bake cookies")
tasks.display() # => "[Bake cookies]"

tasks = Todo()
tasks.add("")
tasks.display() # => "[""]"

tasks = Todo()
tasks.display() # raises an error with the message "No tasks in list."

tasks = Todo()
tasks.add("Bake cookies")
tasks.add("Walk dog")
tasks.remove(0) # returns "Removed 'Bake cookies' from the list."
tasks.display() # => "[Walk dog]"

tasks = Todo()
tasks.remove(0) # raises an error with the message "Index not found."

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

