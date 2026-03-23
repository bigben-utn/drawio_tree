from logical_tree import BuildTree
from spatial_tree import *

TAB = "    "

root, niveles   = BuildTree("tree.txt", TAB)
mapa            = buildLayout(root, niveles)

print(mapa)