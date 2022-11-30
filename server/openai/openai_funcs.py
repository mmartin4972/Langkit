import openai
from key import api_key
#                  30 requests ~~ 0.03 cents

openai.api_key = api_key

def get_prompt_string(input):
    prompt = '''You are a teacher building a vocabulary list for your students on the topic "%s". You will generate perfectly formatted the following:

    1. Three complex sentences

    2. Three short sentences

    3. Three medium sentences

    4. Eight phrases'''

    return prompt % input

# TODO: We can do alot of stuff to properly configure this
def query_gpt3(query, n_in=1, max_tokens_in=236) :
    out = openai.Completion.create(
        model="text-davinci-003", # could also use text-cure-001 or any other models on this page (https://beta.openai.com/docs/models/gpt-3)
        prompt=get_prompt_string(query),
        n=n_in,
        max_tokens=max_tokens_in,
    )
    res = []
    for choice in out['choices'] :
        res.append(choice['text'])
    return res



#print(query_gpt3("dinner party"))

res = ['\n\n1. "Well behaved guests always make for an enjoyable dinner party," Julie remarked as her guests greeted one another warmly.\n2. The host had gone all out, decorating the house in gilded tablecloths and sumptuous spreads of food.\n3. Everyone was in awe of the stunning decorations and the delicate aromas from the kitchen that wafted through the air.\n\n1. Choosing the perfect menu.\n2. Gathering the guests.\n3. Setting the table.\n\n1. Preparing the food took up most of the day as the host tried to create the perfect culinary experience.\n2. The atmosphere was animated with people talking and laughing around the table.\n3. The host felt incredibly proud of the successful dinner party they had created.\n\n1. Planning the perfect party.\n2. Setting the right atmosphere.\n3. Crafting exquisite cuisine.\n4. Creating a stunning tablescape.\n5. Making sure the guests are comfortable.\n6. Ensuring there\'s enough food.\n7. Crafting the perfect playlist.\n8. Giving thanks to the guests.']

long = res[0]

print(long)

extracted = []
buildastring = ''
read_mode = False
for c in long:
    if read_mode:
        if c == '\n':
            read_mode = False
            extracted.append(buildastring)
            buildastring = ''
            continue
        buildastring += c
    elif c == ' ':
        read_mode = True

print(extracted)