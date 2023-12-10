#IMPORTING NECESSARY MODULES
import pygame
import time
import random

#IMPORTING KEY STROKES
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT,
    K_ESCAPE,
    QUIT,
    KEYDOWN,
    K_a,
    K_w,
    K_s,
    K_d,
)
pygame.init()

#CREATING SNAKE'S HEAD SPRITE CLASS
class Snake(pygame.sprite.Sprite):
    def __init__(self, snakePosn, color):
        super(Snake, self).__init__()   #INHERITING FROM SPRITE CLASS IN PYGAME MODULE
        self.surf = pygame.Surface((25,25))    #CREATING SHAPE HEAD OF SNAKE
        self.surf.fill((color))   #COLORING THE HEAD
        self.x = 0  #INITIALIZING X,Y SPEED VARIABLES
        self.y = 0
        self.rect = self.surf.get_rect(center = (snakePosn, (Height/2 - 13))) #INITIAL lOCATION OF HEAD
        self.posList = []
        self.tailLength = 7

    def updateDir(self, X, Y): #FUNCTION TO CHANGE SNAKE'S DIRECTION (X,Y SPEED)
        self.x = X
        self.y = Y
        self.posList.append([X, Y])
        if len(self.posList) > self.tailLength:
            self.posList.pop(0)

    def updatePosn(self):
        self.rect.move_ip(self.x, self.y)   #FUNCTION TO CHANGE X,Y POSITION BASED ON X,Y SPEED



class Tail(pygame.sprite.Sprite):
    def __init__(self, lengthno, posnx, posny, color):
        super(Tail, self).__init__() #INHERITING
        self.surf = pygame.Surface((25,25)) #CREATING A TAIL BLOCK
        self.surf.fill((color))
        self.num = lengthno #THE NUMBER OF THE BLOCK, AKA, WHICH BLOCK OF TAIL IS IT?
        self.posnx = posnx  # X,Y POSITION TO CREATE THE BLOCK
        self.posny = posny
        self.x = 0
        self.y = 0
        self.rect = self.surf.get_rect(center = ((self.posnx), (self.posny))) #CREATING THE BLOCK AT X,Y POSN
        self.posList = []

    def updatePosn(self):
        self.rect.move_ip(self.x, self.y) #MOVE TAILBLOCK ACC TO X,Y SPEED

    def updateDir(self):
        self.x = self.posList[-self.num-1][0] #MOVE TAIL BLOCK ACC TO THE SPEED OF THE PREVIOUS BLOCK IN THE SEQUENCE DURING THE TURN BEFORE IT (SO THAT IT FOLLOWS THE SAME PATH)
        self.y = self.posList[-self.num-1][1]



class Grid(pygame.sprite.Sprite): #MAKING ONE USELESS GRID...IF YOU'RE NOT USING IT, IGNORE THIS CLASS
    def __init__(self):
        super(Grid, self).__init__()
        for CboxNo in range(0, 24):
            boxPosnY = CboxNo*25 + 12.5
            for RboxNo in range(0, 32):
                boxPosnX = RboxNo*(25) + 12.5
                self.surf2 = pygame.Surface((23,23))
                self.surf2.fill((0,0,0))
                self.rect2 = self.surf2.get_rect(
                    center = (
                        boxPosnX,
                        boxPosnY,
                    )
                )
                screen.fill((255,255,255))
                screen.blit(self.surf2, self.rect2)

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super(Food, self).__init__()
        self.surf = pygame.Surface((19,19)) #TINY RED FOOD BLOCK :)
        self.surf.fill((255,165,0))  #RED COLOR FOOD BLOCK!
        self.x = random.randint(0, 31)*25 + 12.5 #RANDOM POSITION FOR BLOCK. FIRST RANDOM BLOCK ON GRID, AND THEN 12.5 IS ADDED TO PUT IT IN THE CENTER OF BOTH
        self.y = random.randint(0, 23)*25 + 12.5
        self.rect = self.surf.get_rect(center = ((self.x),(self.y)))    #CENTERING BLOCK ON THE RANDOM COORDS

    def newFood(self):
        self.x = random.randint(0, 31)*25 + 12.5    #MAKING A NEW RANDOM COORDS
        self.y = random.randint(0, 23)*25 + 12.5
        self.rect = self.surf.get_rect(center = ((self.x),(self.y))) #CENTERING NEW FOOD ON THIS SPOT

