# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def sentenceChecker(sentence):
    '''returns true if the string starts with a capital letter and ends with a punctuation mark.

    Parameters: (list all parameters and their types)
        sentence: the stirng to be checked

    Returns: (state the return value and its type)
        a boolean, true if all parameters are met

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    '''
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

sentenceChecker("no") => False

sentenceChecker("No") => False

sentenceChecker("no.") => False

sentenceChecker("multiple words") => False

sentenceChecker("Multiple words") => False

sentenceChecker("multiple words.") => False


sentenceChecker("Yes.") => True

sentenceChecker("Yes?") => True

sentenceChecker("Yes!") => True

sentenceChecker("Multiple words.") => True

sentenceChecker("Multiple words?") => True

sentenceChecker("Multiple words!") => True

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python


```

Ensure all test function names are unique, otherwise pytest will ignore them!