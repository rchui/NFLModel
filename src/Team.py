import random

class Team(object):

    def __init__(self, name):
        self.name = name

    def buildTeam(self, rushingData, passingData, kickingData, returningData, puntingData, downData, playData):
        """ Builds the team based on the read in data.
        
        @params:
            :rushingData: rushing data
            :kickingData: kicking data
            :returningData: return data
            :puntingData: punt data:
            :downData: play data
        """
        #Rushing data
        self.playData = playData
        self.rushYA = rushingData[self.name][2]
        self.rushLong = rushingData[self.name][3]

        # Passing data
        self.passYA = passingData[self.name][4]
        self.passComp = passingData[self.name][2]
        self.passLong = passingData[self.name][5]

        # Kick return data
        self.returnKYA = returningData[self.name][2]
        self.returnKLong = returningData[self.name][3]
        self.returnPYA = returningData[self.name][7]
        self.returnPLong = returningData[self.name][8]

        # Field goal data
        self.fgComp = kickingData[self.name][2]
        self.fgLong = kickingData[self.name][3]

        # Extra Point data
        self.epComp = kickingData[self.name][6]

        # Punting data
        self.puntYA = puntingData[self.name][3]
        self.puntLong = puntingData[self.name][2]

        # Pass vs Rush data
        self.rush1 = downData[self.name][1] / (downData[self.name][1] + downData[self.name][2])
        self.pass1 = downData[self.name][2] / (downData[self.name][1] + downData[self.name][2])

        # Rushing percentage data
        self.rushCenter = 0.3453
        self.rushRightEnd = self.rushCenter + 0.2155
        self.rushLeftEnd = self.rushRightEnd + 0.1381
        self.rushRightGuard = self.rushLeftEnd + 0.1050
        self.rushLeftGuard = self.rushRightGuard + 0.081
        self.rushLeftTackle = self.rushLeftGuard + 0.058
        self.rushRightTackle = self.rushLeftTackle + 0.058

    def nextPlay(self, down, distance, field):
        """ Determines the next play by the team.

        @params:
            :down: down the team is playing on
            :distance: distance from the first yard line marker
            :field: position on the field
            :returns: play information, new down, distance, and field

        """
        def passing():
            """ Determines passing distance """
            direct = ["Left", "Right", "Middle"]

            if random.random() < 0.80: # short pass
                print("Short Pass " + random.choice(direct) +  ": ")
                if random.random < self.passComp:
                    return round(random.uniform(0, self.passYA) - random.randint(0, round(self.passYA)) + random.randint(2, round(self.passYA)))
                else:
                    return 0

            else: # long pass:
                choice = random.random()
                if choice < 0.4:
                    direct = "Left"
                elif choice < 0.8:
                    direct = "Right"
                else:
                    direct = "Middle"
                print("Long Pass " + direct + ": ")
                if random.random() < self.passComp:
                    return max(round(random.uniform(self.passYA, self.passLong) - random.randint(round(self.passYA), round(self.passLong))), 10)
                else:
                    return 0

        def rushing():
            """ Determines rushing distance """
            playPer = random.random()
            perTracker = 0
            
            if playPer < (self.rushCenter):
                print("Rush Center: ")
                return round(random.uniform(0, self.rushYA) - random.randint(0, round(self.rushYA)) + random.randint(0, round(self.rushYA)))
            perTracker += self.rushCenter
            
            if playPer < self.rushRightEnd:
                print("Rush Right End: ")
                return round(self.rushYA - random.randint(0, round(self.rushYA)) + random.randint(0, round(self.rushYA)))
            perTracker += self.rushRightEnd
            
            if playPer < self.rushLeftEnd:
                print("Rush Left End: ")
                return round(self.rushYA - random.randint(0, round(self.rushYA)) + random.randint(0, round(self.rushYA)))
            perTracker += self.rushLeftEnd
            
            if playPer < self.rushRightGuard:
                print("Rush Right Guard: ")
                return round(self.rushYA - random.randint(0, round(self.rushYA)) + random.randint(0, round(self.rushYA)))
            perTracker += self.rushRightGuard
            
            if playPer < self.rushLeftGuard:
                print("Rush Left Guard: ")
                return round(self.rushYA - random.randint(0, round(self.rushYA)) + random.randint(0, round(self.rushYA)))
            perTracker += self.rushLeftGuard

            if playPer < self.rushLeftTackle:
                print("Rush Left Tackle: ")
                playDist = round(random.uniform(self.rushYA, self.rushLong) - random.randint(round(self.rushYA), round(self.rushLong)))
                return max(random.randint(-5, 0), playDist)
            perTracker += self.rushLeftTackle
            
            print("Rush Right Tackle: ")
            playDist = round(random.uniform(self.rushYA, self.rushLong) - random.randint(round(self.rushYA), round(self.rushLong)))
            return max(random.randint(-5, 0), playDist)

        if down == 1:
            if self.rush1 > random.random():
                return rushing()
            else:
                return passing()
        elif down == 2:
            if distance > 7:
                return passing()
            elif distance < 4:
                return rushing()
            else: # distance > 3 || distance < 7
                if random.random() > 0.5:
                    return rushing()
                else:
                    return passing()
        elif down == 3:
            if distance > 4:
                return passing()
            else: 
                if random.random() > 0.5:
                    return rushing()
                else:
                    return passing()
        else:
            # Kick field goal if in range
            if 100 - field + 17 <= self.fgLong and distance > 2:
                return "fg"
            # If close enough maybe go for it on 4th
            elif 100 - field + 17 <= self.fgLong and distance  < 3:
                if random.random() < 0.90:
                    return "fg"
                else:
                    if distance == 1:
                        return rushing()
                    else:
                        return passing()
            # If close but not in range sometimes go for it
            elif 100 - field > 50 and distance < 3:
                if random.random() > 0.975:
                    if distance == 1:
                        return rushing()
                    else:
                        return passing()
                else:
                    return "punt"
            # Otherwise punt
            else:
                return "punt"

