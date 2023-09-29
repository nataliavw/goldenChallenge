
class Diary:
    def __init__(self):
        self.allEntries = []

    def add(self, entry):
        self.allEntries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.allEntries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        count = 0
        for i in self.allEntries:
            count += i.count_words()
        return count

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        time = 0
        for i in self.allEntries:
            time += i.reading_time(wpm)
        return time

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        wordCapacity = wpm * minutes
        bestEntry = self.allEntries[0]
        for item in self.allEntries:
            if item.count_words() >= bestEntry.count_words() and item.count_words() <= wordCapacity:
                bestEntry = item
        return bestEntry

        print(self.allEntries[3].reading_chunk(wpm, minutes))
