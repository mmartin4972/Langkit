import os
import openai
openai.api_key = os.getenv("OPENAI_KEY")
res = openai.Completion.create(
  model="text-davinci-002", # could also use text-cure-001 or any other models on this page (https://beta.openai.com/docs/models/gpt-3)
  prompt="Generate phrases about winter",
  n=5,
  max_tokens=20,
)
print(res)