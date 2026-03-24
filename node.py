from typing import NamedTuple

class Position(NamedTuple):
    x: int
    y: int

class NodeData():
    """
    Empaquetador de datos necesario para la implementación de nodos en el diagrama
    """

    def __init__(self, id, text, level, id_s_beg="nodo-"):
        self.id     = id
        self.text   = text
        self.level  = level

        self.id_s = id_s_beg + str(id)

        self.block_size = 0                 #Tamaño horizontal del subárbol asociado, que contiene al nodo self como raíz
        self.distance   = 0                 #Distancia horizontal relativa del nodo self, a la cara izquierda del bloque
        self.position   = Position(0, 0)    #Posición lógica absoluta en el mapa final

class Node():
    """
    Nodo con datos _NodeData_, único padre, múltiples hijos.

    isLegitimate=True: Su existencia actualiza la lista _children_ del nodo padre
    """

    def __init__(self, data: NodeData, parent: Node = None, update_parent: bool = True, children: list[Node] = None):
        if (children == None):
            children = []
            
        self.data           = data
        self.children       = children
        self.setParent(parent, update_parent)

    def setParent(self, parent: Node, update_parent: bool):
        self.parent = parent
        if update_parent and (parent != None):
            parent.children.append(self)

    def isLeaf(self) -> bool:
        return (len(self.children) == 0)

    def hasParent(self) -> bool:
        return (self.parent != None)

    def __getitem__(self, key) -> Node:
        if key >= len(self.children):
            return None
        else:
            return self.children[key]

    def __str__(self) -> str:
        if (self == None):
            return None
        else:
            return str(self.data.text)
    
    def __repr__(self) -> str:
        return str(self)