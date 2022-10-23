import eel
from os import path
from random import randint
import speech_recognition as sr
from googletrans import Translator

eel.init(f'{path.dirname(path.realpath(__file__))}/templates')  
  
@eel.expose
def quick_translate_list(s):
    tr = Translator()

    return [tr.translate(w, dest="fi") for w in s.split(' ')]

@eel.expose
def quick_translate_word(s):
    tr = Translator()

    return tr.translate(s)

@eel.expose
def mic_click():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
             
            r.adjust_for_ambient_noise(source, duration=0.2)
             
            audio = r.listen(source)

            return r.recognize_google(audio)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occured")

    return "error"

  
# Start the index.html file
eel.start("index.html", size=(1020, 750), port=8080)