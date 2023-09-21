from lib.readingTime import *

def test_200_returns_one():
    result = readingTime(200)
    assert result == 1

def test_400_returns_two():
    result = readingTime(400)
    assert result == 2

def test_100_returns_point_five():
    result = readingTime(100) 
    assert result == 0.5

def test_500_returns_two_point_five():
    result = readingTime(500) 
    assert result == 2.5

def test_250_returns_one_point_two_five():
    result = readingTime(250)
    assert result == 1.25