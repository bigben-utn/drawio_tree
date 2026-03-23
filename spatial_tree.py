from node import Node

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