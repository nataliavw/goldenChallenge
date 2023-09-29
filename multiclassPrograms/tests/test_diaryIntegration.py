from lib.diary import *
from lib.diaryEntry import *

#test diary.add
def test_add_and_all():
    diary = Diary()
    entry1 = DiaryEntry("Today", "I saw a balloon!")
    diary.add(entry1)
    assert diary.all() == [entry1]

#test count all words (uses the count words for each diary entry)
def test_count_words():
    diary = Diary()
    entry1 = DiaryEntry("Today", "I saw a balloon!")
    entry2 = DiaryEntry("Yesterday", "I saw no balloons.")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 8

#test reading time (use the count words function)
def test_reading_time():
    diary = Diary()
    entry1 = DiaryEntry("Today", "I saw a balloon!")
    entry2 = DiaryEntry("Yesterday", "I saw no balloons.")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.reading_time(4) == 2

#test finding the best entry for time
def test_find_entry_by_reading_time():
    diary = Diary()
    entry1 = DiaryEntry("Today", "I saw a balloon!")
    entry2 = DiaryEntry("Yesterday", "I saw no balloons.")
    entry3 = DiaryEntry("Tomorrow", "I might see another balloon, maybe.")
    entry4 = DiaryEntry("Overmorrow", "I think seeing a balloon is pretty unlikely.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    diary.add(entry4)
    assert diary.find_best_entry_for_reading_time(3, 2) == entry3