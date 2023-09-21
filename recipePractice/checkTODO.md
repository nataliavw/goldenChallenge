## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def checkTODO(string):
    '''checks the given string for any instance of "TODO"

    Parameters: (list all parameters and their types)
        string - the text being checked

    Returns: (state the return value and its type)
        boolean - true if an instance of "TODO" is found

    Side effects: (state any side effects)
        none
    '''
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

checkTODO("test") => False

checkTODO("todo") => False

checkTODO("ToDo") => False

checkTODO("TOdo") => False

checkTODO("TO DO") => False

checkTODO("TO SPLIT DO") => False

checkTODO("TODO") => False

checkTODO("#TODO") => True

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!