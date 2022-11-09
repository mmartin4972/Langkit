from main import app as application
import os

if __name__ == "__main__":
    # Hack for Creating Google Credentials From Env Variable
    print("Doing Credential stuff\n")
    contents = os.getenv('GOOGLE_CREDENTIALS')
    f = open("/app/cred.json", "w")
    f.write(contents)
    f.close()
    print("Got contents: ", contents)

    application.run()
