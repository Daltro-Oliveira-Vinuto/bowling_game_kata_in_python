"This module has the class Bowling_Game with the functionalities for a bowling game"

class BowlingGame():
    "Class the the attributes and methods(behaviours) expected for a bowling game"

    def __init__(self) -> None:
        self._score: int = 0

    def get_score(self) -> int:
        "return the score of the bowling game"
        return self.score

    @property
    def score(self) -> int:
        "handles the return of the protected variable _score"
        return self._score

    def roll(self, points) -> None:
        "deals with each roll of the bowling game"
        self._score+= points

    def __str__(self) -> str:
        return f"The score of the bowling game was {self.get_score}"

    def repeated_rolls(self, total: int, points: int) -> None:
        "this function get a pontuation by roll(points) and repeat that roll 'total' times "
        for _ in range(total):
            self.roll(points)
