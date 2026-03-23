class NodeData():
    """
    Empaquetador de datos necesario para la implementación de nodos en el diagrama
    """

    def __init__(self, id, text, nivel, id_s_beg="nodo-"):
        self.id     = id
        self.text   = text
        self.nivel  = nivel

        self.id_s = id_s_beg + str(id)

        self.long = 0                   #Longitud
        self.pos_relativa = 0           #Respecto de la cara izquierda del bloque que engloba al subarbol asociado

class Node():
    """
    Nodo con datos _NodeData_, único padre, hijos.

    isLegitimate=True: Su existencia actualiza la lista _children_ del padre
    """

    def __init__(self, data: NodeData, parent: Node = None, isLegitimate: bool = True, children: list[Node] = None):
        if (children == None):
            children = []
            
        self.data           = data
        self.isLegitimate   = isLegitimate
        self.children       = children
        self.setParent(parent)

    def setParent(self, parent: Node):
        self.parent = parent
        if self.isLegitimate and (parent != None):
            parent.children.append(self)

    def isLeaf(self) -> bool:
        return (len(self.children) == 0)

    def __getitem__(self, key) -> Node:
        if key >= len(self.children):
            return None
        else:
            return self.children[key]

    def __str__(self):
        return str(self.data.text)
    
    def __repr__(self):
        return str(self)