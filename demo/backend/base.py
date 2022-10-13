from flask import Flask, jsonify

api = Flask(__name__)

@api.route('/flashcards')
def default_pairs():
    response_body = {
        "words": "more words"
    }

    return response_body