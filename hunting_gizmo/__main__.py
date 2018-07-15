

# -*- coding: utf-8 -*-
"""
Created on Sat May 26 14:21:20 2018

@author: nafis
"""


from audio_record import audio_record as ar
from speech_synthesizer import speech_synthesizer as ss
from audio_recognizer import audio_recognizer as AU

from os import path
import threading


AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "new_file.wav")


def listen():
	m = ar.Audio_record()
	m.record()
	m.writeFile()
	m.readFile()


def reply():
	text = AU.Audio_recognizer(AUDIO_FILE).text()
	print("FROM main ------------> ", text)
#	g.reply(text)
	g.reply("hi")

	return text


if __name__ == "__main__":

	g = ss.speech_syn("Gizmo", "Hi");
	
	while 1:
		listen()
		if reply() == "bye":
			break

#    help(AU)




#
