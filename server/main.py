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

db_name = 'local_langkit.db'

db_handler = handler(db_name)

# push some default data for testing
db_handler.add_topic("Fruit", ("en", "es"))
db_handler.add_topic("Another Topic", ("en", "es"))
db_handler.add_topic("Fruit But Blue", ("en", "es"))
db_handler.add_pair_to_topic( "Fruit", ("Apple", "Manzana"))
db_handler.add_pair_to_topic("Fruit But Blue", ("A Blue Apple", "Una Manzana Azul"))


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


@app.route('/get-topics', methods=['GET'])
def get_topics_endpoint():
    topic_list = db_handler.get_topics()

    r_list = []
    for i in topic_list:
        r_list.append({'id': i[0], 'name': i[1], 'sourceLang': i[2], 'targetLang': i[3]})

    return jsonify(r_list)


@app.route('/get-topic', methods=['GET'])
def get_topic_endpoint():
    data = request.json()

    topic_name = data['topic-name']

    topic = db_handler.get_topic(topic_name)

    r_list = []
    for i in topic:
        r_list.append({'id': i[0], 'source': i[1], 'translation': i[2]})

    return jsonify(r_list)


@app.route('/parse-cmd', methods=['POST'])
def parse_cmd():

    d = [
        {
            'id': 0,
            'name': 'Fruit',
            'sourceLang': 'en',
            'targetLang': 'es'
        },
        {
            'id': 1,
            'name': 'Fruit but blue',
            'sourceLang': 'en',
            'targetLang': 'es'
        },
        {
            'id': 2,
            'name': 'Fruit, still',
            'sourceLang': 'en',
            'targetLang': 'es'
        }
    ]

    return jsonify(d)

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


@app.route('/naive-gpt3-res', methods=['POST'])
def naive_gtp3_res():
    cmds = request.json


@app.route('/translate', methods=['POST'])
def quick_translate():
    print("Got request ", request.json)
    res = []
    for req in request.json :
        s = translate_text(req['to'], req['text'])
        res.append(s)
        print(s)
    return res



@app.route('/cmd', methods=['POST', 'GET'])
def cmd_endpoint():
    data = request.json

    if request.method == 'GET':
        type = data[0]['request-type']

        if type == 'user-topics':
            username = data[0]['username']
            topic_list = db_handler.get_topics(username)
    elif request.method == 'POST':
        if type == 'user-topics':
            username = data[0]['username']
            topic_list = db_handler.get_topics(username)
    else:
        return


@app.route('/user/init', methods=['POST'])
def user_init():
    req = request.json
    new_user = [req[0]['username'], req[0]['password']]
    db_handler.add_user(new_user[0], new_user[1])


def get_user_topics (user: str):
    return jsonify([
        {
            'src': 'source',
            'trn': 'translation'
        },
        {
            'src': 'source',
            'trn': 'translation'
        },
        {
            'src': 'source',
            'trn': 'translation'
        },
        {
            'src': 'source',
            'trn': 'translation'
        },
    ])


@app.route('/user/topics', methods=['GET'])
def user_get_topics():
    req = request.json

    username = req[0]['username']

    # Fake DB Request
    # After db is up this should be made using the username from the request

    if request.method == 'GET':
        return jsonify(
            topicname='Gerald',
            topiclist=get_user_topics(username)
        )

    return jsonify(
        topicname='Gerald',
        topiclist=get_user_topics(username)
    )

