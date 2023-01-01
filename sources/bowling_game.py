"This module has the class Bowling_Game with the functionalities for a bowling game"

class BowlingGame():
    "Class the the attributes and methods(behaviours) expected for a bowling game"
    number_frames: int = 10

    def __init__(self) -> None:
        self._score: int = 0
        self._pontuation: list[int] = []

    def get_score(self) -> int:
        "return the score of the bowling game"

        self._score = 0
        frame_index = 0
        for _ in range(BowlingGame.number_frames):
            if self._is_spare(frame_index):
                self._score+= 10 + self._spare_bonus(frame_index)
                frame_index+= 2
            else:
                self._score+= self._get_normal_score(frame_index)
                frame_index+= 2

        return self._score

    def _is_spare(self, index: int) -> bool:
        logic_state: bool
        list_out_of_bounds: bool = index >= len(self._pontuation) or index >= len(self._pontuation)
        if list_out_of_bounds:
            logic_state = False
        else:
            logic_state = self._pontuation[index] + self._pontuation[index+1] == 10
        return logic_state

    def _spare_bonus(self, index: int) -> int:
        bonus: int
        if (index+2) < len(self._pontuation):
            bonus = self._pontuation[index+2]
        else:
            bonus = 0

        return bonus

    def _get_normal_score(self, index: int) -> int:
        "return pontuation of the bowling when there is not a spare or a strike"
        score: int
        if index < len(self._pontuation) and (index+1) < len(self._pontuation):
            score = self._pontuation[index] + self._pontuation[index+1]
        else:
            score = 0

        return score

    @property
    def score(self) -> int:
        "handles the return of the protected variable _score"
        return self._score

    def roll(self, points) -> None:
        "deals with each roll of the bowling game"
        self._pontuation.append(points)

    def __str__(self) -> str:
        return f"The score of the bowling game was {self.get_score}"

    def repeated_rolls(self, total: int, points: int) -> None:
        "this function get a pontuation by roll(points) and repeat that roll 'total' times "
        for _ in range(total):
            self.roll(points)
