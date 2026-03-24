import xml.etree.ElementTree as ET
from node import NodeData, Node, Position

ESTILO_ENTEGRAMA    = "whiteSpace=wrap;html=1;"
ESTILO_CONEXION     = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;endArrow=none;endFill=0;"

class Tree():
    def __init__(self, dx=1000, dy=1000):
        self.nexo = ET.Element("mxGraphModel", 
        {
            "dx": str(dx), "dy": str(dy), "grid": "1", "gridSize": "10"
        })

        self.body = ET.SubElement(self.nexo, "root")

        ET.SubElement(self.body, "mxCell", id="0")
        ET.SubElement(self.body, "mxCell", id="1", parent="0")

    def close(self, filename):
        ET.indent(self.nexo, space="  ", level=0)    #Aplica pretty printing

        tree = ET.ElementTree(self.nexo)
        with open(filename, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=False)

    def drawBox(self, data: NodeData, factor_x=100, factor_y=40, width=80, height=40):
        cell = ET.SubElement(
            self.body,
            "mxCell",
            {
                "id": data.id_s,
                "parent":"1",
                "style":ESTILO_ENTEGRAMA,
                "value":data.text,
                "vertex":"1"
            }
        )

        ET.SubElement(
            cell,
            "mxGeometry",
            {
                "height": str(height),
                "width": str(width),
                "x": str(data.position.x * factor_x),
                "y": str(data.position.y * factor_y),
                "as": "geometry"
            }
        )
    
    def drawConnection(self, parent: Node, child: Node, id_lazo_s: str):
        cell = ET.SubElement(
            self.body,
            "mxCell",
            {
                "id": id_lazo_s,
                "edge": "1",
                "parent": "1",
                "source": parent.data.id_s,
                "style": ESTILO_CONEXION,
                "target": child.data.id_s
            }
        )

        ET.SubElement(
            cell,
            "mxGeometry",
            {
                "relative": "1",
                "as": "geometry"
            }
        )