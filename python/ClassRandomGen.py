import random

class Player:
	score = 0

	def __init__(self, playern):
		print("Enter name of Player"+playern+":")
		self.name = input()

	def printScore(self):
		print(self.score)

	def guessNumber(self):
		print(self.name + " Guess a number between 1-100")
		self.guess = int(input())


class Game:

	def __init__(self):
		self.rand = 0
		self.p1 = Player(1)
		self.p2 = Player(2)

		print("How many games do you want to play?")
		self.counter = int(input())

	def playGame(self):
		self.rand = random.randint(1, 100)
		i = 0
		while i < self.counter:
			self.p1.guessNumber()
			self.p2.guessNumber()
			self.compareNumber(self.p1.guess, self.p2.guess)
			i += 1;
		print("Score for Player 1 vs Player 2 is:" + str(self.p1.score) + "-" + str(self.p2.score))

	def compareNumber(self, p1Guess, p2Guess):
		gap1 = abs(self.rand - p1Guess)
		gap2 = abs(self.rand - p2Guess)
		if gap1 < gap2:
			self.p1.score += 1
		else:
			self.p2.score += 1



myGame = Game()
myGame.playGame()
