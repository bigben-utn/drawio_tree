import sys
import subprocess
import os
import configparser

from logical_tree import buildTree
from spatial_tree import buildLayout
from visual_tree import Tree

def drawTree(tree: Tree, matrix, box_height, horizontal_distance, text_size):
    for row in matrix:
        for cell in row:
            if cell != None:
                tree.drawBox(cell.data, text_size, factor_x=(box_height + int(horizontal_distance / 2)), factor_y=box_height, width=(box_height * 2), height=box_height)
    index=1
    for level in niveles:
        for nodo in level:
            for child in nodo.children:
                tree.drawConnection(nodo, child, f"lazo-{index}")
                index += 1

def saveTree(tree: Tree, output_file):
    tree.close(output_file)
    print("Archivo generado exitosamente en:", output_file)

def copyFile(filename):                 #Specific for operative systems with powershell (e.g.: Windows 11)
    abs_path = os.path.abspath(filename)
    cmd = f"powershell -command \"Set-Clipboard -Path '{abs_path}'\""
    subprocess.run(cmd, shell=True)

    print(f"Archivo {filename} copiado exitosamente en el portapapeles.")

# - - - - - CONFIGURATION
if len(sys.argv) < 2:
    print("No se encontro el archivo de configuraciones.")
    exit()

config = configparser.ConfigParser()
config.read(sys.argv[1])

box_height          = int(config['Ajustes']['box_height'])
horizontal_distance = int(config['Ajustes']['horizontal_distance'])
text_size           = int(config['Ajustes']['text_size'])

key = config['Formato']['key'].strip('"')
should_copy_file = config['Permisos'].getboolean('copy_file')

input_file  = config['Archivos']['input_file']
output_file = config['Archivos']['output_file']
# - - - - - CONFIGURATION

niveles = buildTree(input_file, key)
mapa    = buildLayout(niveles)

tree = Tree()
drawTree(tree, mapa.matrix, box_height, horizontal_distance, text_size)
saveTree(tree, output_file)

if should_copy_file:
    copyFile(output_file)