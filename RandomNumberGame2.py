import random
import getpass

class Game:

    def __init__(self):
        self.play = 0
        self.P1Diff = 0
        self.P2Diff = 0
        self.Comp = 0
        self.P1W = 0
        self.P2W = 0
        self.maj = 0

    def playCount(self):
        print("How many times do you want to play?")
        self.play = int(input())

    def playerName(self):
        print("What is Player 1's name?")
        self.P1name = input()
        print("What is Player 2's name?")
        self.P2name = input()

    def playerNameInput(self):
        self.playCount()
        self.playerName()

    def playGameinput(self):
        print(self.P1name+", please enter your guess (A number between 1 and 100):")
        self.P1 = int(getpass.getpass())
        print(self.P2name+", please enter your guess (A number between 1 and 100):")
        self.P2 = int(getpass.getpass())

    def calculations(self):
        self.Comp = random.randint(1,100)
        self.P1Diff = abs(self.P1 - self.Comp)
        self.P2Diff = abs(self.P2 - self.Comp)

    def p1Win(self):
        print(self.P1name+"'s number was "+str(self.P1)+" and "+self.P2name+"'s number was "+str(self.P2)+".")
        print(self.P1name+" wins! The number is "+str(self.Comp)+"!")
        self.P1W = self.P1W + 1
        print("The score is "+str(self.P1W)+"-"+str(self.P2W)+"!")

    def p2Win(self):
        print(self.P1name+"'s number was "+str(self.P1)+" and "+self.P2name+"'s number was "+str(self.P2)+".")
        print(self.P2name+" wins! The number is "+str(self.Comp)+"!")
        self.P2W = self.P2W + 1
        print("The score is "+str(self.P1W)+"-"+str(self.P2W)+"!")

    def tie(self):
        print(self.P1name+"'s number was "+str(self.P1)+" and "+self.P2name+"'s number was "+str(self.P2)+".")
        print("It's a tie! The number was "+str(self.Comp)+"!")
        print("Its time to restart the game!")
        print("The score is "+str(self.P1W)+"-"+str(self.P2W)+"!")
        self.playGame()

    def majorityRules(self):
        if (self.play % 2) == 0:
            self.maj = (1+(self.play)/2)
        elif (self.play % 2) == 1:
            self.maj = (0.5+(self.play)/2)
        else:
            print("Please do not enter decimals in number of games.")

    def majorityP1(self):
        print(self.P1name+" has won the majority of games: "+str(int(self.maj))+" games.")

    def majorityP2(self):
        print(self.P2name+" has won the majority of games: "+str(int(self.maj))+" games.")

    def winLogic(self):
        i = 0
        while i < self.play and self.P2W <= (self.play/2) and self.P1W <= (self.play/2):
            print("Game "+str(i+1)+":")
            self.playGame()
            i += 1
        else:
            if self.P1W > (self.play/2):
                self.majorityP1()
            elif self.P2W > (self.play/2):
                self.majorityP2()
            print("Thank you for playing!")

    def playGame(self):
        self.playGameinput()
        self.calculations()
        if self.P1Diff < self.P2Diff:
            self.p1Win()
        elif self.P1Diff > self.P2Diff:
            self.p2Win()
        else:
            self.Tie()

    def complete(self):
        self.playerNameInput()
        self.majorityRules()
        self.winLogic()

obj = Game()
obj.complete()
