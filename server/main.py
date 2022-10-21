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
# entity_extractor = spacy.load("./server/spacy/output")

# Load word embedder
# preprocessor = hub.KerasLayer(
#     "https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
# word_embedder = hub.KerasLayer(
#     "https://tfhub.dev/tensorflow/small_bert/bert_en_uncased_L-2_H-128_A-2/2",
#     trainable=True)
# print("Models loaded")

# # TODO: Would be good to cache these embeddings in a file to reduce launch time
# funcs = {
#     'GEN_PHRASE': {
#         'str': 'generate phrases', 
#         'emb': word_embedder(['generate phrases'])
#     },
#     'GEN_WORD': {
#         'str': 'generate words',
#         'emb': word_embedder(['generate words'])
#     },
#     'TRANS': {
#         'str': 'translate',
#         'emb': word_embedder(['translate'])
#     },
#     'UNKNOWN': {
#         'str': '',
#         'emb': tf.constant([[0]*512], tf.float32)
#     }
# }
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
        ents = entity_extractor(cmd['cmd']).ents

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
                    input_text = tf.constant([ent.text])
                    embedder_input = preprocessor(input_text)
                    print(word_embedder(embedder_input))
                    print(word_embedder(embedder_input)[0])

                    dist = np.inner(funcs[func]['emb'], word_embedder(embedder_input)[0]) # TODO could do embedding in batch
                    if best_dist < dist :
                        elt['FUNC'] = func
                        best_dist = dist

            elif ent.label_ == 'PARAM' :
                elt['PARAM'] = ent.text  

        res.append(elt)

    return res
