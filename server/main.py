import spacy
import tensorflow_hub as hub
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from enum import Enum

print("Loading Models. This could take some time")
# Load entity extractor
entity_extractor = spacy.load("./spacy/output")

# Load word embedder
word_embedder = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
print("Models loaded")

funcs = {
    'GEN_PHRASE': {
        'str': "generate phrases", 
        'emb': word_embedder(["generate phrases"])
    }
}

GEN_WORD = "generate words"
TRANS = "translate" 

input_text = [
    "hello"
    "generate me"
]

print(funcs['GEN_PHRASE']['emb'])

input_embeddings = word_embedder(input_text)
for i, emb in enumerate(input_embeddings) :
    print(input_text[i])
    print(np.inner(funcs['GEN_PHRASE']['emb'], emb))
