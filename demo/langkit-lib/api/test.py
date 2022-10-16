import requests

def func ():
    x = requests.get('https://libretranslate.com/translate')
    print(x.headers)


if __name__ == "__main__":
    func()
