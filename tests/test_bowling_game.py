
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
	game: BowlingGame = BowlingGame()
	assert game.get_score() == 0
	assert game.score == 0


def test_gutted_all_rolls():
	game: BowlingGame = BowlingGame()

	game.repeated_rolls(20, 0)

	assert game.get_score() == 0
	assert game.score == 0

def test_get_one_all_rolls():
	game: BowlingGame = BowlingGame()

	game.repeated_rolls(20, 1)

	assert game.get_score() == 20
	assert game.score == 20





