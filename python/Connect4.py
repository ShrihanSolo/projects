#lyvis
#IMPORTING NECESSARY MODULES
import pygame
import time
import random
import numpy

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

class Grid(pygame.sprite.Sprite): #MAKING ONE USELESS GRID...IF YOU'RE NOT USING IT, IGNORE THIS CLASS
    def __init__(self):
        super(Grid, self).__init__()
        self.surf = pygame.Surface((700,600))
        self.surf.fill((212,175,55))
        self.rect = self.surf.get_rect(center = (((Width/2), (Height/2))))

    def gridUpdate(self):
        for x in range(0, 7):
            for y in range(0, 6):
                circPosnForm = (50+100*x, 50+100*y)
                if grid[x][y] == 1:
                    pygame.draw.circle(self.surf, (0,0,0), circPosnForm, rad)
                elif grid[x][y] == 2:
                    pygame.draw.circle(self.surf, (255, 0, 0), circPosnForm, rad)
                elif grid[x][y] == 0:
                    pygame.draw.circle(self.surf, (255, 255, 255), circPosnForm, rad)
                elif grid[x][y] == 3:
                    if blk == 0:
                        pygame.draw.circle(self.surf, (0, 0, 0), circPosnForm, rad)
                    if blk == 1:
                        pygame.draw.circle(self.surf, (0, 255, 0), circPosnForm, rad)
                elif grid[x][y] == 4:
                    if blk == 0:
                        pygame.draw.circle(self.surf, (255, 0, 0), circPosnForm, rad)
                    if blk == 1:
                        pygame.draw.circle(self.surf, (0, 255, 0), circPosnForm, rad)


def printGame(text, location, color, font):
    lossSurface = font.render(text, False, color) #USE FONT TO DISPLAY YOU LOSE, CUS OFC U DID
    lossRect = lossSurface.get_rect()
    lossRect.center = location    #DETERMINING WHERE THE FONT WILL GO
    screen.blit(lossSurface, lossRect)

#INITIALIZATION OF VARIABLES
running = True
Width = 900 #OF SCREEN
Height = 600
cont = 1 #DECIDES IF GAME SHOULD GO ON
clock = pygame.time.Clock()
fps = 30
rad = 40
biz = 100
turn = 1
cont = 2
blk = 1

grid = []
for i in range(0,7):
    row = []
    for i in range(0,6):
        row.append(0)
    grid.append(row)
#grid[row(top)][col[left]]

screen = pygame.display.set_mode((Width, Height), pygame.FULLSCREEN) #MAKE SCREEN IN PYGAME
board = Grid()

