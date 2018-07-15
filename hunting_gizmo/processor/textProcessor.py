

from nltk.tokenize import sent_tokenize, word_tokenize
import xml.etree.ElementTree as ET
import os
#from naturalLangTool import tool as tl

class textProcessor:
	def __init__(self):
		self.text = None

	def self_intro(self):
		print("---------- From self Intro function")
		intro = self.get_reply("who_you")
		return str(intro)

	def stop_words(self):
		return ["please","hey", "hi", "hello", "am", "is", "are", "was", "were"]

	def tokenize(self, text):
		self.text = text
		tokens = word_tokenize(text)
		if len(tokens) == 1: # THIS IS FOR SINGLE WORD
			return tokens

		#stop_words = tl.nlt().stop_words()
		tokens_without_stop_words =  [word for word in tokens if not word in self.stop_words()] 

		return tokens_without_stop_words

	def put_underscore(self, tokens):
		str_tokens = '';
		for i in range(0, len(tokens)):
			if i != len(tokens)-1:
				str_tokens = str_tokens+tokens[i]+'_'
			else:
				str_tokens = str_tokens+tokens[i]
		return str_tokens;

	def get_reply(self, str_tokens):
		file_path = "/home/nafis/projects/JobsMarkt/hunting_gizmo/XMLs/Answers_Mappings"
		xml_file = os.path.join(file_path, 'Answers_Mappings.xml')
		tree = ET.parse(xml_file)
		root = tree.getroot()

		Answers = [element.text for child in root if child.tag == 'Answers_Questions' for element in child if element.tag ==  str_tokens ]
		return Answers


	def make_pair(self, child):
		return child.tag, child.text


	def make_chunk(self, m_list):
		
		if len(m_list) == 1:
			return m_list

		c_text = []
		pair = m_list[0]
		str_key = pair[0]
		int_key = pair[1]

		for i in range(1, len(m_list)):
			if m_list[i][1] == int_key:
				str_key = str_key + " " + m_list[i][0]
				if i == len(m_list)-1:
					c_text.append((str_key, int_key))
			else:
				c_text.append((str_key, int_key))
				str_key = m_list[i][0]
				int_key = m_list[i][1]

		return c_text




	def put_frequency(self, text):

		file_path = "/home/nafis/projects/JobsMarkt/hunting_gizmo/XMLs/words_frequency"
		xml_file = os.path.join(file_path, 'words_frequency.xml')
		tree = ET.parse(xml_file)
		root = tree.getroot()

		tokens = word_tokenize(text)
		xml_text = [ self.make_pair(child) for child in root ]
#		m_text = [word for xml_word in xml_text for token in tokens if token == xml_word[0] ]
		if len(xml_text) == 0:
			return 0
		m_text = []

		for token in tokens:
			for xml_word in xml_text:
				if xml_word[0] == token:
					m_text.append(xml_word)
					break
		print("put_frequency ----->", m_text)

		c_text = self.make_chunk(m_text)
		return c_text



	
