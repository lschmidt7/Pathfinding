from math import hypot
import pygame

class AStar():

    def __init__(self,start,finish,grid,size):
        self.size = size
        self.start = start
        self.finish = finish
        self.opened = []
        self.closed = []
        self.path = []
        self.grid = grid
        self.opened.append(start)
        print(start)

    def run(self):
        while(self.finish not in self.closed):
            if(len(self.opened)>0):
                m = self.menor()
                self.path.append(m)
                self.vizinhos(m)
        return self.path

    def distance(self,p1,p2):
        return hypot(p1[0]-p2[0],p1[1]-p2[1])

    def menor(self):
        menor = self.opened[0]
        menorDist = self.distance(menor,self.finish)
        for x in self.opened:
            menorDistAux = self.distance(x,self.finish)
            if(menorDistAux<menorDist):
                menorDist = menorDistAux
                menor=x
        self.opened.remove(menor)
        self.closed.append(menor)
        return menor

    def vizinhos(self,ponto):
        self.opened=[]
        top = (ponto[0],ponto[1]+1)
        bottom = (ponto[0],ponto[1]-1)
        right = (ponto[0]+1,ponto[1])
        left = (ponto[0]-1,ponto[1])
        if(self.valida(top) and self.grid[top[0],top[1]]!=1 and top not in self.closed):
            self.opened.append(top)
        if(self.valida(bottom) and self.grid[bottom[0],bottom[1]]!=1 and bottom not in self.closed):
            self.opened.append(bottom)
        if(self.valida(left) and self.grid[left[0],left[1]]!=1 and left not in self.closed):
            self.opened.append(left)
        if(self.valida(right) and self.grid[right[0],right[1]]!=1 and right not in self.closed):
            self.opened.append(right)

    def valida(self,ponto):
        if(ponto[0]<self.size and ponto[0]>=0 and ponto[1]<self.size and ponto[1]>=0):
            return True
        return False

    def drawPath(self,surface,screenSize):
        spacey = screenSize[1]/self.size
        spacex = screenSize[0]/self.size
        if(len(self.path)>1):
            for i in range(len(self.path)-1):
                pygame.draw.line(surface, pygame.Color("yellow") , (self.path[i][0]*spacex,self.path[i][1]*spacey), (self.path[i+1][0]*spacex,self.path[i+1][1]*spacey), 4)
