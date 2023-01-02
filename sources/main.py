"main program"

from bowling_game import BowlingGame

if __name__ == "__main__":
    game: BowlingGame = BowlingGame()

    score_list = [1,4,4,5,6,4,5,5,10,0,1,7,3,6,4,10,2,8,6]

    #print(game)
    print(game.get_score())
