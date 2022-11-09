from main import app as application
import os

if __name__ == "__main__":
    contents = os.getenv('GOOGLE_CREDENTIALS')
    f = open("/app/cred.json", "w")
    f.write(contents)
    f.close()

    application.run()
