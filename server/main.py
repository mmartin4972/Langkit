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
    res = []	
    	
    for cmd in cmds :	
        res.append(parse_cmd(cmd['cmd']))	
        	
    return jsonify(res)


def prompt_engineer (topic: str, ty: str):
    s = ''

    if ty == 'phrases':
        s = '''You are a teacher building a vocabulary list for your students on the topic "%s". You will generate the following as lists:

        1. Five complex phrases as a numbered list related to "%s"

        2. Five short phrases as a numbered list related to "%s"''' % (topic, topic, topic)
    elif ty == 'words':
        s = '''You are a teacher building a vocabulary list for your students on the topic "%s". You will generate the following as lists:

        1. Five complex words as a numbered list related to "%s"

        2. Five short words as a numbered list related to "%s"''' % (topic, topic, topic)
    elif ty == 'other':
        s = '''You are a teacher building a vocabulary list for your students on the topic "%s". You will generate perfectly formatted the following:

        1. Three complex sentences as a numbered list related to "%s"

        2. Three short sentences as a numbered list related to "%s"

        3. Three medium sentences as a numbered list related to "%s"

        4. Eight phrases as a numbered list related to "%s"''' % (topic, topic, topic, topic, topic)
    
    print("Parsed")
    print(s)
    return s


def get_choices (s: str):
    s = s.strip()
    clean_s = ""
    for c in s:
        if c.isalpha() or c == "," or c == " " :
            clean_s += c
    return clean_s.split(', ') 

    # extracted = []
    # buildastring = ''
    # read_mode = False
    # for c in s:
    #     if read_mode:
    #         if c == '\n':
    #             read_mode = False
    #             extracted.append(buildastring)
    #             buildastring = ''
    #             continue
    #         buildastring += c
    #     elif c == ' ':
    #         read_mode = True

    # return extracted


openai.api_key = os.getenv("OPENAI_KEY")
# TODO: We can do alot of stuff to properly configure this
def query_gpt3(query, n_in=1, max_tokens_in=300) :
    out = openai.Completion.create(
        model="text-davinci-002", # could also use text-cure-001 or any other models on this page (https://beta.openai.com/docs/models/gpt-3)
        prompt=query,
        n=n_in,
        max_tokens=max_tokens_in,
    )
    print(out)
    res = []
    for choice in out['choices']:
        res.append(choice['text'])

    return res[0]


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

    # Classify the command
    parsed = parse_cmd(req[0]['cmd'])

    func = parsed['FUNC']
    param = parsed['PARAM']

    # Get information to translate
    generated_strings = []
    if 'GEN_PHRASE' == func:
        r = query_gpt3(prompt_engineer(param, "phrases"))
        generated_strings = get_choices(r)
    elif 'GEN_WORD' == func:
        r = query_gpt3(prompt_engineer(param, "words"))
        generated_strings = []
        for choice in get_choices(r) :
            print(choice)
            for word in choice.split(', ') :
                print(word)
                generated_strings.append(word)
    elif 'TRANS' == func:
        generated_strings = param.split(', ')
    else:
        r = query_gpt3(prompt_engineer(param, "other"))
        generated_strings = get_choices(r)
    
    print ("Generate string", generated_strings)
    # Translate
    res = []
    for s in generated_strings:
        source = translate_text(s, target=req[0]['from'])
        target = translate_text(s, target=req[0]['to'])
        res.append({'source': source, 'translation': target})
    
    return jsonify(res)
