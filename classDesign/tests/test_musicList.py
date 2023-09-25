import pytest
from lib.musicList import *

# test normal functioning with adding one track
def test_adding_single_track():
    tracks = MusicHistory()
    tracks.add("test track")
    assert tracks.display() == ["test track"]

# test normal functioning with adding three track
def test_adding_three_tracks():
    tracks = MusicHistory()
    tracks.add("test 1")
    tracks.add("test 2")
    tracks.add("test 3")
    assert tracks.display() == ["test 1", "test 2", "test 3"]

# test adding an empty string throws an exception
def test_exception_for_empty_track():
    tracks = MusicHistory()
    with pytest.raises(Exception) as e:
        tracks.add("") # => throws exception "No track title provided."
    error = str(e.value)
    assert error == "No track title provided."

# test displaying an empty list throws an exception
def test_exception_for_empty_track_history():
    tracks = MusicHistory()
    with pytest.raises(Exception) as e:
        tracks.display() # => throws exception "No tracks in music history."
    error = str(e.value)
    assert error == "No tracks in music history."