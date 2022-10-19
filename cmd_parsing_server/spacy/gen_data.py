import spacy
from spacy.tokens import DocBin

nlp = spacy.blank("en")
training_data = [
    ("generate me phrases about dinner parties ontop of volcanoes",[(0,19, "func"),(26, 59, "params")]),
    ("generate phrases for running a marathon",[(0,16,"func"),(21,39,"params")]),
    
    ("generate me words about dinner parties ontop of volcanoes",[(0,17,"func"),(24,57,"params")]),
    ("generate vocabulary for running a marathon(params)",[(0,19,"func"),(24,42,"params")]),

    ("translate the phrase I'm hungry",[(0,9,"func"),(21,31,"params")])
]

# the DocBin will store the example documents
db = DocBin()
for text, annotations in training_data:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations:
        span = doc.char_span(start, end, label=label)
        ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./train.spacy")