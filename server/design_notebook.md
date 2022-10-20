# Jaseci Setup Docs

You only need to follow either the Python or Docker setup. Not necessary to do both.

## Python Setup
- Requires python_version > 3.6
- pip install -r requirements.txt

## Docker Setup
1. docker pull mmartin4972/ubuntu20:jaseci
2. docker run -dt -v ${pwd}:/jaseci mmartin4972/ubuntu20:jaseci
3. Attach visual studio code to docker container

## Named Entity Recognition or Sentence Encoding
- Jaseci enables you to perform 3 [nlp tasks](https://github.com/Jaseci-Labs/jaseci/blob/main/jaseci_ai_kit/README.md):
    - Sentence Encoding: Given 2 sentences can tell you how similar they are to each other
    - Named Entity Recognition: Given a sentence pull out predefined entities from the sentence
    - Summarization: Provided a body of text generate a summary of it
- We can make either sentence encoding or named entity recognition work for our purposes
- We are going to use named entity recognition, since sentence encoding is all pre-trained we won't learn as much if we use sentence encoding

## Training our Entity Extraction
- We are going to extract 2 entities from all sentences:
    - Function: What you want the application to do. This can be thought of as specifying a function to run.
    - Parameters: Parameters that configure how the action executes. This can be thought of as specifying the parameters we will use to run a function(action).
- Training data is in ner_train.json
- Run these commands to train:
    - ```jsctl```
    - ```actions load module jaseci_ai_kit.tfm_ner```
    - 
- [Example](https://github.com/Jaseci-Labs/jaseci/blob/main/examples/CanoniCAI/CCAI_codelab.md#train-an-entity-extraction-model)

## Switching From Jaseci
- I tried a bit to learn Jaseci, but the documentation is very lacking, and it abstracts many things away without explanation, so it is very hard to understand how to use them
- I am just going to use Python to create this server and some general python functions and models. Jaseci is too much of a pain
- I am going to switch to spacy since this is the first library that appeared online that is recommended for solving NER problems

## Spacy Setup
- https://spacy.io/usage/training
- Using spacy version 2.3.8 just because it is far easier to use than latest version of Spacy
- Train model: ```python3 train.py```

## Server Launch
```python3 -m flask --app main run```

## TODO:
- Use Sentence Encoding to make our entity extraction more flexible

## Jaseci doc mistakes:
- *Modelling Behavior* under JAC Language overview is spelled wrong
    - b change to be
- *Modelling Structures*
    - ass to as
    - excetuable to executable
- *Register Sentinel* examples under action modules Jaseci actions is incorrect

