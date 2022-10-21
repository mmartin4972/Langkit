import spacy
import tensorflow_hub as hub
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
from flask import Flask
from flask import request


app = Flask(__name__)

print("Loading Models. This could take some time")
# Load entity extractor
entity_extractor = spacy.load("./spacy/output")

def extract_entities(phrase:str) :
    return entity_extractor(phrase).ents

# Load word embedder
preprocessor = hub.KerasLayer(
    "https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
word_embedder = hub.KerasLayer(
    "https://tfhub.dev/tensorflow/small_bert/bert_en_uncased_L-2_H-128_A-2/2",
    trainable=True)

def get_phrase_embedding(phrase:str) :
    return word_embedder(preprocessor(tf.constant([phrase])))['pooled_output']

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
        'emb': tf.constant([[0]*128], tf.float32)
    }
}
print("Server Initialized Successfully")

@app.route("/")
def default():
    print("MESSAGE RECEIEVED")
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
                print(ent.text)
                for func in funcs :
                    dist = np.inner(funcs[func]['emb'], get_phrase_embedding(ent.text)) # TODO could do embedding in batch
                    print(func)
                    print(dist)
                    if best_dist < dist :
                        elt['FUNC'] = func
                        best_dist = dist

            elif ent.label_ == 'PARAM' :
                elt['PARAM'] = ent.text  

        res.append(elt)

    return res
