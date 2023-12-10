#lyvis
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
)
pygame.init()

#CREATING SNAKE'S HEAD SPRITE CLASS
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super(Snake, self).__init__()   #INHERITING FROM SPRITE CLASS IN PYGAME MODULE
        self.surf = pygame.Surface((25,25))    #CREATING SHAPE HEAD OF SNAKE
        self.surf.fill((0,255,0))   #COLORING THE HEAD
        self.x = 0  #INITIALIZING X,Y SPEED VARIABLES
        self.y = 0
        self.rect = self.surf.get_rect(center = (snakePosn, (Height/2 - 13))) #INITIAL lOCATION OF HEAD

    def updateDir(self, X, Y): #FUNCTION TO CHANGE SNAKE'S DIRECTION (X,Y SPEED)
        self.x = X
        self.y = Y
        posList.append([X, Y])
        if len(posList) > tailLength:
            posList.pop(0)

    def updatePosn(self):
        self.rect.move_ip(self.x, self.y)   #FUNCTION TO CHANGE X,Y POSITION BASED ON X,Y SPEED



class Tail(pygame.sprite.Sprite):
    def __init__(self, lengthno, posnx, posny):
        super(Tail, self).__init__() #INHERITING
        self.surf = pygame.Surface((25,25)) #CREATING A TAIL BLOCK
        self.surf.fill((0,255,0))
        self.num = lengthno #THE NUMBER OF THE BLOCK, AKA, WHICH BLOCK OF TAIL IS IT?
        self.posnx = posnx  # X,Y POSITION TO CREATE THE BLOCK
        self.posny = posny
        self.x = 0
        self.y = 0
        self.rect = self.surf.get_rect(center = ((self.posnx), (self.posny))) #CREATING THE BLOCK AT X,Y POSN

    def updatePosn(self):
        self.rect.move_ip(self.x, self.y) #MOVE TAILBLOCK ACC TO X,Y SPEED

    def updateDir(self):
        self.x = posList[-self.num-1][0] #MOVE TAIL BLOCK ACC TO THE SPEED OF THE PREVIOUS BLOCK IN THE SEQUENCE DURING THE TURN BEFORE IT (SO THAT IT FOLLOWS THE SAME PATH)
        self.y = posList[-self.num-1][1]



class Grid(pygame.sprite.Sprite): #MAKING ONE USELESS GRID...IF YOU'RE NOT USING IT, IGNORE THIS CLASS
    def __init__(self):
        super(Grid, self).__init__()
        for CboxNo in range(0, 24):
            boxPosnY = CboxNo*25 + 12
            for RboxNo in range(0, 32):
                boxPosnX = RboxNo*(25) + 13
                self.surf2 = pygame.Surface((23,23))
                self.surf2.fill((0,0,0))
                self.rect2 = self.surf2.get_rect(
                    center = (
                        boxPosnX,
                        boxPosnY,
                    )
                )
                screen.blit(self.surf2, self.rect2)

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super(Food, self).__init__()
        self.surf = pygame.Surface((19,19)) #TINY RED FOOD BLOCK :)
        self.surf.fill((255,0,0))  #RED COLOR FOOD BLOCK!
        self.x = random.randint(1, 30)*25 + 13 #RANDOM POSITION FOR BLOCK. FIRST RANDOM BLOCK ON GRID, AND THEN 12.5 IS ADDED TO PUT IT IN THE CENTER OF BOTH
        self.y = random.randint(1, 22)*25 + 12
        self.rect = self.surf.get_rect(center = ((self.x),(self.y)))    #CENTERING BLOCK ON THE RANDOM COORDS

    def newFood(self):
        self.x = random.randint(1, 30)*25 + 13    #MAKING A NEW RANDOM COORDS
        self.y = random.randint(1, 22)*25 + 12
        self.rect = self.surf.get_rect(center = ((self.x),(self.y))) #CENTERING NEW FOOD ON THIS SPOT

