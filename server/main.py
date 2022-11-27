import spacy
import tensorflow_hub as hub
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import translators as tr
from flask import Flask, request, jsonify
from word_embedding.word_embedder import WordEmbedder
from translate.translate import translate_text
from database.handler import handler

# Start INITIALIZATION

## Set Database Name
db_name = 'local_langkit.db'

## Create Database Handler Object
db_handler = handler(db_name)

## Fill Database with Default Data
db_handler.add_topic("Fruit", ("en", "es"))
db_handler.add_topic("Another Topic", ("en", "es"))
db_handler.add_topic("Fruit But Blue", ("en", "es"))
db_handler.add_pair_to_topic( "Fruit", ("Apple", "Manzana"))
db_handler.add_pair_to_topic("Fruit But Blue", ("A Blue Apple", "Una Manzana Azul"))
db_handler.add_pair_to_topic("Fruit But Blue", ("A Red Apple", "Una Manzana Roja"))
db_handler.add_pair_to_topic("Fruit But Blue", ("An Orange Orange", "Una Naranja Naranja"))

## Create Flask App Object
app = Flask(__name__)

## Create Spacy Entity Extraction Object
entity_extractor = spacy.load("./spacy/output")

## Create Word Embedder Object
word_embedder = WordEmbedder()

## Create Entity Extraction Function
def extract_entities(phrase:str) :
    return entity_extractor(phrase).ents

## Create Word Embedding Functions
## TODO: Would be good to cache these embeddings in a file to reduce launch time
def get_phrase_embedding(phrase:str) :
    return word_embedder.get_embedding([phrase])[0]

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

# End INITILIZATION


# Start: END POINT FUNCTIONS

## Root Function
@app.route("/")
def default():
    return "Server Ack\n"


## Get Topics Endpoint
@app.route('/get-topics', methods=['GET'])
def get_topics_endpoint():
    topic_list = db_handler.get_topics()

    r_list = []
    for i in topic_list:
        r_list.append({'id': i[0], 'name': i[1], 'sourceLang': i[2], 'targetLang': i[3]})

    return jsonify(r_list)


## Get Topic Endpoint
@app.route('/get-topic', methods=['POST'])
def get_topic_endpoint():
    data = request.json()

    topic_name = data['name']

    topic = db_handler.get_topic(topic_name)

    r_list = []
    for i in topic:
        r_list.append({'id': i[0], 'source': i[1], 'translation': i[2]})

    return jsonify(r_list)


## Parse Command Endpoint
@app.route('/parse-cmd', methods=['POST'])
def parse_cmd():
    cmds = request.json
    res = []
    for cmd in cmds:
        ents = extract_entities(cmd['cmd'])

        elt = {
            'FUNC':'UNKNOWN',
            'PARAM':''
        }
        
        # Look through found entities to populate elt
        for ent in ents:
            if ent.label_ == 'FUNC':
                # Find func enum that best matches extracted func phrase
                best_dist = 0.5
                for func in funcs:
                    dist = np.inner(funcs[func]['emb'], get_phrase_embedding(ent.text)) # TODO could do embedding in batch
                    if best_dist < dist:
                        elt['FUNC'] = func
                        best_dist = dist

            elif ent.label_ == 'PARAM':
                elt['PARAM'] = ent.text  

        res.append(elt)

    return res


## Add Topic Endpoint
@app.route('/add-topic', methods=['POST'])
def parse_cmd():
    pass


## Remove Topic Endpoint
@app.route('/remove-topic', methods=['POST'])
def parse_cmd():
    pass


## Update Pairs Endpoint
@app.route('/update-pairs', methods=['POST'])
def parse_cmd():
    pass

# End: END POINT FUNCTIONS

