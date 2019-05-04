from frame import Frame


class Game:

    def __init__(self, frames, frame10ball3=0):
        self.frames = [Frame(frame) for frame in frames]
        self.frame10ball3 = frame10ball3
        self.game_score = 0
        self.validate()

    def validate(self):

        # Verify that there are no more than ten frames in the game
        if not 0 <= len(self.frames) <= 10:
            raise ValueError("Invalid number of frames in game: {}".format(
                len(self.frames)
            ))

        # Verify that frame 10's ball 3 hit no more than 10 pins
        if not 0 <= self.frame10ball3 <= 10:
            raise ValueError("Frame 10's third ball is out of range: {}".format(
                self.frame10ball3
            ))

        # Have each frame validate itself; this is redundant if Frame.__init__ does the job
        for frame in self.frames:
            frame.validate()

    def score_game(self):
        pass
