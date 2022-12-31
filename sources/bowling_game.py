"This module has the class Bowling_Game with the functionalities for a bowling game"

class BowlingGame():
    "Class the the attributes and methods(behaviours) expected for a bowling game"

    def __init__(self):
        self._score = 0

    def get_score(self):
        "return the score of the bowling game"
        return self.score

    @property
    def score(self):
        "handles the return of the protected variable _score"
        return self._score

    def roll(self):
        "deals with each roll of the bowling game"

    def __str__(self):
        return f"The score of the bowling game was {self.get_score}"