class Wall(pygame.sprite.Sprite):
    def __init__(self, shape, location):
        super(Wall, self).__init__()
        self.surf = pygame.Surface(shape)
        self.surf.fill((255,255,255))
        (self.x, self.y) = location
        self.rect = self.surf.get_rect(center = (location))

def printGame(text, location, color, font):
    lossSurface = font.render(text, False, color) #USE FONT TO DISPLAY YOU LOSE, CUS OFC U DID
    lossRect = lossSurface.get_rect()
    lossRect.center = location    #DETERMINING WHERE THE FONT WILL GO
    screen.blit(lossSurface, lossRect)

#INITIALIZATION OF VARIABLES


Width = 800 #OF SCREEN
Height = 600
fps = int(input("Enter speed (From 10-50): "))  #UK WHAT THIS IS - FPS DETERMINES HOW MANY TIMES THE UPCOMING WHILE LOOP RUNS PER SECOND
norounds = int(input("Enter number of rounds (From 1-10): "))
screen = pygame.display.set_mode((Width, Height), pygame.FULLSCREEN) #MAKE SCREEN IN PYGAME

TIMEDMOVE = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEDMOVE, 1000//fps)

running = True
snakeSpeed = 25 #DO NOT CHANGE THIS, CHANGE FPS TO CHANGE SPEED
snake1x = snakeSpeed #INITIALIZED FOR SNAKE TO BE GOING RIGHT
snake1y = 0
snake2x = -snakeSpeed #INITIALIZED FOR SNAKE TO BE GOING RIGHT
snake2y = 0
cont = 1 #DECIDES IF GAME SHOULD GO ON
clock = pygame.time.Clock()
dir = "R"
dir2 = "L"

snake1 = Snake(63, (0,255,0)) #MAKES THE SNAKE HEAD!
snake2 = Snake((800-63), (255,0,0))
food = Food() #MAKES THE FIRST FOOD AT RANDOM SPOT

leftWall = Wall((25,Height), (13, (Height/2)))
rightWall = Wall((25,Height), (Width-12, (Height/2)))
topWall = Wall((Width,25), ((Width/2), 12))
botWall = Wall((Width,25), ((Width/2), Height-13))

foodGroup = pygame.sprite.Group()
foodGroup.add(food) #GROUP OF SPRITES CONSISTING OF ALL THE FOOD
tailGroup1 = pygame.sprite.Group() #GROUP OF SPRITES CONSISTING OF ALL THE TAIL BLOCKS
tailGroup2 = pygame.sprite.Group() #GROUP OF SPRITES CONSISTING OF ALL THE TAIL BLOCKS


tail = [] #THE LIST THAT CONTAINS ALL THE TAIL BLOCK CLASSES - MOST IMP LIST!
tail2 = []
for i in range(0, snake1.tailLength): #TAILLENGTH REALLY IS JUST SNAKE LENGTH
    tail.append(Tail(i, (63-(25*i)), (((Height/2)-13)), (0,255,0))) #ADDING THE INITIAL TAILS BEFORE THE START OF THE GAME
    if i != 0:
        tailGroup1.add(tail[i])  #DONT ADD THE FIRST BLOCK OF TAIL TO COLLISION GRP. THE FIRST BLOCK OF TAIL IS BEHIND THE HEAD, IF PART OF COLLISION GRP, IMMEDIATE D

for i in range(0, snake2.tailLength):
    tail2.append(Tail(i, ((800-63)+(25*i)), (((Height/2)-13)), (255,0,0))) #ADDING THE INITIAL TAILS BEFORE THE START OF THE GAME
    if i != 0:
        tailGroup2.add(tail2[i])  #DONT ADD THE FIRST BLOCK OF TAIL TO COLLISION GRP. THE FIRST BLOCK OF TAIL IS BEHIND THE HEAD, IF PART OF COLLISION GRP, IMMEDIATE D

