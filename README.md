A class-based solution to scoring the game of bowling.

The Frame class handles a 3-member tuple of integers indicating the score on the first roll, score on the second roll, and the total score for the frame. The class validates itself and uses properties to keep its internal and external api clean.

The Game class is a collection of Frames. It has an attribute for the tenth frame's third ball, and a scoring method that scores the game at any point during game play. It rejects incorrect source game data with instructive error messages.

Both classes use simple internal data structures for easy serizlization to or from JSON in anticipation of extension into a ReST api. Both are fully tested.

```bash
(py3) rriehle@ontario:~/src/multiscale/bowling (master)$ python -m pytest -vv tests/
===================================================================== test session starts ======================================================================
platform darwin -- Python 3.7.3, pytest-4.4.1, py-1.8.0, pluggy-0.9.0 -- /Users/brew/.virtualenvs/py3/bin/python
cachedir: .pytest_cache
rootdir: /Users/rriehle/src/multiscale/bowling
collected 14 items

tests/test_frame.py::test_valid_frame PASSED                                                                                                             [  7%]
tests/test_frame.py::test_invalid_first_ball_raises_value_error PASSED                                                                                   [ 14%]
tests/test_frame.py::test_valid_frame_score PASSED                                                                                                       [ 21%]
tests/test_frame.py::test_invalid_frame_score PASSED                                                                                                     [ 28%]
tests/test_game.py::test_valid_game PASSED                                                                                                               [ 35%]
tests/test_game.py::test_invalid_frame_in_game_raises_error PASSED                                                                                       [ 42%]
tests/test_game.py::test_invalid_frame_score_raises_error PASSED                                                                                         [ 50%]
tests/test_game.py::test_invalid_number_of_frames_in_game_raises_error PASSED                                                                            [ 57%]
tests/test_game.py::test_invalid_value_for_frame10ball3_raises_error PASSED                                                                              [ 64%]
tests/test_game.py::test_score_simple_game PASSED                                                                                                        [ 71%]
tests/test_game.py::test_score_game_with_spares PASSED                                                                                                   [ 78%]
tests/test_game.py::test_score_game_with_multiple_spares PASSED                                                                                          [ 85%]
tests/test_game.py::test_score_almost_perfect_game PASSED                                                                                                [ 92%]
tests/test_game.py::test_score_perfect_game PASSED                                                                                                       [100%]

================================================================== 14 passed in 0.03 seconds ===================================================================
(py3) rriehle@ontario:~/src/multiscale/bowling (master)$
```

