from math import sqrt

class Node():

    def __init__(self,pos,g_coast):
        self.pos = pos
        self.g_coast = g_coast
        self.h_coast = 0
        self.f_coast = 0
        self.pai = None

    def calcCosts(self,posalvo):
        self.h_coast = sqrt(((self.pos[0]-posalvo[0])**2) + ((self.pos[1]-posalvo[1])**2))
        self.f_coast = self.g_coast + self.h_coast

    def generateChilds(self):
        top = Node((self.pos[0],self.pos[1]+1),self.g_coast+1)
        top.pai = self
        bottom = Node((self.pos[0],self.pos[1]-1),self.g_coast+1)
        bottom.pai = self
        right = Node((self.pos[0]+1,self.pos[1]),self.g_coast+1)
        right.pai = self
        left = Node((self.pos[0]-1,self.pos[1]),self.g_coast+1)
        left.pai = self
        return [top,bottom,right,left]
