

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 13:44:21 2018

@author: nafis
"""

from nltk.tokenize import sent_tokenize, word_tokenize
import xml.etree.ElementTree as ET


class textProcessor:
    def __init__(self):
        self.text = None

    def self_intro(self):
        import os
        path = os.path.dirname(os.path.realpath(__file__))
        xml_file = os.path.join(path, 'words_speed.xml')
        tree = ET.parse(xml_file)

        root = tree.getroot()
        intro = [element.text for child in root for element in child if element.tag == 'intro' ]
        print(intro)
        str_intro = 'Hi. this is Gizmo, a highly professional job profiler from Jobsmarkt, Switzerland.'+'I have gone through your incompleted profile in Jobsmarkt. I will help you for futher process.'+'So, I will ask you few questions for registration, please help me.'
        sent_tokens =  sent_tokenize(str(intro)) # intro.split('.')
        print(sent_tokens)
        return sent_tokens

    def do_pair(self, child):
        return child.tag, child.text

    def speed(self, text):
        self.text = text
        tokens = word_tokenize(self.text)

        import os
        path = os.path.dirname(os.path.realpath(__file__))
        xml_file = os.path.join(path, 'words_speed.xml')
        tree = ET.parse(xml_file)

        root = tree.getroot()

        xml_words = [self.do_pair(child) for child in root ]

        word_with_speed = [ word for word in  xml_words if word[0] in tokens]

        return word_with_speed
