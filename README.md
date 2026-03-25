# drawio_tree
Programa de Python para la generación de arboles en archivos XML a partir de archivos TXT con lenguaje estructurado simple.
Dicho archivo XML será compatible con draw.io

- Clonación: git clone https://github.com/bigben-utn/drawio_tree.git
- Ejecución: python main.py [settings_filename]

*settings_filename: Es el archivo de configuración, típicamente: settings.ini*

El contenido del archivo XML resultante puede agregarse a draw.io mediante:
draw.io -> Extras -> Edit Diagram...

Nota: El archivo *tree.txt* y *settings.ini* son ejemplos de uso, y son los únicos dispuestos a ser modificados

**ARCHIVO DE CONFIGURACION**

- box_height: Establece la cantidad de puntos (de draw.io) que ocupa verticalmente cada entegrama
- horizontal_distance: Establece la mínima distancia que debe haber entre nodos
- text_size: Establece el tamaño de la tipografía encerrada en cada entegrama
- key: Establece la cadena de texto según la cual se formatea el archivo *input_filename*
- input_filename: Archivo de tipo *txt* con lenguaje estructurado
- output_filename: Archivo *xml* utilizable en draw.io
- copy_file: Establece si se debe copiar el archivo *output_filename* en el portapapeles

Nota: Si copy_file está activo, desde draw.io: *ctrl*+*V* pegará inmediatamente el diagrama del árbol

**FORMATO**

En el archivo *input_filename* se incorporan los textos a incluir en cada entegrama.
En cada línea se describe a un único nodo (asociado a cierto entegrama).
Al inicio de la linea se usa una cadena de texto *key* con sucesivas repeticiones, la cantidad de apariciones establece el nivel del nodo.

**PRINCIPIOS DEL DIAGRAMA**

- Si un par de nodos comparten nivel, entonces coincide su disposición vertical (se diagraman a la misma altura).
- Un nodo se encuentra centrado horizontalmente respecto de su sub-árbol asociado.
- Un nodo no debe estar debajo de otro nodo, a menos que se pueda crear un camino unidireccional entre ambos.
- Cada nodo tiene un único nodo padre.
- Los nodos hijos de un nodo están al mismo nivel.
