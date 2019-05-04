import pytest
from game import Game


def test_valid_game():
    valid_game = (
        (0, 1, 1),
        (3, 4, 7)
    )

    game = Game(valid_game)
    game.validate()


def test_invalid_frame_in_game_raises_error():
    invalid_game = (
        (0, 1, 1),
        (3, 9, 7)  # invalid frame score, should be 12
    )

    with pytest.raises(ValueError):
        Game(invalid_game)


def test_invalid_frame_score_raises_error():
    invalid_game = (
        (0, 1, 1),
        (10, 10, 42)  # 42 is an out-of-bounds score
    )

    with pytest.raises(ValueError):
        Game(invalid_game)


def test_invalid_number_of_frames_in_game_raises_error():
    invalid_game = (
        (0, 1, 1),
        (0, 1, 1),
        (0, 1, 1),
        (0, 1, 1),
        (0, 1, 1),
        (0, 1, 1),
        (0, 1, 1),
        (0, 1, 1),
        (0, 1, 1),
        (0, 1, 1),
        (0, 1, 1)  # an eleventh frame
    )

    with pytest.raises(ValueError):
        Game(invalid_game)


def test_invalid_value_for_frame10ball3_raises_error():
    valid_game = (
        (0, 1, 1),
        (3, 4, 7)
    )
    invalid_value_for_frame10ball3 = 12

    with pytest.raises(ValueError):
        Game(valid_game, invalid_value_for_frame10ball3)
