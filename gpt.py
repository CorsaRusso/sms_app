import openai
import os
from dotenv import load_dotenv

load_dotenv()

def gpt_search(prompt):
    openai.api_key = os.environ['OPEN_AI']

    response = openai.Completion.create(
        engine="text-davinci-001", 
        prompt=prompt, 
        max_tokens=100)

    return(response.choices[0].text)

