from lib.diaryEntry import *

def test_format():
    entry = DiaryEntry("title", "contents")
    assert entry.format() == "title: contents"

def test_count():
    entry = DiaryEntry("title", "there are five words here")
    assert entry.count_words() == 5

def test_reading_time():
    entry = DiaryEntry("title", "there are five words here")
    assert entry.reading_time(10) == 0.5

def test_reading_chunk():
    entry = DiaryEntry("title", "there are five words here.  here is another five words.  here's five words for you!")
    readingOne = entry.reading_chunk(5, 1)
    readingTwo = entry.reading_chunk(5, 1)
    assert readingOne != readingTwo