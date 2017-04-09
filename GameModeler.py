import sys
import random
from src.Utilities import DataReader
from src.Team import Team
from src.Game import Game

def printStats(name1, name2):
    """ Print the state of the play predictor

    @params:
        :name: name of the team1
        :down: down the play is on
        :distance: distance to go
        :field: position on the field
    """
    print(name1)
    print(name2)

name1 = sys.argv[1]
name2 = sys.argv[2]

# Read in team1 stats
dataReader = DataReader()
rushingData = dataReader.statReader("Rushing.csv")
passingData = dataReader.statReader("Passing.csv")
kickingData = dataReader.statReader("Kicking.csv")
returningData = dataReader.statReader("Returning.csv")
puntingData = dataReader.statReader("Punting.csv")
downData = dataReader.statReader("Down.csv")

# Read in play percentages
playData = dataReader.playReader("Percent.csv")

# Build Team
team1 = Team(name1)
team1.buildTeam(rushingData, passingData, kickingData, returningData, puntingData, downData, playData)

team2 = Team(name2)
team2.buildTeam(rushingData, passingData, kickingData, returningData, puntingData, downData, playData)

game = Game(team1, team2)
game.startGame()

# Choose a play
# play = team1.nextPlay(down, distance, field)
# if play == "fg":
    # print("Attempting Field Goal: ")
    # if team1.fgComp / 100 > random.random():
        # print(str(100 - field + 17) + " yard field goal completed\n")
    # else:
        # print(str(100 - field + 17) + " field goal missed\n")
# elif play == "punt":
    # print("Punting: ")
    # puntDeviation = (team1.puntLong - team1.puntYA) / 3
    # puntDistance = team1.puntYA - random.randint(0, 3) * puntDeviation + random.randint(0, 3) * puntDeviation
    # print("Punted " + str(int(round(puntDistance))) + " yards\n")
# else:
    # print(str(int(play)) + " yards\n")
