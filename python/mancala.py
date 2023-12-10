import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT,
    K_ESCAPE,
    QUIT,
    KEYDOWN,
)
pygame.init()

myfont = pygame.font.Font("freesansbold.ttf", 60)
myfont40 = pygame.font.Font("freesansbold.ttf", 40)
myfont80 = pygame.font.Font("freesansbold.ttf", 80)

def printGame(text, location, color = (0,0,0), font = myfont):
    Surface = font.render(text, False, color) #USE FONT TO DISPLAY YOU LOSE, CUS OFC U DID
    Rect = Surface.get_rect()
    Rect.center = location    #DETERMINING WHERE THE FONT WILL GO
    screen.blit(Surface, Rect)


class Grid(pygame.sprite.Sprite):
    def __init__(self):
        super(Grid, self).__init__()
        self.width = 800
        self.height = 200
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((193,154,107))
        self.rect = self.surf.get_rect(center = (400, 300))

    def gridUpdate(self):
        screen.fill((255,255,255))
        zip_brd = list(zip(game.board[7:13][::-1], game.board[:6]))
        screen.blit(self.surf, self.rect)
        for x in range(0, 6):
            for y in range(0, 2):
                circPosn = (150+100*x, 50+100*y)
                numPosn = (150+100*x, 250+100*y)
                circRad = 40
                if mapper[(x,y)] == game.color_pos:
                    pygame.draw.circle(self.surf, (255,0,0) if game.turn == 0 else (0,0,255), circPosn, circRad)
                else:
                    pygame.draw.circle(self.surf, (255,255,255), circPosn, circRad)
                printGame(str(zip_brd[x][y]), numPosn)
        if game.color_pos == 13:
            pygame.draw.rect(self.surf, (255,0,0) if game.turn == 0 else (0,0,255), ((20, 10), (70, 180)))
        else:
            pygame.draw.rect(self.surf, (255,255,255), ((20, 10), (70, 180)))
        if game.color_pos == 6:
            pygame.draw.rect(self.surf, (255,0,0) if game.turn == 0 else (0,0,255), ((710, 10), (70, 180)))
        else:
            pygame.draw.rect(self.surf, (255,255,255), ((710, 10), (70, 180)))
        printGame(str(game.board[13]), (55, 300))
        printGame(str(game.board[6]), (745, 300))
        printGame("Player " + str(game.turn)+ ", Your Move.", (400, 100), (255,0,0) if game.turn == 0 else (0,0,255))

class Pocket(pygame.sprite.Sprite):
    pkt_lst = []
    def __init__(self, posn, name):
        self.posn = posn
        self.name = name
        Pocket.pkt_lst.append([self, name])
        self.surf = pygame.Surface((50,50), pygame.SRCALPHA)
        #pygame.draw.circle(self.surf, (0,0,0), circPosn, 40)
        self.rect = self.surf.get_rect(center = self.posn)

class GameState:
    def __init__(self):
        self.turn = random.randint(0, 1)
        self.board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0] #NNNNNNPNNNNNNP
        self.p0posns = [0,1,2,3,4,5,6]
        self.p1posns = [7,8,9,10,11,12,13]
        self.extra = False
        self.color_pos = None

    def printBoard(self):
        """print("Turn: Player", self.turn)
        print("    ", self.board[7:13][::-1])
        print("", [self.board[13]], "                  ", [self.board[6]])
        print("    ", self.board[:6])
        print("")"""

    def make_turn(self, loc):
        self.extra = False
        count = self.board[loc]
        self.board[loc] = 0
        while count > 0:
            if self == game:
                delay(150)
            loc += 1
            posn = loc % len(self.board)
            self.color_pos = posn
            grid.gridUpdate()
            pygame.display.flip()
            if (posn == 13 and self.turn == 0) or (posn == 6 and self.turn == 1):
                pass
            else:
                count -= 1
                self.checkCapture(count, posn)
                self.board[posn] += 1
                self.printBoard()
                grid.gridUpdate()
                pygame.display.flip()
            if count == 0 and ((self.turn == 0 and posn == 6) or (self.turn == 1 and posn == 13)):
                #print("Extra Turn! Go Again")
                self.printBoard()
                grid.gridUpdate()
                if self == game:
                    printGame("Extra Turn!", (400, 500), (255,0,0) if self.turn == 0 else (0,0,255))
                pygame.display.flip()
                if self == game:
                    delay(1000)
                self.color_pos = None
                grid.gridUpdate()
                pygame.display.flip()
                self.extra = True
        grid.gridUpdate()
        pygame.display.flip()
        if self == game:
            delay(500)
        self.color_pos = None
        grid.gridUpdate()
        pygame.display.flip()
        if self.checkEndGame():
            print("Game Over! The winner is Player", max(0, 1, key = self.playerScore), "with", max(self.playerScore(0), self.playerScore(1)), "points, versus", str(min(self.playerScore(0), self.playerScore(1)))+"!")
            self.extra = False
        elif not self.extra:
            self.turn = 1 - self.turn
            #print("It is Player " + str(self.turn) +"'s turn!")
            self.printBoard()
            grid.gridUpdate()
            pygame.display.flip()

    def make_valid_turn(self, loc):
        assert loc != 6 and loc != 13, "Not allowed to draw from pockets!"
        assert loc < 14 and loc >= 0, "Position Invalid."
        if self.board[loc] != 0 and ((self.turn == 0 and loc in self.p0posns) or (self.turn == 1 and loc in self.p1posns)):
            self.make_turn(loc)

    def playerScore(self, player):
        assert player == 0 or player == 1, "Enter valid player number."
        if player == 0:
            return self.board[6]
        else:
            return self.board[13]

    def checkCapture(self, count, posn):
        if count == 0 and self.board[posn] == 0 and self.board[12-posn] != 0:
            if (self.turn == 0 and posn in self.p0posns[:6]):
                self.board[6] += (1 + self.board[12 - posn])
                self.board[posn] = 1
                if self == game:
                    screen.fill((255,255,255))
                    grid.gridUpdate()
                    printGame("Captured " + str(self.board[12-posn]) + "!", (400, 500),(255,0,0) if self.turn == 0 else (0,0,255))
                    pygame.display.flip()
                    if self == game:
                        delay(1500)
                self.board[posn], self.board[12 - posn] = -1, 0
            elif (self.turn == 1 and posn in self.p1posns[:6]):
                self.board[13] += (1 + self.board[12 - posn])
                self.board[posn] = 1
                if self == game:
                    screen.fill((255,255,255))
                    grid.gridUpdate()
                    printGame("Captured " + str(self.board[12-posn]) + "!", (400, 500), (255,0,0) if self.turn == 0 else (0,0,255))
                    pygame.display.flip()
                    if self == game:
                        delay(1500)
                self.board[posn], self.board[12 - posn] = -1, 0


    def checkEndGame(self):
        game_end_val = not any(self.board[:6]) or not any(self.board[7:13])
        return game_end_val

