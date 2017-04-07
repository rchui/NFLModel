import sys
from src.Utilities import DataReader
from src.Team import Team

name = sys.argv[1]
down = sys.argv[2]
distance = sys.argv[3]
field = sys.argv[4]

# Read in team stats
dataReader = DataReader()
rushingData = dataReader.statReader("Rushing.csv")
passingData = dataReader.statReader("Passing.csv")
kickingData = dataReader.statReader("Kicking.csv")
returningData = dataReader.statReader("Returning.csv")
puntingData = dataReader.statReader("Punting.csv")

# Read in play percentages
playData = dataReader.playReader("Percent.csv")

team = Team(name)
team.buildTeam(rushingData, passingData, kickingData, returningData, puntingData, playData)


