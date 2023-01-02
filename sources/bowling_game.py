"This module has the class Bowling_Game with the functionalities for a bowling game"

class BowlingGame():
    "Class the the attributes and methods(behaviours) expected for a bowling game"
    number_frames: int = 10

    def __init__(self) -> None:
        self._score: int = 0
        self._pontuation: list[int] = []

    def get_score(self) -> int:
        "return the score of the bowling game"

        for i,value in enumerate(self._pontuation):
            print(f"(v({i})={value}, ",end='')
        print()
        print()
        self._score = 0
        frame_index = 0
        for i in range(BowlingGame.number_frames):
            # a important note here is the fact that checking strike
            # has to come before cheking spare"
            # otherwise all strikes will be treated as spares

            if self._is_strike(frame_index):
                self._score+= 10 + self._strike_bonus(frame_index)
                frame_index+= 1
            elif self._is_spare(frame_index):
                self._score+= 10 + self._spare_bonus(frame_index)
                frame_index+= 2
            else:
                self._score+= self._get_normal_score(frame_index)
                frame_index+= 2

        return self._score

    def _is_strike(self, index: int) -> bool:
        list_out_of_bounds: bool = index >= len(self._pontuation)
        logic_state: bool
        if list_out_of_bounds:
            logic_state = False
        else:
            logic_state = self._pontuation[index] == 10

        return logic_state

    def _strike_bonus(self, index: int) -> int:
        list_out_of_bounds: bool = index+1 >= len(self._pontuation) or \
            index+2 >= len(self._pontuation)
        strike_bonus: int = 0
        if list_out_of_bounds:
            strike_bonus = 0
        else:
            strike_bonus = self._pontuation[index+1] + self._pontuation[index+2]

        return strike_bonus

    def _is_spare(self, index: int) -> bool:
        logic_state: bool
        list_out_of_bounds: bool = index >= len(self._pontuation) or index+1>= len(self._pontuation)
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
        return self.get_score()

    def roll(self, points) -> None:
        "deals with each roll of the bowling game"
        self._pontuation.append(points)

    def __str__(self) -> str:
        return f"The score of the bowling game was {self.get_score}"

    def repeated_rolls(self, total: int, points: int) -> None:
        "this function get a pontuation by roll(points) and repeat that roll 'total' times "
        for _ in range(total):
            self.roll(points)


    def store_roll_list(self, roll_list: list[int]) -> None:
        "receive a list of rolls and store in the class"
        for roll in roll_list:
            self.roll(roll)

    def load_roll_list(self) -> list[int]:
        "return the list of rolls of the bowling game"
        return self._pontuation
