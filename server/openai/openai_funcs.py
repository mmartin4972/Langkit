import openai
from key import api_key
#                  30 requests ~~ 0.03 cents

openai.api_key = api_key

# list engines
engines = openai.Engine.list()

# print the first engine's id
print(engines.data[17].id)

sentences = []

prompt = "complex sentence about running"

for _ in range(2):
    # create a completion
    completion = openai.Completion.create(engine="text-davinci-002", prompt=prompt)

    # print the completion
    sentences.append(completion.choices[0].text)

print(sentences)