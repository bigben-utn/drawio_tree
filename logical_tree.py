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

    def fillVoid(self, key, fill):
        if key >= len(self):
            start   = len(self)
            end     = key

            for i in range(end - start + 1):
                self.append(fill)

    def __getitem__(self, s):
        if s == -1:
            return None
        else:
            self.fillVoid(s, copy.copy(self.default))
            return super().__getitem__(s)
    
    def __setitem__(self, key, value):
        self.fillVoid(key, copy.copy(self.default))
        return super().__setitem__(key, value)
    
def parseLine(line: str, key: str) -> tuple[int, str]:
    """
    Distingue las dos partes de una linea: nivel & texto (sin interpretacion de errores)

    - key (str): Cadena de texto que se define como un nivel. No puede usarse en el texto
    - key (char): Caracter que se define como un nivel. Puede usarse en el texto
    """

    if len(key) == 1:
        text = line.lstrip(key)
        level = len(line) - len(text)
    else:
        text = line.replace(key, '')
        level = line.count(key)

    return level, text.rstrip()

def buildTree(file: str, spechar: str = '*') -> tuple[Node, list[list[Node]]]:
    """
    Vincula nodos con sus hijos.
    
    Retorna dos objetos: El nodo raiz, y la lista de nodos organizada por niveles
    """

    id = 0
    linaje:  SmartList[Node]        = SmartList()
    levels:  SmartList[list[Node]]  = SmartList([])

    with open(file, 'r') as f:
        for line in f:
            level, text = parseLine(line, spechar)
            nodo = Node(NodeData(id, text, level), linaje[level - 1])

            levels[level].append(nodo)

            linaje[level] = nodo
            del linaje[level + 1:]

            id += 1

    return linaje[0], list(levels)