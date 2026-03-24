from node import Node, Position

class World():
    """
    Objeto con matriz definida según las dimensiones del subárbol de la raíz principal.

    La matriz es de referencias a objetos de tipo Node, agregables con _addNode(nodo, posición)_
    """

    def __init__(self, levels_list: list[ list[Node] ], node: Node = None, pos: Position = None):
        root = levels_list[0][0]
        self.size = Position(root.data.block_size, (len(levels_list) * 2) - 1)

        #El acceso a algún elemento de la matriz inicializada sigue el orden de las coordenadas... matriz[x][y]
        self.matrix = [[None for _ in range(self.size.y)] for _ in range(self.size.x)]
        
        if node != None and pos != None:
            self.addNode(node, pos)
    
    def addNode(self, node: Node, pos: Position):
        self.matrix[pos.x][pos.y] = node
        node.data.position = (pos.x, pos.y)

    def __str__(self) -> str:
        res = ""

        for y in range(self.size.y):
            res += "\n"
            for x in range(self.size.x):
                element = self.matrix[x][y]
                if element == None:
                    res += "____, "
                else:
                    res += str(element) + ", "

        return res

def updateNodes(levels_list: list[ list[Node] ]):
    """
    Datos actualizados post-proceso:
    - Tamaño del subárbol asociado
    - Posición del nodo dentro de su subárbol.
    """

    #Actualiza los datos de los nodos ascendentemente (desde las hojas hasta la raíz)
    for level in reversed(levels_list):
        for nodo in level:
            data    = nodo.data
            parent  = nodo.parent
            # - - - SELF - - -
            if nodo.isLeaf():
                data.block_size = 1
            else:
                data.block_size += len(nodo.children) - 1       #Contabiliza las unidades de separación entre nodos
            # - - - PARENT - - -
            if nodo.hasParent():
                parent.data.block_size += data.block_size
            # - - - POSITION - - -
            data.distance = int(data.block_size / 2)

def addSubtree(nodo: Node, mapa: World, offset: int) -> int:
    for child in nodo.children:
        data = child.data

        mapa.addNode(child, Position(data.distance + offset, 2 * data.level))

        if child.isLeaf():
            offset += data.block_size + 1
        else:
            offset = addSubtree(child, mapa, offset)

    return offset

def buildLayout(root: Node, levels_list: list[list[Node]]) -> World:
    updateNodes(levels_list)
    mapa = World(levels_list, root, Position(root.data.distance, 0))

    addSubtree(root, mapa, 0)

    return mapa