
class Node():

    def __init__(self,point):
        self.point = point
        self.childs = []

    def addChild(self,child):
        self.childs.extend(child)
