import spacy
from spacy.tokens import DocBin

nlp = spacy.blank("en")
training_data = [
  ("Generate me phrases about dinosaurs.", [(0, 19, "FUNC"),(26, 35, "PARAM")]),

  ("translate the phrase I'm hungry",[(0,9,"FUNC"),(21,31,"PARAM")])
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