while running == True: #WHILE LOOP!
    for event in pygame.event.get():
        if event.type == QUIT: #SO THAT THE X BUTTON WORKS TO CLOSE THE GAME OTHERWISE IT WILL RUN FOREVER. THAT IS BAD.
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  #IF A BUTTON IS PRESSED:
            mousePosnX, mousePosnY = pygame.mouse.get_pos()
            if cont == 2:
                for x in range(1, 8):
                    if x*biz < mousePosnX < (x+1)*biz:
                        if turn == 1:
                            turn = 2
                            grid[x-1].pop(0)
                            grid[x-1].insert(grid[x-1].count(0), 1)
                        elif turn == 2:
                            turn = 1
                            grid[x-1].pop(0)
                            grid[x-1].insert(grid[x-1].count(0), 2)
                for x in range(0,7):
                    for y in range(0,6):
                        if grid[x][y] == 1:
                            if (x+3) < 7:
                                trip = []
                                for m in range(1,4):
                                    trip.append(grid[x+m][y])
                                if trip == [1,1,1]:
                                    cont = 0
                                    for m in range(0,4):
                                        grid[x+m][y] = 3
                            if (x+3) < 7:
                                if (y+3) < 6:
                                    trip = []
                                    for m in range(1,4):
                                        trip.append(grid[x+m][y+m])
                                    if trip == [1,1,1]:
                                        cont = 0
                                        for m in range(0,4):
                                            grid[x+m][y+m] = 3
                                if (y-3) > -1:
                                    trip = []
                                    for m in range(1,4):
                                        trip.append(grid[x+m][y-m])
                                    if trip == [1,1,1]:
                                        cont = 0
                                        for m in range(0,4):
                                            grid[x+m][y-m] = 3
                            if (y+3) < 6:
                                trip = []
                                for m in range(1,4):
                                    trip.append(grid[x][y+m])
                                if trip == [1,1,1]:
                                    cont = 0
                                    for m in range(0,4):
                                        grid[x][y+m] = 3
                        if grid[x][y] == 2:
                            if (x+3) < 7:
                                trip = []
                                for m in range(1,4):
                                    trip.append(grid[x+m][y])
                                if trip == [2,2,2]:
                                    cont = 1
                                    for m in range(0,4):
                                        grid[x+m][y] = 4
                            if (x+3) < 7:
                                if (y+3) < 6:
                                    trip = []
                                    for m in range(1,4):
                                        trip.append(grid[x+m][y+m])
                                    if trip == [2,2,2]:
                                        cont = 1
                                        for m in range(0,4):
                                            grid[x+m][y+m] = 4
                                if (y-3) > -1:
                                    trip = []
                                    for m in range(1,4):
                                        trip.append(grid[x+m][y-m])
                                    if trip == [2,2,2]:
                                        cont = 1
                                        for m in range(0,4):
                                            grid[x+m][y-m] = 4
                            if (y+3) < 6:
                                trip = []
                                for m in range(1,4):
                                    trip.append(grid[x][y+m])
                                if trip == [2,2,2]:
                                    cont = 1
                                    for m in range(0,4):
                                        grid[x][y+m] = 4
    if cont == 2:
        screen.fill((255,255,255))
        myfont = pygame.font.Font("freesansbold.ttf", 100)
        myfont2 = pygame.font.Font("freesansbold.ttf", 70)
        screen.blit(board.surf, board.rect)
        board.gridUpdate()
    if cont == 0:
        screen.fill((255,255,255))
        myfont = pygame.font.Font("freesansbold.ttf", 100)
        myfont2 = pygame.font.Font("freesansbold.ttf", 70)
        screen.blit(board.surf, board.rect)
        board.gridUpdate()
        stime = pygame.time.get_ticks()
        while pygame.time.get_ticks() - stime < 5000:
            num = (pygame.time.get_ticks() - stime)
            if numpy.mod((num // 500), 2) == 0:
                blk = 1
            elif  numpy.mod((num // 500), 2) == 1:
                blk = 0
            board.gridUpdate()
            screen.blit(board.surf, board.rect)
            pygame.display.flip()   #DISPLAY!
        screen.fill((255,255,255))
        printGame("Black Wins!", ((Width/2), (Height/2 - 100)), (0,0,0), myfont)
        printGame("Thanks For Playing!", ((Width/2), (Height/2 + 100)), (0,0,0), myfont2)
        pygame.display.flip()
        cont = 3
    if cont == 1:
        myfont = pygame.font.Font("freesansbold.ttf", 100)
        myfont2 = pygame.font.Font("freesansbold.ttf", 70)
        screen.blit(board.surf, board.rect)
        board.gridUpdate()
        stime = pygame.time.get_ticks()
        while pygame.time.get_ticks() - stime < 5000:
            num = (pygame.time.get_ticks() - stime)
            if numpy.mod((num // 500), 2) == 0:
                blk = 1
            elif  numpy.mod((num // 500), 2) == 1:
                blk = 0
            board.gridUpdate()
            screen.blit(board.surf, board.rect)
            pygame.display.flip()   #DISPLAY!
        screen.fill((255,255,255))
        printGame("Red Wins!", ((Width/2), (Height/2 - 100)), (255,0,0), myfont)
        printGame("Thanks For Playing!", ((Width/2), (Height/2 + 100)), (0,0,0), myfont2)
        pygame.display.flip()
        cont = 3
    pygame.display.flip()   #DISPLAY!
    clock.tick(fps) #DETERMINES SPEED OF WHILE LOOP, DEPENDING ON FPS DETERMINED EARLIER
