class Game:
    def __init__(self):
        self.play = 0
    def complete(self):
        self.play = 10
        print(self.play)

myGame = Game()
Game.complete()
