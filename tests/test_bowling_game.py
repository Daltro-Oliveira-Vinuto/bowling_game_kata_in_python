
import os
import sys

real_path = os.path.realpath(__file__)
directory_actual = os.path.dirname(real_path)
parent_directory = os.path.dirname(directory_actual)

sys.path.append(parent_directory+"/sources")
sys.path.append(parent_directory+"sources")


import bowling_game
from bowling_game import BowlingGame

def happen_spare(game: BowlingGame):
	game.roll(5)
	game.roll(5)

def happen_strike(game: BowlingGame):
	game.roll(10)


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


def test_one_spare():
	game: BowlingGame = BowlingGame()

	happen_spare(game)

	game.roll(3)

	game.repeated_rolls(17, 0)

	assert game.get_score() == 16
	assert game.score == 16

def test_one_strike():
	game: BowlingGame = BowlingGame()

	happen_strike(game)

	game.roll(3)
	game.roll(2)

	game.repeated_rolls(17, 0)

	assert game.get_score() == 20
	assert game.score == 20

def test_best_game():
	game: BowlingGame = BowlingGame()

	game.repeated_rolls(20,10)

	assert game.get_score() == 300
	assert game.score == 300


def test_specific_game():
	game: BowlingGame = BowlingGame()

	
	score_list = [1,4,4,5,6,4,5,5,10,0,1,7,3,6,4,10,2,8,6]

	game.store_roll_list(score_list)

	assert game.load_roll_list() == score_list
	assert game.get_score() == 133
	assert game.score == 133
	
	game: BowlingGame = BowlingGame()

	game.roll(1)
	game.roll(4)

	game.roll(4)
	game.roll(5)

	game.roll(6)
	game.roll(4)

	game.roll(5)
	game.roll(5)

	game.roll(10)

	game.roll(0)
	game.roll(1)

	game.roll(7)
	game.roll(3)

	game.roll(6)
	game.roll(0)

	game.roll(0)
	game.repeated_rolls(6,0)
	

	assert game.score == 83