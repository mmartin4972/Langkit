from server.main import app
import os
import subprocess

if __name__ == "__main__":
    
    # Heroku specific stuff
    # TODO: This is really sketchy. I'm sure there's a better way
    p = '/app/use_model'
    if not os.path.exists(p) :
        os.mkdir(p)
        print("Downloading Universal Sentence Encoder Model")
        subprocess.call("curl -L \"https://tfhub.dev/google/universal-sentence-encoder/4?tf-hub-format=compressed\" | tar -zxvC /app/use_model", shell=True)
    
    app.run()