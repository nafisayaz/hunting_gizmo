


from nltk.tokenize import sent_tokenize, word_tokenize
import xml.etree.ElementTree as ET

class sent_parse:
    def __init__(self):
        self.intro = None

    def parse_intro(self):
        import os
        path = os.path.dirname(os.path.realpath(__file__))
        xml_file = os.path.join(path, 'words_speed.xml')
        tree = ET.parse(xml_file)

        root = tree.getroot()
        intro = [element.text for child in root for element in child if element.tag == 'intro' ]

        self.intro = self.getParse(intro)
