from logical_tree import buildTree
from spatial_tree import *

TAB = "    "

root, niveles   = buildTree("tree.txt", TAB)
mapa            = buildLayout(root, niveles)

print(mapa)