

import webbrowser

class browse:
	def __init__(self):
		self.url = None

	def open_browser(self, url):
		webbrowser.get(using='chromium-browser').open(url)

	def is_openable_browser(self, text):

		is_found = 0;
		open_word = ""

		for i in range(0, len(text)):
		
			if text[i] == "open":
				open_word = text[i]
				is_found = 1
				continue
		
			return (is_found, open_word, text[i])    

