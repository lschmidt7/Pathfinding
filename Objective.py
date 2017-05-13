import pygame

class Objective():

    def __init__(self,(sizex,sizey)):
        self.pos = (0,0)
        self.sprite = pygame.image.load('flag.png').convert_alpha()
        self.scale(sizex,sizey)

    def drawObjective(self,screen):
        screen.blit(self.sprite,self.pos)

    def scale(self,sx,sy):
        self.sprite = pygame.transform.scale(self.sprite, (sx,sy))

    def rotate(self,angle):
        self.sprite = pygame.transform.rotate(self.sprite,angle)
