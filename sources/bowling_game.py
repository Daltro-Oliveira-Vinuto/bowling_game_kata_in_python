"This module has the class Bowling_Game with the functionalities for a bowling game"

class Bowling_Game():
	"Class the the attributes and methods(behaviours) expected for a bowling game"

	def __init__(self):
		self.score = 0

	def get_score(self):
		return self.score

	def roll(self):
		pass

	def __str__(self):
		return f"The score of the bowling game was {self.get_score}"