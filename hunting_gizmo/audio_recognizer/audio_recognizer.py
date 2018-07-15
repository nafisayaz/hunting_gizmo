
import speech_recognition as sr
r  = sr.Recognizer()


class Audio_recognizer:

    def __init__(self, AUDIO_FILE):
        self.AUDIO_FILE = AUDIO_FILE
        
    def text(self):
        
        with sr.AudioFile(self.AUDIO_FILE) as source:
            audio = r.record(source)
        try:
            return r.recognize_google(audio)
        #    return r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return  "Recog Error; {0}".format(e)

        



