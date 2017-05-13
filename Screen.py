
class Screen():

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.display = None

    def getSize(self):
        return (self.width,self.height)
