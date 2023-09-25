## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class MusicHistory:

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   instantiates an empty list to store the track history
        pass # No code here yet

    def add(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to self.history
        pass # No code here yet

    def display(self):
        # Parameters:
        #   none
        # Returns:
        #   the listening history
        # Side-effects
        #   none
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

# test normal functioning with adding one track
tracks = MusicHistory()
tracks.add("test track")
tracks.display() # => returns ["test track"]

# test normal functioning with adding three track
tracks = MusicHistory()
tracks.add("test 1")
tracks.add("test 2")
tracks.add("test 3")
tracks.display() # => returns ["test 1", "test 2", "test 3"]

# test adding an empty string throws an exception
tracks = MusicHistory()
tracks.add("") # => throws exception "No track title provided."

# test displaying an empty list throws an exception
tracks = MusicHistory()
tracks.display() # => throws exception "No tracks in music history."

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

