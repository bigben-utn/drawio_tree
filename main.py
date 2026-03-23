from logical_tree import BuildTree
from spatial_tree import nodeUpdater

TAB = "    "

def myFunc():
    pass

root, niveles = BuildTree("tree.txt", TAB)
nodeUpdater(niveles)

for nivel in niveles:
    for nodo in nivel:
        print(nodo, nodo.data.long, nodo.data.pos_relativa)