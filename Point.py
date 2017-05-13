

class Point():

    def __init__(self):
        self.x = 0
        self.y = 0

    def PointDistance(self,p1,p2):
        return math.hypot(p1.x-p2.x,p1.y-p2.y)
