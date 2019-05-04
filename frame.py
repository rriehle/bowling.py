import json


class Frame:

    # index into frame tuple for readability and schema documentation
    FIRST_BALL = 0
    SECOND_BALL = 1
    FRAME_SCORE = 2
    MAX_FRAME_SCORE = 30  # Not sure of this; need to check the rules

    def __init__(self, frame=(0, 0, 0)):
        self.frame = frame
        self.validate()

    @property
    def first_ball(self):
        return self.frame[self.FIRST_BALL]

    @property
    def second_ball(self):
        return self.frame[self.SECOND_BALL]

    @property
    def frame_score(self):
        return self.frame[self.FRAME_SCORE]

    @frame_score.setter
    def frame_score(self, score):
        assert 0 <= score <= self.MAX_FRAME_SCORE
        self.frame[self.FRAME_SCORE] = score

    def is_strike(self):
        return self.first_ball == 10

    def is_spare(self):
        return self.first_ball + self.second_ball == 10 and not self.is_strike()

    def validate(self):

        if not 0 <= self.first_ball <= 10:
            raise ValueError("First ball value out of bounds: {}".format(
                self.first_ball
            ))

        if not 0 <= self.second_ball <= 10:
            raise ValueError("Second ball value out of bounds: {}".format(
                self.second_ball
            ))

        if not 0 <= (self.first_ball + self.second_ball) <= 20:
            raise ValueError("Too many pins scored in frame: {}".format(
                self.first_ball + self.second_ball
            ))

        # Validate frame score = first ball + second ball
        # when there are no strikes or spares
        # and when frame has been scored (score != 0)
        if (
            self.frame_score and  # if the frame has been scored
            not self.is_strike() and
            not self.is_spare()
        ):
            if self.frame_score != self.first_ball + self.second_ball:
                raise ValueError("Incorrect score for frame: {}".format(
                    self.frame_score
                ))

        if not 0 <= self.frame_score <= self.MAX_FRAME_SCORE:
            raise ValueError("Invalid frame score: {}".format(
                self.frame_score
            ))

    def to_json(self):
        return json.dumps(list(self.frame))
