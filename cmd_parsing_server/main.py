import spacy

nlp = spacy.load("/langkit/cmd_parsing_server/spacy/output")

data = ["Generate me phrases about dinosaurs.",
        "Generate me phrases about food",
        "Generate me phrases regarding fish",
        "Generate stuff about corn",
        "Please generate me topics about a dinner party on a volcano"
        ]

# Just test because
for text in data:
    doc = nlp(text)
    print('Entities', [(ent.text, ent.label_) for ent in doc.ents])