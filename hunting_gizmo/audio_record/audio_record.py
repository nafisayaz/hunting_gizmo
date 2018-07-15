

import sounddevice as sd
import soundfile as sf

class Audio_record:

	def __init__(self):
		self._data = None
		self._fs = 41000
      
          
	def record(self):
		sd.default.samplerate = self._fs
		sd.default.channels = 2
		self._data = sd.rec(5 * self._fs, dtype = 'float32')
		sd.wait()
	
	def play(self):
		sd.play(self._data)
		sd.wait()
		print(self._data)

	
	def rec_play(self):
		myrecording = sd.playrec(self._data)
		print(myrecording)

	
	def writeFile(self):
		sf.write('new_file.wav', self._data, self._fs)

	
	def readFile(self):
		data, samplerate = sf.read('new_file.wav')
#		print(data)
#		print(samplerate)







