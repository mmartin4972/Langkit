import eel
from os import path
import speech_recognition as sr
import translators as tr

eel.init(f'{path.dirname(path.realpath(__file__))}/templates')  
  
@eel.expose
def quick_translate_list(s: list) -> list:
    return [tr.google(w, from_language='en', to_language='es') for w in s]


@eel.expose
def quick_translate_word(w: str) -> str:
    return tr.google(w, from_language='en', to_language='es')


@eel.expose
def mic_click() -> str:
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