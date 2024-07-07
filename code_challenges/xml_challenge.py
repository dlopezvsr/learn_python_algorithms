import xml.etree.ElementTree as ET

data_xml = """
<data>
    <country name="Liechtenstein">
        <year>2008</year>
    </country>
</data>
"""


# for every node next

class XMLHandler:

    def __init__(self, xml_text):
        self.xml_text = xml_text

    def xml_processor(self):
        root = ET.ElementTree(ET.fromstring(self.xml_text)).getroot()
        for node in root:
            if a := (node.keys()):
                for key in a:
                    setattr(XMLHandler, key, node.attrib[key])


xml_class = XMLHandler(data_xml)
xml_class.xml_processor()
attribute = xml_class.name
location = xml_class.direction
print(attribute, location)
