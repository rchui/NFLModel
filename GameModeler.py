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

team1Count = 0
team2Count = 0
tieCount = 0

fileWriter = open("output.txt", 'w')
for i in range(1000):
    game = Game(team1, team2)
    game.startGame()
    while(game.quarter <= 4):
        game.playGame(game.possession)
        game.displayGame()
    if game.score1 > game.score2:
        fileWriter.write(game.team1.name + "," + str(game.score1) + "," + str(game.score2) + "\n")
        team1Count += 1
    elif game.score2 > game.score1:
        fileWriter.write(game.team2.name + "," + str(game.score2) + "," + str(game.score1) + "\n")
        team2Count += 1
    else:
        fileWriter.write("Tie" + "," + str(game.score1) + "," + str(game.score2) + "\n")
        tieCount += 1
print(team1.name + " win: " + str(float(team1Count) / float(team1Count + team2Count + tieCount) * 100) + "%")
print(team2.name + " win: " + str(float(team2Count) / float(team1Count + team2Count + tieCount) * 100) + "%")
print("Tie: " + str(float(tieCount) / float(team1Count + team2Count + tieCount) * 100) + "%")
fileWriter.close()
