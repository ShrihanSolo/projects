import time
import pygame

from pygame.locals import (
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_6,
    K_7,
    K_8,
    K_9,
    K_0,
    K_ESCAPE,
    QUIT,
    KEYDOWN,
)
pygame.init()

#Creation of floors
floors = ["0"]
i = 1
while i < 10:
    floors.append(str(i))
    i += 1

#Creation of Elevator Class
class Elevator:
    def __init__(self, number):
        self.elevNo = number
        self.elevPosn = 5
        self.elevState = "IDLE"
        self.elevList = []
        self.sortedElevList = []

    def getDist(self, floorCall):
        if self.elevState == "IDLE":
            intDist = abs(floorCall - self.elevPosn)
        elif self.elevState == "UP":
            intDist = (floorCall - self.elevPosn)
            if intDist < 0:
                intDist = (2*(int(floors[-1]) - self.elevPosn)) - intDist
        elif self.elevState == "DOWN":
            intDist = -(floorCall - self.elevPosn)
            if intDist < 0:
                intDist = (-2*(int(floors[0]) - self.elevPosn)) - intDist
        return intDist

    def dispPosn(self, location):
        posnSurface = myfont2.render("Elevator " + str(self.elevNo) + " is on Floor: "+ str(self.elevPosn), False, (255,255,255))
        posnRect = posnSurface.get_rect()
        posnRect.center = location
        screen.blit(posnSurface, posnRect)

    def dispList(self, location):
        selevList = self.elevList.copy()
        selevList.sort()
        posnSurface = myfont2.render("Calls: " + str(selevList), False, (255,255,255))
        posnRect = posnSurface.get_rect()
        posnRect.center = location
        screen.blit(posnSurface, posnRect)

    def dispState(self, location):
        posnSurface = myfont2.render("State: " + str(self.elevState), False, (255,255,255))
        posnRect = posnSurface.get_rect()
        posnRect.center = location
        screen.blit(posnSurface, posnRect)

    def reSortElevList(self):
        if len(self.elevList) > 0:
            for call in self.elevList:
                sortList = []
                sortList.append(self.getDist(call))
                sortList.append(call)
                if (sortList in self.sortedElevList) == False:
                    self.sortedElevList.append(sortList)
            self.sortedElevList.sort()
            for x in range(0, len(self.sortedElevList)):
                if x > (len(self.sortedElevList)-1):
                    continue
                for y in range(0, len(self.sortedElevList)):
                    if y > (len(self.sortedElevList)-1):
                        continue
                    if self.sortedElevList[x][1] == self.sortedElevList[y][1]:
                        if x > y:
                            self.sortedElevList.remove(self.sortedElevList[x])
                        elif y > x:
                            self.sortedElevList.remove(self.sortedElevList[y])
                        elif x == y:
                            pass

    def moveCode(self):
        if len(self.sortedElevList) > 0:
            call = self.sortedElevList[0][1]
            if (call - self.elevPosn) > 0:
                self.elevPosn += 1
                for elem in self.sortedElevList:
                    if (elem[0] == self.elevPosn) == False:
                        self.sortedElevList.remove(elem)
            elif (call - self.elevPosn) < 0:
                self.elevPosn -= 1
                for elem in self.sortedElevList:
                    if (elem[0] == self.elevPosn) == False:
                        self.sortedElevList.remove(elem)
            elif (call - self.elevPosn) == 0:
                for elem in self.sortedElevList:
                    if elem[1] == call:
                        self.sortedElevList.remove(elem)
                if self.elevPosn in niceList:
                    niceList.remove(self.elevPosn)
                if call in self.elevList:
                    self.elevList.remove(call)

    def stateCode(self):
        if len(self.sortedElevList) > 0:
            call = self.sortedElevList[0][1]
            if (call - self.elevPosn) > 0:
                self.elevState = "UP"
            elif (call - self.elevPosn) < 0:
                self.elevState = "DOWN"
        else:
            self.elevState = "IDLE"



#ADDING ELEVATOR MOVE EVENT
MOVATOR = pygame.USEREVENT + 1
pygame.time.set_timer(MOVATOR, 2000)



#Instantiation of Elevators
elev1 = Elevator(1)
elev2 = Elevator(2)
screen = pygame.display.set_mode((800,600))

#INITIALIZATION
running = True
callList = []
niceList = []
myfont = pygame.font.Font("freesansbold.ttf", 20)
myfont2 = pygame.font.Font("freesansbold.ttf", 30)
screen.fill((0,0,0))

#Running
while running == True:
    #TAKING ALL INPUTS
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_1:
                if (1 in callList) == False:
                    callList.append(1)
            if event.key == K_2:
                if (2 in callList) == False:
                    callList.append(2)
            if event.key == K_3:
                if (3 in callList) == False:
                    callList.append(3)
            if event.key == K_4:
                if (4 in callList) == False:
                    callList.append(4)
            if event.key == K_5:
                if (5 in callList) == False:
                    callList.append(5)
            if event.key == K_6:
                if (6 in callList) == False:
                    callList.append(6)
            if event.key == K_7:
                if (7 in callList) == False:
                    callList.append(7)
            if event.key == K_8:
                if (8 in callList) == False:
                    callList.append(8)
            if event.key == K_9:
                if (9 in callList) == False:
                    callList.append(9)
            if event.key == K_0:
                if (10 in callList) == False:
                    callList.append(0)
            if event.key == K_ESCAPE:
                callList = []
            for call in callList:
                if (call in niceList) == False:
                    niceList.append(call)
            niceList.sort()
        elif event.type == MOVATOR:
            elev1.moveCode()
            elev2.moveCode()

    callList.sort()
    #ELEVATOR MOTION LOGIC
    if len(callList) > 0:
        for call in callList:
            minList = [elev1.getDist(call), elev2.getDist(call)]
            if min(minList) == minList[0]:
                if (call in elev1.elevList) == False:
                    elev1.elevList.append(call)
            elif min(minList) == minList[1]:
                if (call in elev2.elevList) == False:
                    elev2.elevList.append(call)
            callList.remove(call)

    #INITIALIZING ALL ELEVATOR CALLS BEFORE MOVING
    elev1.reSortElevList()
    elev2.reSortElevList()
    elev1.stateCode()
    elev2.stateCode()

    #EXTRAFLOORFIX
    if elev1.elevState == "IDLE":
        if (elev2.elevState == "IDLE") == False:
            for call in elev2.elevList:
                if elev1.getDist(call) < elev2.getDist(call):
                    elev1.elevList.append(call)
                    elev2.elevList.remove(call)
                    elev2.sortedElevList.remove([elev2.getDist(call), call])
    if elev2.elevState == "IDLE":
        if (elev1.elevState == "IDLE") == False:
            for call in elev1.elevList:
                if elev2.getDist(call) < elev1.getDist(call):
                    elev2.elevList.append(call)
                    elev1.elevList.remove(call)
                    elev1.sortedElevList.remove([elev1.getDist(call), call])
    #PRINTING LIST OF FLOORS BEING CALLED
    callSurface = myfont.render("All Floors Being Called: " + str(niceList), False, (255,255,255))
    callRect = callSurface.get_rect()
    callRect.center = (400, 20)
    screen.fill((0,0,0))
    screen.blit(callSurface, callRect)

    #PRINTING LOCATION OF ELEVATORS
    elev1.dispPosn((400, 150))
    elev1.dispList((400, 180))
    elev1.dispState((400, 210))
    elev2.dispPosn((400, 290))
    elev2.dispList((400, 320))
    elev2.dispState((400, 350))
    pygame.display.update()
