import numpy as np
from random import randint
import math
import pygame
from Obstacle import Obstacle
from Car import Car
from Objective import Objective

class Grid():

    def __init__(self,size):
        self.size = size
        self.grid = np.zeros((size,size))
        self.stones = []
        self.car = None
        self.objective = None

    def generateObstacles(self,percent,sizeOfQuad):
        nobstacles = math.pow(self.size,2)*(percent/100.0)
        while nobstacles>0:
            posx = randint(0,self.size-1)
            posy = randint(0,self.size-1)
            if(self.grid[posx,posy]!=1):
                self.grid[posx,posy]=1
                nobstacles-=1
                stone = Obstacle(sizeOfQuad)
                stone.pos = (sizeOfQuad[0]*posx,sizeOfQuad[1]*posy)
                self.stones.append(stone)

    def createCar(self,sizeOfQuad):
        car = Car(sizeOfQuad)
        spawned = False
        while spawned==False:
            posx = randint(0,self.size-1)
            posy = randint(0,self.size-1)
            if(self.grid[posx,posy]!=1):
                self.grid[posx,posy] = 2
                car.pos = (posx,posy)
                spawned = True
                self.car = car
        return self.car.pos

    def createObjective(self,sizeOfQuad):
        objective = Objective(sizeOfQuad)
        spawned = False
        while spawned==False:
            posx = randint(0,self.size-1)
            posy = randint(0,self.size-1)
            if(self.grid[posx,posy]!=1 and self.grid[posx,posy]!=2):
                self.grid[posx,posy] = 3
                objective.pos = (posx,posy)
                spawned = True
                self.objective = objective
        return self.objective.pos

    def drawGrid(self,surface,screenSize,sizeOfQuad):
        spacey = screenSize[1]/self.size
        spacex = screenSize[0]/self.size
        for i in range(self.size):
            pygame.draw.line(surface, pygame.Color("red") , (0,i*spacey), (screenSize[0],i*spacey), 1)
            pygame.draw.line(surface, pygame.Color("red") , (i*spacex,0), (i*spacex,screenSize[1]), 1)
        for i in range(len(self.stones)):
            self.stones[i].drawStone(surface)
        self.car.drawCar(surface,sizeOfQuad)
        self.objective.drawObjective(surface,sizeOfQuad)

    def drawPath(self,path,surface,screenSize):
        spacey = screenSize[1]/self.size
        spacex = screenSize[0]/self.size
        for i in range(len(path)-1):
            pygame.draw.line(surface, pygame.Color("blue") , (path[i][0]*spacex,path[i][1]*spacey), (path[i+1][0]*spacex,path[i+1][1]*spacey), 3)
