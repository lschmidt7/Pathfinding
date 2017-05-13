import pygame

class Obstacle():

    def __init__(self,(sizex,sizey)):
        self.pos = (0,0)
        self.sprite = pygame.image.load('stone.png').convert_alpha()
        self.scale(sizex,sizey)

    def drawStone(self,screen):
        screen.blit(self.sprite,self.pos)

    def scale(self,sx,sy):
        self.sprite = pygame.transform.scale(self.sprite, (sx,sy))
