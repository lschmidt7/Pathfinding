import pygame
from random import randint

class Obstacle():

    def __init__(self,(sizex,sizey)):
        self.pos = (0,0)
        obstacles = ['stone.png','tree.png','house.png']
        spritename = obstacles[randint(0,2)]
        self.sprite = pygame.image.load(spritename).convert_alpha()
        self.scale(sizex,sizey)

    def drawStone(self,screen):
        screen.blit(self.sprite,self.pos)

    def scale(self,sx,sy):
        self.sprite = pygame.transform.scale(self.sprite, (sx,sy))
