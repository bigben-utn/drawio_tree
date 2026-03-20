from logical_tree import BuildTree, Node

TAB = "    "

root: Node = BuildTree("tree.txt", TAB)
print(root.children)