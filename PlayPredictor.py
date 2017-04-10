import sys
import random
from src.Utilities import DataReader
from src.Team import Team

def printStats(name, down, distance, field):
    """ Print the state of the play predictor

    @params:
        :name: name of the team
        :down: down the play is on
        :distance: distance to go
        :field: position on the field
    """
    print(name)
    print(down)
    print(distance)
    print(field)

name = sys.argv[1]
down = int(sys.argv[2])
distance = int(sys.argv[3])
field = int(sys.argv[4])

# Read in team stats
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
team = Team(name)
team.buildTeam(rushingData, passingData, kickingData, returningData, puntingData, downData, playData)

# Choose a play
playSet = {}
play = ""
percent = 0.0
for i in range(1000):
    playTemp, percentTemp = team.playProb(down, distance, field)
    if playTemp not in playSet.keys():
        playSet[playTemp] = percentTemp
    if percent < percentTemp:
        play = playTemp
        percent = percentTemp

print("")
for i in playSet.keys():
    print(i + ", " + str(playSet[i]))
print("")

if play == "fg":
    print("Kicking field goal with " + str("{:3.2f}".format(percent * 100)) + "% probability\n")
elif play == "punt":
    print("Punting with " + str("{:3.2f}".format(percent * 100)) + "% probability\n")
else:
    print(play + " with " + str("{:3.2f}".format(percent * 100)) + "% probability\n")
