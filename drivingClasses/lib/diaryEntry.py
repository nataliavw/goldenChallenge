class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.bookmark = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return (len(self.contents.split()) / wpm)

    def reading_chunk(self, wpm, minutes):
        maxWords = wpm * minutes
        words = self.contents.split()
        startChunk = self.bookmark
        endChunk = self.bookmark + maxWords
        chunk = words[startChunk:endChunk]
        self.bookmark = endChunk
        return " ".join(chunk)