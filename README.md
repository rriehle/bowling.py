A class-based solution to scoring the game of bowling.

The Frame class handles a 3-member tuple of integers indicating the score on the first roll, score on the second roll, and the total score for the frame. The class validates itself and uses properties to keep its internal and external api clean.

The Game class is a collection of Frames. It has an attribute for the tenth frame's third ball, and a scoring method that scores the game at any point during game play. It rejects incorrect source game data with instructive error messages.

Both classes use simple internal data structures for easy serizlization to or from JSON in anticipation of extension into a ReST api. Both are fully tested.
