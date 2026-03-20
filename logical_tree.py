
class SmartList(list):
    """
    Clase irrestrictiva derivada de _list_:
    1. Acceder al índice _i=-1_ retorna _None_
    2. Fijar valor según un índice inexistente es posible: fuerza la existencia de dicho índice y todos los anteriores
    """

    def __getitem__(self, s):
        if s == -1:
            return None
        else:
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

class NodeData():
    """
    Empaquetador de datos necesario para la implementación de nodos en el diagrama
    """

    def __init__(self, id, text, nivel, id_s_beg="nodo-"):
        self.id     = id
        self.text   = text
        self.nivel  = nivel

        self.id_s = id_s_beg + str(id)

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

    def __getitem__(self, key):
        if key >= len(self.children):
            return None
        else:
            return self.children[key]

    def __str__(self):
        return str(self.data.text)
    
    def __repr__(self):
        return str(self)
    
def LineParser(line: str, spechar: str):
    if len(spechar) == 1:
        text = line.lstrip(spechar)
        level = len(line) - len(text)
    else:
        text = line.replace(spechar, '')
        level = line.count(spechar)

    return level, text.rstrip()                 #Remueve los espacios finales del texto

def BuildTree(file: str, spechar: str = '*'):
    id = 0
    linaje: SmartList[Node] = SmartList()

    with open(file, 'r') as f:
        for line in f:
            nivel, text = LineParser(line, spechar)
            nodo = Node(NodeData(id, text, nivel), linaje[nivel - 1])

            linaje[nivel] = nodo
            del linaje[nivel + 1:]

            id += 1

    return linaje[0]

#root: Node = BuildTree("tree.txt")
