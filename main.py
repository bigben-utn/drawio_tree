from logical_tree import buildTree
from spatial_tree import *
from visual_tree import Tree
from node import Position

TAB = "    "

root, niveles   = buildTree("tree.txt", TAB)
mapa            = buildLayout(root, niveles)

arbol = Tree()

for row in mapa.matrix:
    for cell in row:
        if cell != None:
            print(cell, cell.data.position.x)
            arbol.drawBox(cell.data, 90, 45, 100, 50)

id_=1
for level in niveles:
    for nodo in level:
        for child in nodo.children:
            arbol.drawConnection(nodo, child, f"lazo-{id_}")
            id_ += 1

arbol.close("tree.xml")