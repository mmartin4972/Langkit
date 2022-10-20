import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY", '-----')

model_options = [
    "text-davinci-001",
    "text-curie-001",
    "text-babbage-001",
    "text-ada-001"
]



gpt3_temperature = 0.4
gpt3_max_tokens = 64
gpt3_top_p = 1
gpt3_frequency_penalty = 0
gpt3_presence_penalty = 0



def get_gpt3_completion_response (prompt: str, model: int) -> str:
    return openai.Completion.create(
        model=model_options[model],
        prompt=prompt,
        temperature=gpt3_temperature,
        max_tokens=gpt3_max_tokens,
        top_p=gpt3_top_p,
        frequency_penalty=gpt3_frequency_penalty,
        presence_penalty=gpt3_presence_penalty
    )
