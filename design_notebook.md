# Jaseci Setup Docs

## Python Setup
- Requires python_version > 3.6
- pip install -r requirements.txt

## Docker Setup
1. docker pull mmartin4972/ubuntu20:langkit
2. docker run -dt -v ${pwd}:/jaseci -p 5000:5000 mmartin4972/ubuntu20:langkit
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
```python3 -wsgi.py```

## Launching to Heroku
- In order to get Heroku working properly the Procfile, wsgi.py, runtime.txt, and requirements.txt files had to be added
- The requirements.txt should only include requirements for the server code, since only the server code is running on Heroku
- Tensorflow Hub takes too much time to download the file. Consequently, I am going to upload the model directly to Heroku and then just read the file from memory

## Switching from use to use-lite
- Heroku server was running out of memory when using use
- By switching to use-lite memory constraints were able to be met and code base was easier to manage

## Switching to using Docker for Deployment
- Unfortunately, using the tensorflow-text caused my slug size to be over 500mb
- I am continually limited by this constraint and it is frustrating my use of interesting models
- Consequently I am going to transition the server to run entirely inside a Docker container so as to avoid this Slug size issue

## Switching to USE_Lite over Small_Bert
- Small Bert required preprocessing and did a far worse job at detecting word embedding similarity than use_lite did
- For these reasons I switched back to use_lite
- I could not use just normal universal sentence encoder since it took up too much memory

## Tensorflow Hub
- Tensorflow hub is a very cool site
- It has pre-trained models that let you solve complex ML tasks with incredibly limited amounts of knowledge about Tensorflow
- Tensorflow 2 is far easier to use than Tensorflow 1 and is far more intuitive. Do your best to always opt for Tensorflow 2 models
- Tensorflos library is very large, so make sure that you keep this in mind when developing

## Jaseci doc mistakes:
- *Modelling Behavior* under JAC Language overview is spelled wrong
    - b change to be
- *Modelling Structures*
    - ass to as
    - excetuable to executable
- *Register Sentinel* examples under action modules Jaseci actions is incorrect

## Google Translate API
- Google has Automatic Credential Detection
- It requires a CLI tool be installed on your local dev environment, and then uses the CLI to log you in and set the environment variables: https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev
- For Google translate you have to explicitly activate the API here: https://cloud.google.com/translate/docs/setup
- You have to have Billing enabled in order for the Cloud Translation API to work properly and do so by linking a Billing account
- Project ID: langkit-368114
- Need to enable Google IAM which supplies Service Accounts and then create key pair with service accounts for credentials
- This guide is really helpful for then creating service accounts and API keys: https://cloud.google.com/translate/docs/setup

## Newlines in Credential Files
- I was running into a serious issue when deploying to Heroku because Google sucks and don't just read their API key from an env variable but from a file
- To solve this problem I ended up following this article: https://www.yeti.co/blog/authorizing-google-cloud-platform-service-accounts-from-a-docker-container-running-in-heroku
- However, I didn't realize that in the process of echoing out the credential json from an environment variable to a file all of the newlines were being removed, and the newline characters are required in the private rsa key.
- To solve this problem I added an extra backslash in front of each of the \n, so that it wasn't rendered as a newline and so that all newlines in the actual private_key are not being filtered out
- https://unix.stackexchange.com/questions/164508/why-do-newline-characters-get-lost-when-using-command-substitution

## Adding Google Credentials
- To add Google credentials to your local environment, go to the Heroku application and copy the environment variable text into a local environment into an environment variable of the same name
- Run the translate/add-google-creds.sh file to create the credentials.json
- Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to point at credentials.json

## Running Google Translate locally
- export GOOGLE_APPLICATION_CREDENTIALS=/langkit/server/translate/google-credentials.json

## Running OpenAI locally
- set the OPENAI_KEY environment variable to the secret key value on Heroku

## Integrating OpenAI
- Simply utilize their python library
- Documentation can be found here: https://beta.openai.com/docs/api-reference/models/retrieve?lang=python
- The only tricky part is that you need to copy the environment variable in the Dockerfile during setup
- Can really fine tune the parameters of the completion endpoint here: https://beta.openai.com/docs/api-reference/completions
- The completion endpoint is what we want


