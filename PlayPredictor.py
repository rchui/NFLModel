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
play = team.nextPlay(down, distance, field)
if play == "fg":
    print("Attempting Field Goal: ")
    if team.fgComp / 100 > random.random():
        print(str(100 - field + 17) + " yard field goal completed\n")
    else:
        print(str(100 - field + 17) + " field goal missed\n")
elif play == "punt":
    print("Punting: ")
    puntDeviation = (team.puntLong - team.puntYA) / 3
    puntDistance = team.puntYA - random.randint(0, 3) * puntDeviation + random.randint(0, 3) * puntDeviation
    print("Punted " + str(int(round(puntDistance))) + " yards\n")
else:
    print(str(int(play)) + " yards\n")
