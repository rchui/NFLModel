class Team(object):

    def __init__(self, name):
        self.name = name

    def buildTeam(self, rushingData, passingData, kickingData, returningData, puntingData, downData, playData):
        self.playData = playData
        self.rushYA = rushingData[self.name][2]
        self.rushLong = rushingData[self.name][3]
        self.passYA = passingData[self.name][4]
        self.passComp = passingData[self.name][2]
        self.passLong = passingData[self.name][5]
        self.returnKYA = returningData[self.name][2]
        self.returnKLong = returningData[self.name][3]
        self.returnPYA = returningData[self.name][7]
        self.returnPLong = returningData[self.name][8]
        self.fgComp = kickingData[self.name][2]
        self.fgLong = kickingData[self.name][3]
        self.epComp = kickingData[self.name][6]
        self.puntYA = puntingData[self.name][3]
        self.puntLong = puntingData[self.name][2]
        self.rush1 = downData[self.name][1] / (downData[self.name][1] + downData[self.name][2])
        self.pass1 = downData[self.name][2] / (downData[self.name][1] + downData[self.name][2])
