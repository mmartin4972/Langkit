import eel
from os import path
from random import randint
  
eel.init(f'{path.dirname(path.realpath(__file__))}/templates')  
  
# Exposing the random_python function to javascript
@eel.expose    
def random_python():
    print("Random function running")
    return randint(1,100)


@eel.expose
def mic_click():
    print("Mic clicked (python console)")

  
# Start the index.html file
eel.start("index.html", size=(1000, 665), port=8080)