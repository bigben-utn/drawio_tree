import copy
from node import *

class SmartList(list):
    """
    Clase irrestrictiva derivada de _list_:
    1. Acceder al índice _i=-1_ retorna _None_
    2. Acceder a un índice inexistente es posible: fuerza la existencia de dicho índice y todos los anteriores usando el elemento default
    """

    def __init__(self, default=None):
        super().__init__()
        self.default = default

    def append(self, object):
        return super().append(object)

    def __getitem__(self, s):
        if s == -1:
            return None
        else:
            if s >= len(self):
                start_point = len(self)
                end_point = s

                for i in range(end_point - start_point + 1):
                    self.append(copy.copy(self.default))

            return super().__getitem__(s)
    
    def __setitem__(self, key, value):
        if key >= len(self):
            start_point = len(self)
            end_point = key

            for x in range(end_point - start_point):
                self.append(None)
            
            self.append(value)
        else:
            return super().__setitem__(key, value)
    
def LineParser(line: str, spechar: str) -> tuple[int, str]:
    """
    Distingue las dos partes de una linea: nivel & texto (sin interpretacion de errores)
    """

    if len(spechar) == 1:
        text = line.lstrip(spechar)
        level = len(line) - len(text)
    else:
        text = line.replace(spechar, '')
        level = line.count(spechar)

    return level, text.rstrip()

def BuildTree(file: str, spechar: str = '*') -> tuple[Node, list[list[Node]]]:
    """
    Vincula nodos con sus hijos.
    
    Retorna dos objetos: El nodo raiz, y la lista de nodos organizada por niveles
    """

    id = 0
    linaje:  SmartList[Node]        = SmartList()
    levels:  SmartList[list[Node]]  = SmartList([])

    with open(file, 'r') as f:
        for line in f:
            nivel, text = LineParser(line, spechar)
            nodo = Node(NodeData(id, text, nivel), linaje[nivel - 1])

            levels[nivel].append(nodo)

            linaje[nivel] = nodo
            del linaje[nivel + 1:]

            id += 1

    return linaje[0], list(levels)

#root: Node = BuildTree("tree.txt")