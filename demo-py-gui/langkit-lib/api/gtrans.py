# pip install googletrans
from googletrans import Translator

text1 = '''
A Római Birodalom (latinul Imperium Romanum) az ókori Róma által létrehozott 
államalakulat volt a Földközi-tenger medencéjében
'''

text2 = '''
Vysoké Tatry sú najvyššie pohorie na Slovensku a v Poľsku a sú zároveň jediným 
horstvom v týchto štátoch s alpským charakterom. 
'''

translator = Translator()

dt1 = translator.detect(text1)
print(dt1)

dt2 = translator.detect(text2)
print(dt2)