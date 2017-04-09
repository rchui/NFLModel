import random



class Game(object):

    """Docstring for Game. """

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def startGame(self):
        print("\nStarting Game...")
        self.down = 1
        self.distance = 10
        self.field = 25
        self.score1 = 0
        self.score2 = 0

        print("\t" + self.team1.name + "\t\t" + self.team2.name)
        print("Score:\t" + str(self.score1) + "\t\t" + str(self.score2))
        print("\t" + str(self.down) + " | " + str(self.distance) + "\t\t" + str(self.field))

        print("\nFlipping Coin...")
        if random.random() > 0.5:
            print(self.team1.name + " will start with the ball.")
            self.possession = 1
        else:
            print(self.team2.name + " will start with the ball.")
            self.possession = 2
