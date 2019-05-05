import json
from frame import Frame


class Game:

    def __init__(self, frames, frame10ball3=0):
        self.frames = [Frame(frame) for frame in frames]
        self.frame10ball3 = frame10ball3
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

    def score(self):

        def is_last_frame(i):
            return 9 == i

        for i, frame in enumerate(self.frames):
            if frame.is_strike():
                self.frames[i] = Frame((
                    frame.first_ball,
                    frame.second_ball,
                    (20 + self.frame10ball3
                     if is_last_frame(i)
                     else 10 + self.frames[i+1].first_ball + self.frames[i+1].second_ball)
                ))
            elif frame.is_spare():
                self.frames[i] = Frame((
                    frame.first_ball,
                    frame.second_ball,
                    (10 + self.frame10ball3
                     if is_last_frame(i)
                     else 10 + self.frames[i + 1].first_ball)
                ))
            else:
                self.frames[i] = Frame((
                    frame.first_ball,
                    frame.second_ball,
                    frame.first_ball + frame.second_ball,
                ))

        return sum([frame.frame_score for frame in self.frames])

    def to_json(self):
        return json.dumps({
            'frames': [frame.to_json() for frame in self.frames],
            'frame10ball3': self.frame10ball3,
            'score': self.score()
        })
