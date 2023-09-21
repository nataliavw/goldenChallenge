# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def readingTime(numWords):
    '''calculates the expected reading time for the given number of words

    Parameters: (list all parameters and their types)
        numWords: a number indicating how many words are in the text

    Returns: (state the return value and its type)
        a number to represent the minutes to read

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    '''
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

readingTime(200) => 1

readingTime(400) => 2

readingTime(100) => 0.5

readingTime(500) => 2.5

readingTime(250) => 1.25

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python


```

Ensure all test function names are unique, otherwise pytest will ignore them!