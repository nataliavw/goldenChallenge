from lib.checkTODO import *

def test_no_match():
    result = checkTODO("test") 
    assert result == False

def test_all_lower():
    result = checkTODO("todo")
    assert result == False

def test_partial_caps_one():
    result = checkTODO("ToDo") 
    assert result == False

def test_partial_caps_two():
    result = checkTODO("TOdo") 
    assert result == False

def test_split_by_space():
    result = checkTODO("TO DO") 
    assert result == False

def test_split_by_string():
    result = checkTODO("TO SPLIT DO") 
    assert result == False

def test_no_hash():
    result = checkTODO("TODO")
    assert result == False

def test_whole_appearance():
    result = checkTODO("#TODO") 
    assert result == True