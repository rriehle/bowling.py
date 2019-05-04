import pytest
from frame import Frame


def test_valid_frame():
    valid_frame = (0, 1, 0)  # Unscored frame (0 as score) is valid
    my_frame = Frame(valid_frame)
    my_frame.validate()


def test_invalid_first_ball_raises_value_error():
    invalid_frame = (11, 3, 0)  # Can't roll 11 on single ball
    with pytest.raises(ValueError):
        Frame(invalid_frame)


def test_valid_frame_score():
    valid_frame = (2, 3, 5)  # 2 + 3 == 5
    my_frame = Frame(valid_frame)
    my_frame.validate()


def test_invalid_frame_score():
    invalid_frame = (2, 3, 6)  # should be 5, not 6
    with pytest.raises(ValueError):
        Frame(invalid_frame)
