import pygame

class Car():

    def __init__(self,(sizex,sizey)):
        self.pos = (0,0)
        self.sprite = pygame.image.load('car.png').convert_alpha()
        self.scale(sizex,sizey)

    def drawCar(self,screen,sizeOfQuad):
        screen.blit(self.sprite,(self.pos[0]*sizeOfQuad[0],self.pos[1]*sizeOfQuad[1]))

    def scale(self,sx,sy):
        self.sprite = pygame.transform.scale(self.sprite, (sx,sy))

    def rotate(self,angle):
        self.sprite = pygame.transform.rotate(self.sprite,angle)
