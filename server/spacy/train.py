from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from tqdm import tqdm
import re
import json

# TODO:
# Replace TRAIN_DATA with something that will read from the ner_train.json file and
#   generate the below structure using regex
# TRAIN_DATA = [
#   ("Generate me phrases about dinosaurs.", { 
#     'entities': [(0, 19, "FUNC"),(26, 35, "PARAM")]
#     }),

#   ("translate the phrase I'm hungry", {
#     'entities': [(0,9,"FUNC"),(21,31,"PARAM")]
#     })
# ]
def restructure_phrase(phrase) :
    res = ""
    reading_entity = False
    reading_type = False
    entity_start = -1
    entity_stop = -1
    entity_type = ""
    entities = []
    for c in phrase :
        if c == '[' :
            reading_entity = True
            entity_start = len(res)
        elif c == ']' :
            reading_entity = False
            entity_stop = len(res)
        elif c == '(' :
            reading_type = True
        elif c == ')' :
            reading_type = False
            entities.append((entity_start, entity_stop, entity_type.upper()))
            entity_type = ""
        elif reading_type :
            entity_type += c
        else :
            res += c
    return (res, {'entities': entities})


TRAIN_DATA = []

f = open('ner_train.json')
data = json.load(f)

for i in data :
    print(i)
    TRAIN_DATA.append(restructure_phrase(i))

f.close()

print(TRAIN_DATA)

model = None
output_dir=Path("./output")
n_iter=100

#load the model

# if model is not None:
#     nlp = spacy.load(model)  
#     print("Loaded model '%s'" % model)
# else:
nlp = spacy.blank('en')  
print("Created blank 'en' model")

#set up the pipeline

if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner, last=True)
else:
    ner = nlp.get_pipe('ner')

for _, annotations in TRAIN_DATA:
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):  # only train NER
    optimizer = nlp.begin_training()
    for itn in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in tqdm(TRAIN_DATA):
            nlp.update(
                [text],  
                [annotations],  
                drop=0.5,  
                sgd=optimizer,
                losses=losses)
        print(losses)

# Test just because
for text, _ in TRAIN_DATA:
    doc = nlp(text)
    print('Entities', [(ent.text, ent.label_) for ent in doc.ents])

# Save model for later use
if output_dir is not None:
    output_dir = Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir()
    nlp.to_disk(output_dir)
    print("Saved model to", output_dir)
