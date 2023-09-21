from lib.sentenceChecker import *


def test_no_punctuation_or_cap():
    result = sentenceChecker("no") 
    assert result == False

def test_no_punctuation():
    result = sentenceChecker("No") 
    assert result == False

def test_no_cap():
    result = sentenceChecker("no.") 
    assert result == False

def test_multiword_no_punctuation_or_cap():
    result = sentenceChecker("multiple words") 
    assert result == False

def test_multiword_no_punctuation():
    result = sentenceChecker("Multiple words") 
    assert result == False

def test_multiword_no_cap():
    result = sentenceChecker("multiple words.") 
    assert result == False

def test_period():
    result = sentenceChecker("Yes.") 
    assert result == True

def test_question():
    result = sentenceChecker("Yes?") 
    assert result == True

def test_exclaimation():
    result = sentenceChecker("Yes!")
    assert result == True

def test_multiword_period():
    result = sentenceChecker("Multiple words.")
    assert result == True

def test_multiword_question():
    result = sentenceChecker("Multiple words?") 
    assert result == True

def test_multiword_exclaimation():
    result = sentenceChecker("Multiple words!") 
    assert result == True