class Wall(pygame.sprite.Sprite):
    def __init__(self, shape, location):
        super(Wall, self).__init__()
        self.surf = pygame.Surface(shape)
        if wall.lower() == "y":
            self.surf.fill((255,255,255))
        if wall.lower() == "n":
            self.surf.fill((0,0,0))
        (self.x, self.y) = location
        self.rect = self.surf.get_rect(center = (location))


#INITIALIZATION OF VARIABLES
running = True
Width = 800 #OF SCREEN
Height = 600
snakeSpeed = 25 #DO NOT CHANGE THIS, CHANGE FPS TO CHANGE SPEED
snakex = snakeSpeed #INITIALIZED FOR SNAKE TO BE GOING RIGHT
snakey = 0
snakePosn = 88 #INITIAL SNAKE POSN
tailLength = 4 #INITIAL SNAKE LENGTH = 4
posList = [[25, 0], [25, 0], [25, 0]] #INITIAL X,Y SPEEDS LIST FOR 3 TAIL BLOCKS
cont = 1 #DECIDES IF GAME SHOULD GO ON
clock = pygame.time.Clock()
fps = int(input("Enter speed (From 10-50): "))  #UK WHAT THIS IS - FPS DETERMINES HOW MANY TIMES THE UPCOMING WHILE LOOP RUNS PER SECOND
wall = input("Would you like a wall? (Y/N): ")
dir = "R"

screen = pygame.display.set_mode((Width, Height), pygame.FULLSCREEN) #MAKE SCREEN IN PYGAME

TIMEDMOVE = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEDMOVE, 1000//fps)

snake = Snake() #MAKES THE SNAKE HEAD!
food = Food() #MAKES THE FIRST FOOD AT RANDOM SPOT

if wall.lower() == "y":
    leftWall = Wall((25,Height), (13, (Height/2)))
    rightWall = Wall((25,Height), (Width-12, (Height/2)))
    topWall = Wall((Width,25), ((Width/2), 12))
    botWall = Wall((Width,25), ((Width/2), Height-13))

if wall.lower() == "n":
    leftWall = Wall((25,Height), (-12, (Height/2)))
    rightWall = Wall((25,Height), (Width+13, (Height/2)))
    topWall = Wall((Width,25), ((Width/2), -13))
    botWall = Wall((Width,25), ((Width/2), Height+12))

wallGroup = pygame.sprite.Group()
wallGroup.add(leftWall)
wallGroup.add(rightWall)
wallGroup.add(topWall)
wallGroup.add(botWall)
foodGroup = pygame.sprite.Group()
foodGroup.add(food) #GROUP OF SPRITES CONSISTING OF ALL THE FOOD
tailGroup = pygame.sprite.Group() #GROUP OF SPRITES CONSISTING OF ALL THE TAIL BLOCKS

tail = [] #THE LIST THAT CONTAINS ALL THE TAIL BLOCK CLASSES - MOST IMP LIST!
for i in range(0, tailLength): #TAILLENGTH REALLY IS JUST SNAKE LENGTH
    tail.append(Tail(i, (snakePosn-(25*(i))), ((Height/2)-13))) #ADDING THE INITIAL TAILS BEFORE THE START OF THE GAME
    if (i == 0) == False:
        tailGroup.add(tail[i])  #DONT ADD THE FIRST BLOCK OF TAIL TO COLLISION GRP. THE FIRST BLOCK OF TAIL IS BEHIND THE HEAD, IF PART OF COLLISION GRP, IMMEDIATE D



