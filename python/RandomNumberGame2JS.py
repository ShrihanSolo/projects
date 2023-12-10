import random
import getpass

class Game:
    classVariable = 0

    def __init__(self):
        self.play = 0

    def playerNameInput(self):
        print("Inside playerNameInput")
        self.playCount()
        self.playerName()

    def playCount(self):
        print("How many times do you want to play?")
        self.play = int(input())

    def playerName(self):
        print("What is Player 1's name?")
        self.P1name = input()
        print("What is Player 2's name?")
        self.P2name = input()

    def complete(self):
        print("Inside complete")
        self.playerNameInput()


#myGame = Game()
#myGame.complete()


class Player:
# Static variable - common for all the players
    playerCount = 0

# Member Functions
    def __init__(self, name):
        # Member variable
        self.playerName = name
        Player.addNumberOfPlayers()

    def printPlayerName(self):
        print(self.playerName)

#static function - which are common for all the Player class
    def addNumberOfPlayers():
        Player.playerCount += 1

    def printPlayerCount():
        print(Player.playerCount)

sPlayer = Player("Shrihan")
jPlayer = Player("Jayashree")
Player.printPlayerCount()
