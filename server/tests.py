import spacy
import tensorflow_hub as hub
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

print("Loading Models. This could take some time")
# Load entity extractor
entity_extractor = spacy.load("./spacy/output")

# Load word embedder
word_embedder = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
print("Models loaded")

input_text = [
    "generate phrases",
    "generate me phrases",
    "translate phrases",
    "translate words",
]

funcs = [
    "generate phrases",
    "translate",
    "generate words"
]

input_embeddings = word_embedder(input_text)
func_embeddings = word_embedder(funcs)
for i, emb in enumerate(input_embeddings) :
    print(input_text[i])
    print(np.inner(func_embeddings[0], emb))
