from lib.diaryEntry import *

#test the count words 
def test_count_words():
    entry = DiaryEntry("Today", "I saw a balloon!")
    assert entry.count_words() == 4

#test the reading time
def test_reading_time():
    entry = DiaryEntry("Today", "I saw a balloon!")
    assert entry.reading_time(2) == 2

#test the chunks return correctly
def test_reading_chunk():
    entry = DiaryEntry("Today", "one two three four five, five four three two one, remix time is here baby.")
    entry.reading_chunk(5, 1)
    assert entry.reading_chunk(5, 1) == "five four three two one,"
