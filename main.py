from logical_tree import BuildTree
from spatial_tree import *

TAB = "    "

def myFunc():
    pass

root, niveles = BuildTree("tree.txt", TAB)
nodeUpdater(niveles)

mapa = Mapa(niveles)

mapa.add(root, root.data.pos_relativa, 0)
agregar_hijos(root, mapa, 0)

print(mapa)