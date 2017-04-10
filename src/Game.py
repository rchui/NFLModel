import random
import sys

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
        self.quarter = 1
        self.time = 900

        print("\t" + self.team1.name[:7] + "\t\t" + self.team2.name[:7])
        print("\t" + str(self.score1) + "\t\t" + str(self.score2))
        print("\t" + str(self.down) + " | " + str(self.distance) + "\t\t" + str(self.field))
        m, s = divmod(self.time, 60)
        print ("\tQuarter " + str(self.quarter) + "\t%02d:%02d" % (m, s))

        print("\nFlipping Coin...")
        if random.random() > 0.5:
            print(self.team1.name + " will start with the ball.")
            self.possession = 1
        else:
            print(self.team2.name + " will start with the ball.")
            self.possession = 2
        print("")

       

    def playGame(self, possession):
        def switchPoss():
            if self.possession == 1:
                self.possession = 2
            else:
                self.possession = 1

        def processPlay(play, result, team, distance):
            # Get length of play
            playLength = int(round(random.normalvariate(30, 5)))
            print(str(playLength) + " seconds\n")

            # Adjust time
            self.time -= playLength
            if self.time < 0:
                self.time = 900
                self.quarter += 1

            # Field goal
            if play == "fg":
                if result == "success":
                    if self.possession == 1:
                        self.score1 += 3
                    else:
                        self.score2 += 3
                    self.field = 25
                else: # result == "failure"
                    self.field = 100 - self.field
                self.down = 1
                self.distance = 10
                switchPoss()
            # Punt
            elif play == "punt":
                switchPoss()
                self.down = 1
                self.distance = 10
                self.field = 100 - (self.field + distance)
                if self.field <= 0:
                    self.field = 25
            # Run/Pass
            else:
                self.distance -= distance
                if self.distance <= 0: # Reached first down
                    self.distance = 10
                    self.down = 1
                    print(team.name + " first down!")
                else: # self.distance > 0
                    self.down += 1
                self.field += distance
                if self.field >= 100: # Reached endzone
                    self.down = 1
                    self.distance = 10
                    self.field = 25
                    if self.possession == 1:
                        self.score1 += 7
                    else:
                        self.score2 += 7
                    switchPoss()

            # Print box
            if self.possession == 1:
                print("\t*")
            else:
                print("\t\t\t*")
            print("\t" + self.team1.name[:7] + "\t\t" + self.team2.name[:7])
            print("\t" + str(self.score1) + "\t\t" + str(self.score2))
            print("\t" + str(self.down) + " | " + str(self.distance) + "\t\t" + str(int(self.field)))
            if self.quarter <= 4:
                m, s = divmod(self.time, 60)
                print ("\tQuarter " + str(self.quarter) + "\t%02d:%02d\n" % (m, s))
            if self.quarter > 4:
                print("")
                print("Game Over!")
                if self.score1 > self.score2:
                    print(self.team1.name + " wins by a score of " + str(self.score1) + " to " + str(self.score2) + "!")
                elif self.score2 > self.score1:
                    print(self.team2.name + " wins by a score of " + str(self.score2) + " to " + str(self.score1) + "!")
                else:
                    print(self.team1.name + " ties " + self.team2.name + " at " + str(self.score2) + " to " + str(self.score1))

        if possession == 1:
            team = self.team1
        else:
            team = self.team2

        # Choose a play
        play = team.nextPlay(self.down, self.distance, self.field)
        if play == "fg":
            print("Attempting Field Goal: ")
            if team.fgComp / 100 > random.random():
                print(str(100 - self.field + 17) + " yard field goal completed")
                processPlay(play, "success", team, 0)
            else:
                print(str(100 - self.field + 17) + " yard field goal missed")
                processPlay(play, "failure", team, 0)
        elif play == "punt":
            print("Punting: ")
            puntDeviation = (team.puntLong - team.puntYA) / 3
            puntDistance = team.puntYA - random.randint(0, 3) * puntDeviation + random.randint(0, 3) * puntDeviation
            print("Punted " + str(int(round(puntDistance))) + " yards")
            processPlay(play, "success", team, puntDistance)
        else:
            print(str(int(play)) + " yards")
            processPlay(play, "success", team, int(play))

    def displayGame(self):
        sys.stdout.write("|")
        for i in range(99):
            sys.stdout.write("-")
        sys.stdout.write("|\n")
        sys.stdout.flush()

        for i in range(4):
            sys.stdout.write("|")
            for j in range(10):
                sys.stdout.write("         |")
            sys.stdout.write("\n")
            sys.stdout.flush()

        for i in range(10):
            if (int(self.field) / 10 == i):
                if int(self.field) % 10 == 0:
                    sys.stdout.write("*         ")
                else:
                    sys.stdout.write("|")
                    for i in range(int(self.field) % 10 - 1):
                        sys.stdout.write(" ")
                    sys.stdout.write("*")
                    for i in range(10 - (int(self.field) % 10) - 1):
                        sys.stdout.write(" ")
            else:
                sys.stdout.write("|         ")
        sys.stdout.write("|\n")
        sys.stdout.flush()

        for i in range(4):
            sys.stdout.write("|")
            for j in range(10):
                sys.stdout.write("         |")
            sys.stdout.write("\n")
            sys.stdout.flush()

        sys.stdout.write("|")
        for i in range(99):
            sys.stdout.write("-")
        sys.stdout.write("|\n\n")
        sys.stdout.flush()
