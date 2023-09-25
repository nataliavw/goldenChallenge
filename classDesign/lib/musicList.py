class MusicHistory:

    def __init__(self):
        self.history = []

    def add(self, track):
        if len(track) > 0:
            self.history.append(track)
        else:
            raise Exception("No track title provided.")

    def display(self):
        if len(self.history) > 0:
            return self.history
        else:
            raise Exception("No tracks in music history.")