while running == True: #WHILE LOOP!
    if snake.x != tail[0].x:
        snake.x = tail[0].x
    if snake.y != tail[0].y:
        snake.y = tail[0].y
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
        if event.type == TIMEDMOVE:
            if dir == "U":
                if (snakex, snakey) != (0, snakeSpeed):     #IF THE SNAKE IS GOING DOWN, UP BUTTON DOESNT WORK, SIMILAR FOR REST
                    snakex = 0                              #CHANGE X,Y SPEED OF SNAKE!
                    snakey = -snakeSpeed
            if dir == "D":
                if (snakex, snakey) != (0, -snakeSpeed):
                    snakex = 0
                    snakey = snakeSpeed
            if dir == "R":
                if (snakex, snakey) != (-snakeSpeed, 0):
                    snakex = snakeSpeed
                    snakey = 0
            if dir == "L":
                if (snakex, snakey) != (snakeSpeed, 0):
                    snakex = -snakeSpeed
                    snakey = 0


    if pygame.sprite.spritecollideany(tail[0], foodGroup): #IF SNAKE COLLIDES WITH FOOD, THEN DO THIS
        food.newFood()  #CREATES A NEW FOOD
        tailLength += 1     #SNAKE BECOMES BIGGER DUE TO FOOD, ALSO DEFINES X,Y SPEED OF NEW TAIL BLOCK
        tail.append(Tail((tailLength-1), ((tail[-1].rect.centerx)), ((tail[-1].rect.centery))))     #PUT A NEW TAIL BLOCK AT THE PREV POSN OF THE BLOCK AT THE END OF TAIL
        tailGroup.add(tail[-1]) #ADD TAIL TO COLLISION GROUP

    if pygame.sprite.spritecollideany(tail[0], tailGroup):    #IF SNAKE HITS TAIL, STOP GAME
        cont = 0

    if pygame.sprite.spritecollideany(food, tailGroup):       #IF FOOD IS CREATED ON A TAIL, MOVE THE FOOD
        food.newFood()

    if wall.lower() == "n":
        scoreLoc = (65, 30)
        if pygame.sprite.collide_rect(snake, leftWall):
            if (snakex, snakey) == (-snakeSpeed, 0):
                snake.rect.move_ip((Width+25), 0)
            elif (snakex, snakey) != (snakeSpeed, 0):
                snake.rect.move_ip((Width), 0)
        if pygame.sprite.collide_rect(snake, rightWall):
            if (snakex, snakey) == (snakeSpeed, 0):
                snake.rect.move_ip((-Width-25), 0)
            elif (snakex, snakey) != (-snakeSpeed, 0):
                snake.rect.move_ip((-Width), 0)
        if pygame.sprite.collide_rect(snake, topWall):
            if (snakex, snakey) == (0, -snakeSpeed):
                snake.rect.move_ip(0, Height+25)
            elif (snakex, snakey) != (0, snakeSpeed):
                snake.rect.move_ip(0, Height)
        if pygame.sprite.collide_rect(snake, botWall):
            if (snakex, snakey) == (0, snakeSpeed):
                snake.rect.move_ip(0, -Height-25)
            elif (snakex, snakey) != (0, -snakeSpeed):
                snake.rect.move_ip(0, -Height)

        for i in range(0, tailLength):
            if (tail[i].x, tail[i].y) == (-snakeSpeed, 0):
                if pygame.sprite.collide_rect(tail[i], leftWall):
                    tail[i].rect.move_ip((Width+25), 0)
            elif (tail[i].x, tail[i].y) != (snakeSpeed, 0):
                if pygame.sprite.collide_rect(tail[i], leftWall):
                    tail[i].rect.move_ip((Width), 0)
        for i in range(0, tailLength):
            if (tail[i].x, tail[i].y) == (snakeSpeed, 0):
                if pygame.sprite.collide_rect(tail[i], rightWall):
                    tail[i].rect.move_ip(-Width-25, 0)
            elif (tail[i].x, tail[i].y) != (-snakeSpeed, 0):
                if pygame.sprite.collide_rect(tail[i], rightWall):
                    tail[i].rect.move_ip((-Width), 0)
        for i in range(0, tailLength):
            if (tail[i].x, tail[i].y) == (0, -snakeSpeed):
                if pygame.sprite.collide_rect(tail[i], topWall):
                    tail[i].rect.move_ip(0, Height+25)
            elif (tail[i].x, tail[i].y) != (0, snakeSpeed):
                if pygame.sprite.collide_rect(tail[i], topWall):
                    tail[i].rect.move_ip(0, Height)
        for i in range(0, tailLength):
            if (tail[i].x, tail[i].y) == (0, snakeSpeed):
                if pygame.sprite.collide_rect(tail[i], botWall):
                    tail[i].rect.move_ip(0, -Height-25)
            elif (tail[i].x, tail[i].y) != (0, -snakeSpeed):
                if pygame.sprite.collide_rect(tail[i], botWall):
                    tail[i].rect.move_ip(0, -Height)

    elif wall.lower() == "y":
        scoreLoc = (77.5, 42.5)
        if pygame.sprite.spritecollideany(snake, wallGroup):
            cont = 0
    else:
        print("Enter valid input.")
        running = False

    if cont == 0:   #IF GAME ENDS
        myfont = pygame.font.Font("freesansbold.ttf", 50)   #DEFINING FONTS
        myfont2 = pygame.font.Font("freesansbold.ttf", 30)
        lossSurface =  myfont.render("You Lose!", False, (255,255,255)) #USE FONT TO DISPLAY YOU LOSE, CUS OFC U DID
        scoreSurface = myfont2.render("Score: " + str(tailLength*fps-4*fps), False, (255,255,255))  #USE FONT TO DISPLAY SCORE
        lossRect = lossSurface.get_rect()
        lossRect.center = (400, 200)    #DETERMINING WHERE THE FONT WILL GO
        scoreRect = scoreSurface.get_rect()
        scoreRect.center = (400, 300)
        screen.fill((0,0,0))  #COVERING EVERYTHING IN BLACK
        screen.blit(scoreSurface, scoreRect) #PRINTING SCORE ON THE SCREEN ON TOP OF BLACK
        screen.blit(lossSurface, lossRect) #PRINTING YOU LOSE ON THE SCREEN ON TOP OF BLACK
        pygame.display.flip() #RELOAD THE DISPLAY :)

    elif cont == 1: #IF GAME IS NOT ENDED
        myfont = pygame.font.Font("freesansbold.ttf", 20)
        scoreSurface = myfont.render("Score: " + str(tailLength*fps-4*fps), False, (255,255,255)) #CREATING SCORE THING
        scoreRect = scoreSurface.get_rect()
        scoreRect.center = scoreLoc # MAKING SCORE GO ON TOP LEFT
        backSurface = pygame.Surface((pygame.Surface.get_width(scoreSurface)+5, pygame.Surface.get_height(scoreSurface)+5))
        backSurface.fill((0,255,0))
        backRect = backSurface.get_rect() #BACKGROUND TO THE SCORE, IN CASE GRID IS BEING USED
        backRect.center = scoreLoc
        snake.updatePosn()      #UPDATE POSITION OF HEAD
        for i in range(0, tailLength):
            tail[i].updatePosn()    #UPDATE POSITION OF EACH BLOCK IN TAIL
        snake.updateDir(snakex, snakey) #UPDATE SPEED AND DIRECTION OF SNAKE
        for i in range(0, tailLength):
            tail[i].updateDir()     #UPDATE SPEED AND DIRECTION OF TAIL
        screen.fill((0,0,0))    #MAKE SCREEN BLACK
        #grid = Grid()  #SHOW GRID IF YOU LIKE, BY UNCOMMENTING THIS
        screen.blit(leftWall.surf, leftWall.rect)
        screen.blit(rightWall.surf, rightWall.rect)
        screen.blit(topWall.surf, topWall.rect)
        screen.blit(botWall.surf, botWall.rect)
        #screen.blit(snake.surf, snake.rect) #LOAD THE SNAKE HEAD AT THE NEW POSITION OF SNAKE HEAD
        screen.blit(food.surf, food.rect) #mAKE THE FOOD SHOW ON SCREEN
        for i in range(0, tailLength):
            screen.blit(tail[i].surf, tail[i].rect)     #MAKE THE TAIL SHOW ON SCREEN
        #screen.blit(backSurface, backRect)     #IF YOU ARE USING GRID, AND WANT BACKGROUND TO THE SCORE
        screen.blit(scoreSurface, scoreRect)    #PRINTING THE SCORE ON TOP LEFT
        pygame.display.flip()   #DISPLAY!
        clock.tick(fps) #DETERMINES SPEED OF WHILE LOOP, DEPENDING ON FPS DETERMINED EARLIER
