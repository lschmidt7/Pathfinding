import pygame
from pygame.locals import *
from sys import exit
from Grid import Grid
from Screen import Screen
from Obstacle import Obstacle

size = 30

pygame.init()

s = Screen(1024,700)

sizeOfQuad = (s.width/size,s.height/size)

s.display = pygame.display.set_mode(s.getSize(),0,32)


pygame.display.set_caption("Pathfinding A*")
s.display.fill((255,255,255))
pygame.display.flip()
grid = Grid(size)
grid.generateObstacles(10,sizeOfQuad)
grid.createCar(sizeOfQuad)
grid.createObjective(sizeOfQuad)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    s.display.blit(pygame.Surface(s.getSize()), (0,0))
    s.display.fill((255,255,255))
    grid.drawGrid(s.display,s.getSize())
    pygame.display.update()