snake1.tailLength = 7 #INITIAL SNAKE LENGTH = 7
snake2.tailLength = 7
snake1.posList = [[25, 0], [25, 0], [25, 0], [25, 0], [25, 0], [25, 0]] #INITIAL X,Y SPEEDS LIST FOR 3 TAIL BLOCKS
snake2.posList = [[-25, 0], [-25, 0], [-25, 0], [-25, 0], [-25, 0], [-25, 0]]

totalScore1 = 0
totalScore2 = 0
round = 0

while running == True: #WHILE LOOP!
    for event in pygame.event.get():
        if event.type == QUIT: #SO THAT THE X BUTTON WORKS TO CLOSE THE GAME OTHERWISE IT WILL RUN FOREVER. THAT IS BAD.
            running = False
        if event.type == KEYDOWN:  #IF A BUTTON IS PRESSED:
            if event.key == K_ESCAPE:
                running = False     #RUNNING FALSE KILLS THE GAME IMMEDIATELY, SO ESC ALSO KILLS THE GAME
            if event.key == K_UP:
                dir = "U"
            elif event.key == K_DOWN:
                dir = "D"
            elif event.key == K_RIGHT:
                dir = "R"
            elif event.key == K_LEFT:
                dir = "L"
            if event.key == K_w:
                dir2 = "U"
            elif event.key == K_s:
                dir2 = "D"
            elif event.key == K_d:
                dir2 = "R"
            elif event.key == K_a:
                dir2 = "L"
        if event.type == TIMEDMOVE:
            if dir == "U":
                if (snake2x, snake2y) != (0, snakeSpeed):     #IF THE SNAKE IS GOING DOWN, UP BUTTON DOESNT WORK, SIMILAR FOR REST
                    snake2x = 0                              #CHANGE X,Y SPEED OF SNAKE!
                    snake2y = -snakeSpeed
            if dir == "D":
                if (snake2x, snake2y) != (0, -snakeSpeed):
                    snake2x = 0
                    snake2y = snakeSpeed
            if dir == "R":
                if (snake2x, snake2y) != (-snakeSpeed, 0):
                    snake2x = snakeSpeed
                    snake2y = 0
            if dir == "L":
                if (snake2x, snake2y) != (snakeSpeed, 0):
                    snake2x = -snakeSpeed
                    snake2y = 0
            if dir2 == "U":
                if (snake1x, snake1y) != (0, snakeSpeed):     #IF THE SNAKE IS GOING DOWN, UP BUTTON DOESNT WORK, SIMILAR FOR REST
                    snake1x = 0                              #CHANGE X,Y SPEED OF SNAKE!
                    snake1y = -snakeSpeed
            if dir2 == "D":
                if (snake1x, snake1y) != (0, -snakeSpeed):
                    snake1x = 0
                    snake1y = snakeSpeed
            if dir2 == "R":
                if (snake1x, snake1y) != (-snakeSpeed, 0):
                    snake1x = snakeSpeed
                    snake1y = 0
            if dir2 == "L":
                if (snake1x, snake1y) != (snakeSpeed, 0):
                    snake1x = -snakeSpeed
                    snake1y = 0

        if event.type == KEYDOWN:  #IF A BUTTON IS PRESSED:
            if event.key == K_ESCAPE:
                running = False     #RUNNING FALSE KILLS THE GAME IMMEDIATELY, SO ESC ALSO KILLS THE GAME
            if event.key == K_w:
                if (snake1x, snake1y) != (0, snakeSpeed):     #IF THE SNAKE IS GOING DOWN, UP BUTTON DOESNT WORK, SIMILAR FOR REST
                    snake1x = 0                              #CHANGE X,Y SPEED OF SNAKE!
                    snake1y = -snakeSpeed
            elif event.key == K_s:
                if (snake1x, snake1y) != (0, -snakeSpeed):
                    snake1x = 0
                    snake1y = snakeSpeed
            elif event.key == K_d:
                if (snake1x, snake1y) != (-snakeSpeed, 0):
                    snake1x = snakeSpeed
                    snake1y = 0
            elif event.key == K_a:
                if (snake1x, snake1y) != (snakeSpeed, 0):
                    snake1x = -snakeSpeed
                    snake1y = 0
            if event.key == K_UP:
                if (snake2x, snake2y) != (0, snakeSpeed):     #IF THE SNAKE IS GOING DOWN, UP BUTTON DOESNT WORK, SIMILAR FOR REST
                    snake2x = 0                              #CHANGE X,Y SPEED OF SNAKE!
                    snake2y = -snakeSpeed
            elif event.key == K_DOWN:
                if (snake2x, snake2y) != (0, -snakeSpeed):
                    snake2x = 0
                    snake2y = snakeSpeed
            elif event.key == K_RIGHT:
                if (snake2x, snake2y) != (-snakeSpeed, 0):
                    snake2x = snakeSpeed
                    snake2y = 0
            elif event.key == K_LEFT:
                if (snake2x, snake2y) != (snakeSpeed, 0):
                    snake2x = -snakeSpeed
                    snake2y = 0

    if pygame.sprite.spritecollideany(snake1, foodGroup): #IF SNAKE COLLIDES WITH FOOD, THEN DO THIS
        food.newFood()  #CREATES A NEW FOOD
        snake1.tailLength += 1     #SNAKE BECOMES BIGGER DUE TO FOOD, ALSO DEFINES X,Y SPEED OF NEW TAIL BLOCK
        tail.append(Tail((snake1.tailLength-1), ((tail[-1].rect.centerx)), ((tail[-1].rect.centery)), (0,255,0)))     #PUT A NEW TAIL BLOCK AT THE PREV POSN OF THE BLOCK AT THE END OF TAIL
        tailGroup1.add(tail[-1]) #ADD TAIL TO COLLISION GROUP

    if pygame.sprite.spritecollideany(snake2, foodGroup): #IF SNAKE COLLIDES WITH FOOD, THEN DO THIS
        food.newFood()  #CREATES A NEW FOOD
        snake2.tailLength += 1     #SNAKE BECOMES BIGGER DUE TO FOOD, ALSO DEFINES X,Y SPEED OF NEW TAIL BLOCK
        tail2.append(Tail((snake2.tailLength-1), ((tail2[-1].rect.centerx)), ((tail2[-1].rect.centery)), (255,0,0)))     #PUT A NEW TAIL BLOCK AT THE PREV POSN OF THE BLOCK AT THE END OF TAIL
        tailGroup2.add(tail2[-1]) #ADD TAIL TO COLLISION GROUP

    for i in range(0, snake1.tailLength):
        tail[i].posList = snake1.posList
    for i in range(0, snake2.tailLength):
        tail2[i].posList = snake2.posList

    if pygame.sprite.spritecollideany(snake1, tailGroup1):    #IF SNAKE HITS TAIL, STOP GAME
        cont = 0

    if pygame.sprite.spritecollideany(snake1, tailGroup2):    #IF SNAKE HITS TAIL, STOP GAME
        cont = 0

    if pygame.sprite.spritecollideany(snake2, tailGroup1):    #IF SNAKE HITS TAIL, STOP GAME
        cont = -1

    if pygame.sprite.spritecollideany(snake2, tailGroup2):    #IF SNAKE HITS TAIL, STOP GAME
        cont = -1

    if pygame.sprite.spritecollideany(food, tailGroup1):       #IF FOOD IS CREATED ON A TAIL, MOVE THE FOOD
        food.newFood()

    if pygame.sprite.spritecollideany(food, tailGroup2):       #IF FOOD IS CREATED ON A TAIL, MOVE THE FOOD
        food.newFood()

    if pygame.sprite.collide_rect(snake1, snake2):
        cont = 3

    if snake1.rect.left < 0 or snake1.rect.right > (Width) or snake1.rect.top < 0 or snake1.rect.bottom > (Height): #IF SNAKE HEAD MOVES BEYOND BOUNDARIES OF WINDOW, DED.
        cont = 0
        tail = []
        snake = 0
        screen.fill((0,0,0))  #COVERING EVERYTHING IN BLACK

    if snake2.rect.left < 0 or snake2.rect.right > (Width) or snake2.rect.top < 0 or snake2.rect.bottom > (Height): #IF SNAKE HEAD MOVES BEYOND BOUNDARIES OF WINDOW, DED.
        cont = -1
        tail = []
        snake = 0
        screen.fill((0,0,0))  #COVERING EVERYTHING IN BLACK


    score1 = snake1.tailLength*fps-7*fps
    score2 = snake2.tailLength*fps-7*fps

    if cont == -1: #IF GREEN WINS
        dir = "R"
        dir2 = "L"
        round += 1
        totalScore1 = totalScore1 + score1
        totalScore1 = totalScore1 + fps*2
        totalScore2 = totalScore2 + score2
        myfont = pygame.font.Font("freesansbold.ttf", 50)   #DEFINING FONTS
        myfont2 = pygame.font.Font("freesansbold.ttf", 30)
        myfont3 = pygame.font.Font("freesansbold.ttf", 70)
        screen.fill((0,0,0))  #COVERING EVERYTHING IN BLACK
        if round < norounds:
            cont = 2
            for i in range(0, 5):
                printGame("ROUND " + str(round), (400, 130), (255,255,255), myfont3)
                printGame("Green Wins! (+" + str(2*fps) + ")", (400,250), (0,255,0), myfont)
                printGame("Green Score: " + str(totalScore1), (400,350), (0,255,0), myfont2)
                printGame("Red Score: " + str(totalScore2), (400,400), (255,0,0), myfont2)
                printGame("Next Round Starting in "+ str(5-i) + "..." , (400,500), (255,255,255), myfont)
                pygame.display.flip()
                pygame.time.wait(1000)
                screen.fill((0,0,0))
        else:
            printGame("Green Score: " + str(totalScore1), (400,350), (0,255,0), myfont2)
            printGame("Red Score: " + str(totalScore2), (400,400), (255,0,0), myfont2)
            printGame("Thanks for Playing!" , (400,500), (255,255,255), myfont)
            printGame("GAME OVER!", (400, 130), (255,255,255), myfont3)
            if totalScore1 < totalScore2:
                printGame("Red Wins Overall!", (400,250), (255,0,0), myfont)
            elif totalScore2 < totalScore1:
                printGame("Green Wins Overall!", (400,250), (0,255,0), myfont)
            else:
                printGame("Tie Overall!", (400,250), (255,255,255), myfont)
            pygame.display.flip()
            pygame.time.wait(10000)
            running = False


    if cont == 0:   #IF RED WINS
        dir = "R"
        dir2 = "L"
        round += 1
        totalScore1 = totalScore1 + score1
        totalScore2 = totalScore2 + fps*2
        totalScore2 = totalScore2 + score2
        myfont = pygame.font.Font("freesansbold.ttf", 50)   #DEFINING FONTS
        myfont2 = pygame.font.Font("freesansbold.ttf", 30)
        myfont3 = pygame.font.Font("freesansbold.ttf", 70)
        screen.fill((0,0,0))  #COVERING EVERYTHING IN BLACK #RELOAD THE DISPLAY :)
        if round < norounds:
            cont = 2
            for i in range(0, 5):
                printGame("ROUND " + str(round), (400, 130), (255,255,255), myfont3)
                printGame("Red Wins! (+" + str(2*fps) + ")", (400,250), (255,0,0), myfont)
                printGame("Green Score: " + str(totalScore1), (400,350), (0,255,0), myfont2)
                printGame("Red Score: " + str(totalScore2), (400,400), (255,0,0), myfont2)
                printGame("Next Round Starting in "+ str(5-i) + "..." , (400,500), (255,255,255), myfont)
                pygame.display.flip()
                pygame.time.wait(1000)
                screen.fill((0,0,0))
        else:
            printGame("Green Score: " + str(totalScore1), (400,350), (0,255,0), myfont2)
            printGame("Red Score: " + str(totalScore2), (400,400), (255,0,0), myfont2)
            printGame("Thanks for Playing!" , (400,500), (255,255,255), myfont)
            printGame("GAME OVER!", (400, 130), (255,255,255), myfont3)
            if totalScore1 < totalScore2:
                printGame("Red Wins Overall!", (400,250), (255,0,0), myfont)
            elif totalScore2 < totalScore1:
                printGame("Green Wins Overall!", (400,250), (0,255,0), myfont)
            else:
                printGame("Tie Overall!", (400,250), (255,255,255), myfont)
            pygame.display.flip()
            pygame.time.wait(10000)
            running = False

    if cont == 3:
        dir = "R"
        dir2 = "L"
        round += 1
        totalScore1 = totalScore1 + fps
        totalScore1 = totalScore1 + score1
        totalScore2 = totalScore2 + fps
        totalScore2 = totalScore2 + score2
        myfont = pygame.font.Font("freesansbold.ttf", 50)   #DEFINING FONTS
        myfont2 = pygame.font.Font("freesansbold.ttf", 30)
        myfont3 = pygame.font.Font("freesansbold.ttf", 70)
        screen.fill((0,0,0))  #COVERING EVERYTHING IN BLACK #RELOAD THE DISPLAY :)
        if round < norounds:
            cont = 2
            for i in range(0, 5):
                printGame("ROUND " + str(round), (400, 130), (255,255,255), myfont3)
                printGame("It's a TIE?! (+" + str(fps) + " Each)", (400,250), (255,255,255), myfont)
                printGame("Green Score: " + str(totalScore1), (400,350), (0,255,0), myfont2)
                printGame("Red Score: " + str(totalScore2), (400,400), (255,0,0), myfont2)
                printGame("Next Round Starting in "+ str(5-i) + "..." , (400,500), (255,255,255), myfont)
                pygame.display.flip()
                pygame.time.wait(1000)
                screen.fill((0,0,0))
        else:
            printGame("Green Score: " + str(totalScore1), (400,350), (0,255,0), myfont2)
            printGame("Red Score: " + str(totalScore2), (400,400), (255,0,0), myfont2)
            printGame("Thanks for Playing!" , (400,500), (255,255,255), myfont)
            printGame("GAME OVER!", (400, 130), (255,255,255), myfont3)
            if totalScore1 < totalScore2:
                printGame("Red Wins Overall!", (400,250), (255,0,0), myfont)
            elif totalScore2 < totalScore1:
                printGame("Green Wins Overall!", (400,250), (0,255,0), myfont)
            else:
                printGame("Tie Overall!", (400,250), (255,255,255), myfont)
            pygame.display.flip()
            pygame.time.wait(10000)
            running = False


    if cont == 1: #IF GAME IS NOT ENDED
        myfont = pygame.font.Font("freesansbold.ttf", 20)
        snake1.updatePosn()      #UPDATE POSITION OF HEAD
        snake2.updatePosn()      #UPDATE POSITION OF HEAD
        for i in range(0, snake1.tailLength):
            tail[i].updatePosn()    #UPDATE POSITION OF EACH BLOCK IN TAIL
        for i in range(0, snake2.tailLength):
            tail2[i].updatePosn()    #UPDATE POSITION OF EACH BLOCK IN TAIL
        snake1.updateDir(snake1x, snake1y) #UPDATE SPEED AND DIRECTION OF SNAKE
        for i in range(0, snake1.tailLength):
            tail[i].updateDir()     #UPDATE SPEED AND DIRECTION OF TAIL
        snake2.updateDir(snake2x, snake2y) #UPDATE SPEED AND DIRECTION OF SNAKE
        for i in range(0, snake2.tailLength):
            tail2[i].updateDir()     #UPDATE SPEED AND DIRECTION OF TAIL
        screen.fill((0,0,0))    #MAKE SCREEN BLACK
        screen.blit(leftWall.surf, leftWall.rect)
        screen.blit(rightWall.surf, rightWall.rect)
        screen.blit(topWall.surf, topWall.rect)
        screen.blit(botWall.surf, botWall.rect)
        #grid = Grid()  #SHOW GRID IF YOU LIKE, BY UNCOMMENTING THIS
        screen.blit(snake1.surf, snake1.rect) #LOAD THE SNAKE HEAD AT THE NEW POSITION OF SNAKE HEAD
        screen.blit(snake2.surf, snake2.rect) #LOAD THE SNAKE HEAD AT THE NEW POSITION OF SNAKE HEAD
        screen.blit(food.surf, food.rect) #mAKE THE FOOD SHOW ON SCREEN
        for i in range(0, snake1.tailLength):
            screen.blit(tail[i].surf, tail[i].rect)     #MAKE THE TAIL SHOW ON SCREEN
        for i in range(0, snake2.tailLength):
            screen.blit(tail2[i].surf, tail2[i].rect)     #MAKE THE TAIL SHOW ON SCREEN
        printGame("Score: " + str(totalScore1)+ "+" +str(score1), (70, 20), (0,255,0), myfont)
        printGame("Score: " + str(totalScore2)+ "+" +str(score2), ((Width-70), 20), (255,0,0), myfont)
        pygame.display.flip()   #DISPLAY!
        clock.tick(fps) #DETERMINES SPEED OF WHILE LOOP, DEPENDING ON FPS DETERMINED EARLIER

    if cont == 2:
        dir = "R"
        dir2 = "L"
        screen.fill((0,0,0))
        pygame.display.flip()
        snakeSpeed = 25 #DO NOT CHANGE THIS, CHANGE FPS TO CHANGE SPEED
        snake1x = snakeSpeed #INITIALIZED FOR SNAKE TO BE GOING RIGHT
        snake1y = 0
        snake2x = -snakeSpeed #INITIALIZED FOR SNAKE TO BE GOING RIGHT
        snake2y = 0
        cont = 1 #DECIDES IF GAME SHOULD GO ON
        snake1 = Snake(63, (0,255,0)) #MAKES THE SNAKE HEAD!
        snake2 = Snake((800-63), (255,0,0))
        food = Food() #MAKES THE FIRST FOOD AT RANDOM SPOT

        foodGroup = pygame.sprite.Group()
        foodGroup.add(food) #GROUP OF SPRITES CONSISTING OF ALL THE FOOD
        tailGroup1 = pygame.sprite.Group() #GROUP OF SPRITES CONSISTING OF ALL THE TAIL BLOCKS
        tailGroup2 = pygame.sprite.Group() #GROUP OF SPRITES CONSISTING OF ALL THE TAIL BLOCKS


        tail = [] #THE LIST THAT CONTAINS ALL THE TAIL BLOCK CLASSES - MOST IMP LIST!
        tail2 = []
        for i in range(0, snake1.tailLength): #TAILLENGTH REALLY IS JUST SNAKE LENGTH
            tail.append(Tail(i, (63-(25*i)), (((Height/2)-13)), (0,255,0))) #ADDING THE INITIAL TAILS BEFORE THE START OF THE GAME
            if i != 0:
                tailGroup1.add(tail[i])  #DONT ADD THE FIRST BLOCK OF TAIL TO COLLISION GRP. THE FIRST BLOCK OF TAIL IS BEHIND THE HEAD, IF PART OF COLLISION GRP, IMMEDIATE D

        for i in range(0, snake2.tailLength):
            tail2.append(Tail(i, ((800-63)+(25*i)), (((Height/2)-13)), (255,0,0))) #ADDING THE INITIAL TAILS BEFORE THE START OF THE GAME
            if i != 0:
                tailGroup2.add(tail2[i])  #DONT ADD THE FIRST BLOCK OF TAIL TO COLLISION GRP. THE FIRST BLOCK OF TAIL IS BEHIND THE HEAD, IF PART OF COLLISION GRP, IMMEDIATE D

        snake1.tailLength = 7 #INITIAL SNAKE LENGTH = 7
        snake2.tailLength = 7
        snake1.posList = [[25, 0], [25, 0], [25, 0], [25, 0], [25, 0], [25, 0]] #INITIAL X,Y SPEEDS LIST FOR 3 TAIL BLOCKS
        snake2.posList = [[-25, 0], [-25, 0], [-25, 0], [-25, 0], [-25, 0], [-25, 0]]
