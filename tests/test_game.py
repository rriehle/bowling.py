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


def test_score_simple_game():
    """ Score a game sans strikes or spares """

    simple_game = (
        (0, 1, 0),
        (2, 3, 0),
        (4, 5, 0),
        (6, 7, 0),
        (8, 9, 0),
        (8, 7, 0),
        (6, 5, 0),
        (4, 3, 0),
        (2, 1, 0),
        (2, 3, 0)
    )

    assert 86 == Game(simple_game).score()


def test_score_game_with_spares():

    game_with_a_spare = (
        (9, 1, 0),  # 12 = spare plus first ball next frame
        (2, 3, 0),  # 5 = frame score
    )

    assert 17 == Game(game_with_a_spare).score()


def test_score_game_with_multiple_spares():

    game_with_a_spare = (
        (9, 1, 0),  # 12 = spare plus first ball next frame
        (2, 3, 0),  # 5 = frame score
        (0, 10, 0),  # 16 = all pins on second ball plus first ball next frame
        (6, 3, 0)  # 9
    )

    assert 42 == Game(game_with_a_spare).score()


def test_score_almost_perfect_game():
    """ Unsure of the rules on scoring this, but I think it is correct """

    almost_perfect_game = (
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (5, 5, 0)  # spare in the last frame
    )

    assert 280 == Game(almost_perfect_game, frame10ball3=10).score()


def test_score_perfect_game():

    perfect_game = (
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0),
        (10, 10, 0)
    )

    assert 300 == Game(perfect_game, frame10ball3=10).score()
