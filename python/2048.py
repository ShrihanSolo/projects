import random
import pygame
import time
import math

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

class Grid(pygame.sprite.Sprite):
    def __init__(self):
        super(Grid, self).__init__()
        self.surf = pygame.Surface((600,600))
        self.surf.fill((120,120,120))
        self.rect = self.surf.get_rect(center = (((Width/2), (Height/2))))

    def gridUpdate(self):
        screen.blit(grid.surf, grid.rect)
        for x in range(0, 4):
            for y in range(0, 4):
                boxPosn = (10+150*x, 10+150*y)
                boxsize = 130
                noPosn = (110+150*x + (boxsize/2), 10+150*y + (boxsize/2))
                for i in nums:
                    if board[y][x] == i[0]:
                        pygame.draw.rect(self.surf, i[1], (boxPosn, (boxsize, boxsize)))
                        if i[0] != 0:
                            printGame(str(i[0]), noPosn)

def printGame(text, location, color = (0,0,0), font = myfont):
    lossSurface = font.render(text, False, color) #USE FONT TO DISPLAY YOU LOSE, CUS OFC U DID
    lossRect = lossSurface.get_rect()
    lossRect.center = location    #DETERMINING WHERE THE FONT WILL GO
    screen.blit(lossSurface, lossRect)

def spawnFn():
    global board
    global cont
    zerochk = []
    for i in board:
        for j in i:
            zerochk.append(j)
    if 0 in zerochk:
        if cont == 1:
            noX = random.randint(0,3)
            noY = random.randint(0,3)
            if board[noY][noX] == 0:
                board[noY][noX] = 2
            else:
                spawnFn()

def rotateFn():
    global board
    rotbd = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
    for rad in range(0,2):
        for lth in range(rad, (4-rad)):
            rotbd[lth][rad] = board[rad][(3-lth)]
            rotbd[rad][lth] = board[lth][(3-rad)]
            rotbd[lth][3-rad] = board[3-rad][3-lth]
            rotbd[3-rad][lth] = board[lth][rad]
    board = rotbd.copy()

def gravFn(row):
    j = 0
    while j < 4:
        for i in range(0,3):
            if row[i] == 0 and row[i+1] != 0:
                row[i] = row[i+1]
                row[i+1] = 0
        j += 1

def mergeFn(row):
    for i in range(0,3):
        if row[i] == row[i+1]:
            row[i] = (row[i]+row[i+1])
            row[i+1] = 0

def moveFn(no = 0, dshun = 0):
    global board
    global cont
    global mvd
    global pvBrd
    for row in board:
        gravFn(row)
        mergeFn(row)
        gravFn(row)
    if no == 0:
        if pvBrd != board:
            OverCheck()
            if cont == 1:
                spawnFn()

def printBoard():
    print("")
    for i in board:
        print(i)

def mvLeft(no = 0):
    global board
    global pvBrd
    rotateFn()
    rotateFn()
    rotateFn()
    rotateFn()
    if no == 0:
        pvBrd = list(board)
    moveFn(no, mvLeft)

def mvRight(no = 0):
    global board
    global pvBrd
    rotateFn()
    rotateFn()
    if no == 0:
        pvBrd = list(board)
    moveFn(no, mvRight)
    rotateFn()
    rotateFn()

def mvUp(no = 0):
    global board
    global pvBrd
    rotateFn()
    if no == 0:
        pvBrd = list(board)
    moveFn(no, mvUp)
    rotateFn()
    rotateFn()
    rotateFn()

def mvDown(no = 0):
    global board
    global pvBrd
    rotateFn()
    rotateFn()
    rotateFn()
    if no == 0:
        pvBrd = list(board)
    moveFn(no, mvDown)
    rotateFn()

def OverCheck():
    global board
    global cont
    x = 0
    cpbrd = list(board)
    mvUp(1)
    if board == cpbrd:
        x += 1
    board = list(cpbrd)
    mvDown(1)
    if board == cpbrd:
        x += 1
    board = list(cpbrd)
    mvRight(1)
    if board == cpbrd:
        x += 1
    board = list(cpbrd)
    mvLeft(1)
    if board == cpbrd:
        x += 1
    board = list(cpbrd)
    if x == 4:
        cont = 0



Width = 800
Height = 600
cont = 1
nums = [[0, (0,0,0), 0],[2, (255,215,160), 0],[4, (255,180,140), 0],[8, (255,160,180), 0],[16, (219,112,147), 0],[32, (210,0,210), 0],[64,(186,85,211), 1],[128, (148,0,211), 1], [256, (138,43,226), 1],[512, (75,0,130), 1],[1024, (90, 0, 255), 1],[2048, (0,0,128), 1]]
board = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

TIMEDMOVE = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEDMOVE, 100)

spawnFn()
spawnFn()

screen = pygame.display.set_mode((Width, Height))#, pygame.FULLSCREEN) #MAKE SCREEN IN PYGAME
screen.fill((255,255,255))
grid = Grid()

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == QUIT: #SO THAT THE X BUTTON WORKS TO CLOSE THE GAME OTHERWISE IT WILL RUN FOREVER. THAT IS BAD.
            running = False
        if event.type == KEYDOWN:  #IF A BUTTON IS PRESSED:
            if event.key == K_ESCAPE:
                running = False     #RUNNING FALSE KILLS THE GAME IMMEDIATELY, SO ESC ALSO KILLS THE GAME
            if event.key == K_UP:
                mvUp()
                OverCheck()
            elif event.key == K_DOWN:
                mvDown()
                OverCheck()
            elif event.key == K_RIGHT:
                mvRight()
                OverCheck()
            elif event.key == K_LEFT:
                mvLeft()
                OverCheck()
    #for i in range(0,4):
        #printGame(str(board[i]), ((Width/2), (100 + 100*i)))
    grid.gridUpdate()
    pygame.display.flip()
    if cont == 0:
        screen.fill((255,255,255))
        printGame("Game Over!", (400, 300))
        pygame.display.flip()
        time.sleep(10)
        running = False
    screen.fill((255,255,255))
