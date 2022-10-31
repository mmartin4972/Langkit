import spacy
import tensorflow_hub as hub
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import translators as tr
from flask import Flask
from flask import request
from word_embedding.word_embedder import WordEmbedder

app = Flask(__name__)

print("Loading Models. This could take some time")
# Load entity extractor
entity_extractor = spacy.load("./spacy/output")

def extract_entities(phrase:str) :
    return entity_extractor(phrase).ents

# Load word embedder
word_embedder = WordEmbedder()

def get_phrase_embedding(phrase:str) :
    return word_embedder.get_embedding([phrase])[0]

print("Models loaded")

# TODO: Would be good to cache these embeddings in a file to reduce launch time
funcs = {
    'GEN_PHRASE': {
        'str': 'generate phrases', 
        'emb': get_phrase_embedding('generate phrases')
    },
    'GEN_WORD': {
        'str': 'generate words',
        'emb': get_phrase_embedding('generate words')
    },
    'TRANS': {
        'str': 'translate',
        'emb': get_phrase_embedding('translate')
    },
    'UNKNOWN': {
        'str': '',
        'emb': [[0]*512]
    }
}
print("Server Initialized Successfully")

@app.route("/")
def default():
    return "Server Ack\n"

@app.route('/parse-cmd', methods=['POST'])
def parse_cmd():
    cmds = request.json
    res = []
    for cmd in cmds :
        print(cmd)
        ents = extract_entities(cmd['cmd'])

        elt = {
            'FUNC':'UNKNOWN',
            'PARAM':''
        }
        
        # Look through found entities to populate elt
        for ent in ents :
            
            if ent.label_ == 'FUNC' :
                # Find func enum that best matches extracted func phrase
                best_dist = 0.5
                for func in funcs :
                    dist = np.inner(funcs[func]['emb'], get_phrase_embedding(ent.text)) # TODO could do embedding in batch
                    if best_dist < dist :
                        elt['FUNC'] = func
                        best_dist = dist

            elif ent.label_ == 'PARAM' :
                elt['PARAM'] = ent.text  

        res.append(elt)

    return res


@app.route('/demo2', methods=['POST'])
def demo2():
    cmds = request.json
    res = []
    for cmd in cmds:
        for ent in extract_entities(cmd['cmd']):
            if ent.text == "coffee":
                res.append({'SRC':'coffee','TRN':'café'})
                res.append({'SRC':'a rich, dark roast','TRN':'Un tostado rico y oscuro'})
                res.append({'SRC':'a bright, light roast','TRN':'Un tostado brillante y ligero'})
                res.append({'SRC':'a smooth, rich coffee','TRN':'Un café rico y suave'})
                res.append({'SRC':'fruity flavor','TRN':'sabor afrutado'})
                res.append({'SRC':'I love a cup of coffee','TRN':'me encanta una taza de cafe'})
                break
            if ent.text == "life":
                res.append({'SRC':'life','TRN':'la vida'})
                res.append({'SRC':'advice','TRN':'consejo'})
                res.append({'SRC':'Attitude is everything','TRN':'Actitud es todo'})
                res.append({'SRC':'You only live once','TRN':'sólo se vive una vez'})
                res.append({'SRC':'Life is what you make it','TRN':'La vida es lo que tu haces de ella'})
                res.append({'SRC':'Follow your heart','TRN':'Sigue a tu corazón'})
                res.append({'SRC':'Believe in yourself.','TRN':'Creer en tu mismo'})
                break
            if ent.text == "fruits":
                res.append({'SRC':'apple','TRN':'manzana'})
                res.append({'SRC':'orange','TRN':'naranja'})
                res.append({'SRC':'watermelon','TRN':'sandía'})
                res.append({'SRC':'pineapple','TRN':'piña'})
                res.append({'SRC':'plum','TRN':'ciruela'})
                res.append({'SRC':'banana','TRN':'plátano'})
            if ent.text == "artificial":
                res.append({'SRC':'artificial intelligence','TRN':'inteligencia artificial'})

    return res

def quick_translate(w: str) -> str:
    s = tr.google(w, from_language='en', to_language='es')
    return s

@app.route('/demo', methods=['POST'])
def demo ():
    cmds = request.json
    res = []
    for cmd in cmds :
        print(cmd)
        ents = extract_entities(cmd['cmd'])

        elt = {
            'FUNC':'UNKNOWN',
            'PARAM':''
        }
        
        # Look through found entities to populate elt
        for ent in ents :
            
            if ent.label_ == 'FUNC' :
                # Find func enum that best matches extracted func phrase
                best_dist = 0.5
                for func in funcs :
                    dist = np.inner(funcs[func]['emb'], get_phrase_embedding(ent.text)) # TODO could do embedding in batch
                    if best_dist < dist :
                        elt['FUNC'] = func
                        best_dist = dist

            elif ent.label_ == 'PARAM' :
                elt['PARAM'] = ent.text  
    
    if elt['FUNC'] == 'TRANS':
        res.append({elt['PARAM'], quick_translate(elt['PARAM'])})
    elif elt['FUNC'] == 'GEN_WORD':
        res.append({'SRC':'coffee','TRN':'café'})
        res.append({'SRC':'a rich, dark roast','TRN':'Un tostado rico y oscuro'})
        res.append({'SRC':'a bright, light roast','TRN':'Un tostado brillante y ligero'})
        res.append({'SRC':'a smooth, rich coffee','TRN':'Un café rico y suave'})
        res.append({'SRC':'fruity flavor','TRN':'sabor afrutado'})
        res.append({'SRC':'I love a cup of coffee','TRN':'me encanta una taza de cafe'})
    elif elt['FUNC'] == 'GEN_PHRASE':
        res.append({'SRC':'coffee','TRN':'café'})
        res.append({'SRC':'a rich, dark roast','TRN':'Un tostado rico y oscuro'})
        res.append({'SRC':'a bright, light roast','TRN':'Un tostado brillante y ligero'})
        res.append({'SRC':'a smooth, rich coffee','TRN':'Un café rico y suave'})
        res.append({'SRC':'fruity flavor','TRN':'sabor afrutado'})
        res.append({'SRC':'I love a cup of coffee','TRN':'me encanta una taza de cafe'})
    elif elt['FUNC'] == 'UNKNOWN':
        res.append({'SRC':'coffee','TRN':'café'})
        res.append({'SRC':'a rich, dark roast','TRN':'Un tostado rico y oscuro'})
        res.append({'SRC':'a bright, light roast','TRN':'Un tostado brillante y ligero'})
        res.append({'SRC':'a smooth, rich coffee','TRN':'Un café rico y suave'})
        res.append({'SRC':'fruity flavor','TRN':'sabor afrutado'})
        res.append({'SRC':'I love a cup of coffee','TRN':'me encanta una taza de cafe'})

    return res
