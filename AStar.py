# -*- coding: utf-8 -*-
from math import hypot
import pygame
from Node import Node

'''
grid contem numeros 0 (espaços livres), 1 (obstaculos), 2 (carro), 3 (objetivo)
'''

class AStar():

    def __init__(self,grid,posinit,posobj):
        self.node = Node(posinit,0)
        self.grid = grid
        self.objetivo = posobj
        self.tam = len(grid)
        self.opened = [self.node]
        self.closed = []
        self.path = []

    # ordena uma fila segundo seu custo f
    def sortQueue(self):
        self.opened.sort(key=lambda q: q.f_coast)

    def verify(self,node):
        for c in self.opened:
            if(c.pos==node.pos):
                return False
        for c in self.closed:
            if(c.pos==node.pos):
                return False
        return True

    def valida(self,childs):
        for c in childs:
            if(c.pos[0]>=0 and c.pos[0]<self.tam and c.pos[1]>=0 and c.pos[1]<self.tam):
                if(self.grid[c.pos[0],c.pos[1]]!=1 and self.verify(c)):
                    c.calcCosts(self.objetivo)
                    self.opened.append(c)

    def arraived(self,n):
        if(self.grid[n.pos[0],n.pos[1]]==3):
            return True
        return False

    def run(self):
        n = self.opened[0]
        n.calcCosts(self.objetivo)
        while(len(self.opened)>0 and not self.arraived(n)):
            n = self.opened[0]
            self.opened.remove(n)
            self.closed.append(n)
            self.valida(n.generateChilds())
            self.sortQueue()
        if(len(self.opened)>0):
            self.path.append(n.pos)
            while(n.pai!=None):
                self.path.append(n.pai.pos)
                n=n.pai
        print("Terminou")
        return self.path
