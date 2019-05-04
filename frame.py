class Frame:

    # index into frame tuple/list for readability/documentation
    FIRST_BALL = 0
    SECOND_BALL = 1
    FRAME_SCORE = 2
    MAX_FRAME_SCORE = 30  # Need to check the rules/algorithm

    def __init__(self, frame=(0, 0, 0)):
        self.frame = frame
        self.validate()

    def is_strike(self):
        return self.frame[self.FIRST_BALL] == 10

    def is_spare(self):
        return self.frame[self.FIRST_BALL] + self.frame[self.SECOND_BALL] == 10 and not self.is_strike()

    def validate(self):

        if not 0 <= self.frame[self.FIRST_BALL] <= 10:
            raise ValueError("First ball value out of bounds: {}".format(
                self.frame[self.FIRST_BALL]
            ))

        if not 0 <= self.frame[self.SECOND_BALL] <= 10:
            raise ValueError("Second ball value out of bounds: {}".format(
                self.frame[self.SECOND_BALL]
            ))

        if not 0 <= (self.frame[self.FIRST_BALL] + self.frame[self.SECOND_BALL]) <= 20:
            raise ValueError("Too many pins scored in frame: {}".format(
                self.frame[self.FIRST_BALL] + self.frame[self.SECOND_BALL]
            ))

        # Validate frame score = first ball + second ball
        # when there are no strikes or spares
        # and when frame has been scored (score != 0)
        if (self.frame[self.FRAME_SCORE] and  # if the frame has been scored
            not self.is_strike() and
            not self.is_spare()
        ):
            if self.frame[self.FRAME_SCORE] != self.frame[self.FIRST_BALL] + self.frame[self.SECOND_BALL]:
                raise ValueError("Incorrect score for frame: {}".format(
                    self.frame[self.FRAME_SCORE]
                ))

        if not 0 <= self.frame[self.FRAME_SCORE] <= self.MAX_FRAME_SCORE:
            raise ValueError("Invalid frame score: {}".format(
                self.frame[self.FRAME_SCORE]
            ))
