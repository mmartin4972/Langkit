import spacy
import tensorflow_hub as hub
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from flask import Flask, request, jsonify
from word_embedding.word_embedder import WordEmbedder
from translate.translate import translate_text
import openai
import os

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
        'emb': [	
            get_phrase_embedding('generate phrases'),	
            get_phrase_embedding('generate sentences'),	
            get_phrase_embedding('create sentences'),	
            get_phrase_embedding('develop phrases'),	
        ]	
    },	
    'GEN_WORD': {	
        'str': 'generate words',	
        'emb': [	
            get_phrase_embedding('generate words'),	
            get_phrase_embedding('generate vocabulary'),	
            get_phrase_embedding('create words'),	
            get_phrase_embedding('develop words'),	
        ]	
    },	
    'TRANS': {	
        'str': 'translate',	
        'emb': [	
            get_phrase_embedding('translate'),	
            get_phrase_embedding('translate the phrase'),	
        ]	
    },	
    'UNKNOWN': {	
        'str': '',	
        'emb': [	
            [[0]*512]	
        ]	
    }	
}

print("Server Initialized Successfully")

@app.route("/")
def default():
    return "Server Ack\n"

def parse_cmd(cmd) :
    ents = extract_entities(cmd.lower())

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
                for emb in funcs[func]['emb'] :	
                    dist = np.inner(emb, get_phrase_embedding(ent.text)) # TODO could do embedding in batch	
                    if best_dist < dist :	
                        elt['FUNC'] = func	
                        best_dist = dist

        elif ent.label_ == 'PARAM' :
            elt['PARAM'] = ent.text  

    return elt


@app.route('/parse-cmd', methods=['POST'])
def parse_cmd_point():
    cmds = request.json
    res = parse_cmd(cmds['cmd'])

    sourceLanguage = cmds['sourceLang'].lower()
    targetLanguage = cmds['targetLang'].lower()

    phrases = query_gpt3(res['PARAM'])

    jsonified_phrases = []

    for p in phrases:
        if sourceLanguage == 'EN':
            jsonified_phrases.append({'source': p, 'translation': translate_text(p, target=targetLanguage)})
        else:
            jsonified_phrases.append({'source': translate_text(p, target=sourceLanguage), 'translation': translate_text(p, target=targetLanguage)})
            
    return jsonify(phrases)
    # cmds = request.json	
    # res = []	
    	
    # for cmd in cmds :	
    #     res.append(parse_cmd(cmd['cmd']))	
        	
    # return jsonify(res)


def prompt_engineer (topic: str):
    return '''You are a teacher building a vocabulary list for your students on the topic "%s". You will generate perfectly formatted the following:

    1. Three complex sentences

    2. Three short sentences

    3. Three medium sentences

    4. Eight phrases''' % topic


def get_choices (s: str):
    extracted = []
    buildastring = ''
    read_mode = False
    for c in s:
        if read_mode:
            if c == '\n':
                read_mode = False
                extracted.append(buildastring)
                buildastring = ''
                continue
            buildastring += c
        elif c == ' ':
            read_mode = True

    return extracted


openai.api_key = os.getenv("OPENAI_KEY")
# TODO: We can do alot of stuff to properly configure this
def query_gpt3(query, n_in=1, max_tokens_in=245) :
    out = openai.Completion.create(
        model="text-davinci-003", # could also use text-cure-001 or any other models on this page (https://beta.openai.com/docs/models/gpt-3)
        prompt=prompt_engineer(query),
        n=n_in,
        max_tokens=max_tokens_in,
    )
    res = []
    for choice in out['choices'] :
        res = get_choices(choice['text'][0])

    return res


@app.route('/naive-gpt3-res', methods=['POST'])
def naive_gtp3_res():
    print("Got request ", request.json)
    res = []
    for req in request.json :
        out = query_gpt3(req['prompt'])
        res.append(out)
    return jsonify(res)


@app.route('/translate', methods=['POST'])
def quick_translate():
    print("Got request ", request.json)
    res = []
    for req in request.json :
        s = translate_text(req['text'], req['to'], req['from'])
        res.append(s)
        print(s)
    return jsonify(res)


@app.route('/process', methods=['POST'])
def process():
    req = request.json
    # cmd = [{'cmd':'text', 'from':'text', 'to':'text'}]
    # Error checking
    if (len(req) != 1) :
        return 406

    # Classify the command
    parsed = parse_cmd(req[0]['cmd'])
    print(parsed)
    func = parsed['FUNC']
    param = parsed['PARAM']

    # Get information to translate
    src_trans = []
    if 'GEN_PHRASE' == func :
        print("Generate phrase about " + param)
        src_trans = query_gpt3("generate one short sentence about " + param)
    elif 'GEN_WORD' == func :
        print("Generate words about " + param)
        src_trans = query_gpt3("generate one word about " + param)
    elif 'TRANS' == func :
        print("Translate")
        src_trans = [param]
    else : # Unknown catch all case will just translate the input
        print("Unknown")
        src_trans = [req[0]['cmd']] # TODO: NOT SURE IF THIS WORKS
    
    # Translate the information
    res = []
    for src in src_trans :
        clean_src = src.strip()
        target = translate_text(clean_src, req[0]['to'], req[0]['from'])
        res.append({'src':clean_src, 'target':target})
    
    return jsonify(res)




# Carson Functions

# import translators as tr
# from database.handler import handler

# db_name = 'local_langkit.db'

# db_handler = handler(db_name)

# # push some default data for testing
# db_handler.add_topic("Fruit", ("en", "es"))
# db_handler.add_topic("Another Topic", ("en", "es"))
# db_handler.add_topic("Fruit But Blue", ("en", "es"))
# db_handler.add_pair_to_topic( "Fruit", ("Apple", "Manzana"))
# db_handler.add_pair_to_topic("Fruit But Blue", ("A Blue Apple", "Una Manzana Azul"))

# @app.route('/get-topics', methods=['GET'])
# def get_topics_endpoint():
#     topic_list = db_handler.get_topics()

#     r_list = []
#     for i in topic_list:
#         r_list.append({'id': i[0], 'name': i[1], 'sourceLang': i[2], 'targetLang': i[3]})

#     return jsonify(r_list)


# @app.route('/get-topic', methods=['GET'])
# def get_topic_endpoint():
#     data = request.json()

#     topic_name = data['topic-name']

#     topic = db_handler.get_topic(topic_name)

#     r_list = []
#     for i in topic:
#         r_list.append({'id': i[0], 'source': i[1], 'translation': i[2]})

#     return jsonify(r_list)

