
import os
import sys

real_path = os.path.realpath(__file__)
directory_actual = os.path.dirname(real_path)
parent_directory = os.path.dirname(directory_actual)

sys.path.append(parent_directory+"/sources")
sys.path.append(parent_directory+"sources")


import bowling_game
from bowling_game import BowlingGame


def test_game_started():
	game = BowlingGame()

	assert game.get_score() == 0
