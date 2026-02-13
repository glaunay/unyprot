from dataclasses import dataclass
from xml.etree import ElementTree as ET


@dataclass
class Domain:
    description: str
    begin: str
    end: str

    @staticmethod
    def from_xml_feature_node(node, ns):
        # node.find(f"{ns}feature[@type='domain']")[0].attrib["description"]

        try:
            return Domain(
                node.attrib["description"],
                node.find(f"{ns}location/{ns}begin").attrib["position"],
                node.find(f"{ns}location/{ns}end").attrib["position"],
            )
        except Exception as e:
            print(f"Failed toi parse doamin from f{ET.tostring(node)}")
            return None


"""
@dataclass
class DomainDef:
    type: str
    id: str
    common_name: str

    @staticmethod
    def from_xml_dbReference_node(node, ns):
        # node.find(f"{ns}feature[@type='domain']")[0].attrib["description"]

        try:
            return Domain(
                node.attrib["description"],
                node.find(f"{ns}location/{ns}begin").attrib["position"],
                node.find(f"{ns}location/{ns}end").attrib["position"],
            )
        except Exception as e:
            print(f"Failed toi parse doamin from f{ET.tostring(node)}")
            return None
"""
