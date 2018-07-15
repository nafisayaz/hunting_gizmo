# -*- coding: utf-8 -*-
"""
Created on Wed May 30 21:24:03 2018

@author: nafis
"""

import matplotlib.pyplot as plt
import numpy as np
#from statistics import mean
import wave
#import sys

plt.figure(1)

class Audio:
    def __init__(self, audio):
        self.audio = wave.open(audio,'r')
        self.signal = self.audio.readframes(-1)
        self.signal = np.fromstring(self.signal, 'Int16')
        self.fr = self.audio.getframerate()
        self.time = np.linspace(0, 100, num=(len(self.signal)))
        self.fft = np.fft.fft(self.signal)

    def plot(self):
        plt.title("Audio waveforms")
        plt.plot(self.time, self.signal, self.fr, '.')
	
    def print_value(FILE_NAME):
        rms = [np.sqrt(np.mean(block**2)) for block in sf.blocks(FILE_NAME, blocksize=1024, overlap=512)]
        return rms




"""		
gana = Audio('new_file.wav')
gana.plot()
humm = Audio('new_file.wav')
plt.show()
"""


#if __name__ == "__main__":
#gana = Audio('new_file.wav')
#gana.plot()
#humm = Audio('new_file.wav')
#plt.show()




