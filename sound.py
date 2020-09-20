class Sound:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.duration_hours = int(duration / 3600)
        self.duration_minutes = int((self.duration - self.duration_hours * 3600) / 60)
        self.duration_seconds = int(self.duration - (self.duration_hours * 3600 + self.duration_minutes * 60))


class PlayingSoundState:
    def __init__(self, name, duration):
        self.atSecond = 0
        self.playing = True
        self.name = name
        self.duration = duration
