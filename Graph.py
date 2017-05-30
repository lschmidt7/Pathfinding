
def Graph():

    def __init__(self, node):
        self.initNode = Node(node)
        self.node_atual = self.initNode

    def addNodes(self,nodes):
        self.node_atual.addChild(nodes)
