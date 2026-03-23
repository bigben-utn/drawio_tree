from node import Node

class Mapa():
    def __init__(self, niveles: list[list[Node]]):
        root = niveles[0][0]

        self.x = root.data.long
        self.y = (len(niveles) * 2) - 1

        self.matrix = []
        for y in range(0, self.y):
            self.matrix.append([])
            for x in range(0, self.x):
                self.matrix[y].append(None)
    
    def add(self, node: Node, x, y):
        self.matrix[x][y] = node
        node.data.pos_absoluta = (x, y)

    def __str__(self):
        res = ""
        for y in range(0, self.y):
            res += str(self.matrix[y])
            res += "\n"
        return res

def nodeUpdater(niveles: list[list[Node]]):
    for i in range(0, len(niveles)):
        nivel = niveles[len(niveles) - 1 - i]
        for nodo in nivel:
            if (nodo.isLeaf()):
                nodo.data.long = 1
            else:
                nodo.data.long += len(nodo.children) - 1
            
            if (nodo.parent != None):
                nodo.parent.data.long += nodo.data.long
            
            nodo.data.pos_relativa = int((nodo.data.long - 1) / 2)