def delay(time):
    before = pygame.time.get_ticks()
    while True:
        now = pygame.time.get_ticks()
        if now - before >= time:
            break

comp = input("Would you like to play against a Computer? (Y/N): ")
comp = (comp.lower() == "y")
if comp:
    diff = int(input("Enter Difficulty (1 - Easy, 2 - Hard or 3 - Insane): "))
else:
    diff = 0

def compStrat(score0, score1, board, diff = diff):
    if diff == 1:
        rv = random.randint(7, 12)
        if board[rv] > 0:
            return rv
        else:
            return compStrat(score0, score1, board)
    elif diff == 2:
        for i in range(1,7):
            if i == board[13-i]:
                return 13-i
        return compStrat(score0, score1, board, 1)
    elif diff == 3:
        return futureDecider(board[:], game.turn, score1)

def futureDecider(board, turn, score1):
    scores = {}
    for i in range(7, 13):
        scores[i] = one_futureTester(board[:], turn, i)
    return max(7,8,9,10,11,12, key = lambda pos: scores[pos])



def one_futureTester(board, turn, loc):
    #print("Predicted One Possible Future Outcome")
    futuregame = GameState()
    futuregame.board = board
    futuregame.turn = turn
    if futuregame.board[loc] > 0:
        futuregame.make_valid_turn(loc)
        if futuregame.extra:
            finalscore = []
            for i in range(7,13):
                finalscore.append(one_futureTester(futuregame.board[:], futuregame.turn, i))
            max_score = max(finalscore)
        else:
            max_score = futuregame.playerScore(1)
        #print("End Score:", max_score)
        return max_score
    return -1




screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN) #MAKE SCREEN IN PYGAME
screen.fill((255,255,255))
grid = Grid()
game = GameState()
game.printBoard()
running = True
mapper = {(0,0): 12, (1,0): 11, (2,0): 10, (3,0): 9, (4,0): 8, (5,0): 7, (0,1): 0, (1, 1): 1, (2, 1): 2, (3, 1): 3, (4, 1): 4, (5,1): 5}

for x in range(0, 6):
    for y in range(0, 2):
        circPosn = (150+100*x, 250+100*y)
        loc = mapper[(x, y)]
        pocket = Pocket(circPosn, loc)

grid.gridUpdate()
grid.gridUpdate()
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == QUIT: #SO THAT THE X BUTTON WORKS TO CLOSE THE GAME OTHERWISE IT WILL RUN FOREVER. THAT IS BAD.
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  #IF A BUTTON IS PRESSED:
            mposx, mposy = pygame.mouse.get_pos()
            for pocket in Pocket.pkt_lst:
                if pocket[0].rect.collidepoint(mposx, mposy):
                    game.make_valid_turn(pocket[1])
            if comp:
                while game.turn == 1 and not game.checkEndGame():
                    delay(500)
                    game.make_valid_turn(compStrat(game.playerScore(0), game.playerScore(1), game.board))

    if game.checkEndGame():
        delay(400)
        end = "Game Over!"
        end4 = "Player " + str(max(0, 1, key = game.playerScore)) + " Wins!"
        end2 = "Player 0: "+ str(game.playerScore(0))
        end3 = "Player 1: "+ str(game.playerScore(1))
        if max(0, 1, key = game.playerScore) == 0:
            win_color = (255,0,0)
        else:
            win_color = (0,0,255)
        screen.fill((255,255,255))
        printGame(end, (400, 150), (0,0,0), myfont)
        printGame(end4, (400, 270), win_color, myfont80)
        printGame(end2, (400, 380), (255,0,0), myfont40)
        printGame(end3, (400, 440), (0,0,255), myfont40)
        pygame.display.flip()
