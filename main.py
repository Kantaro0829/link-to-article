import os
import openai
from IPython.display import display, Markdown
from dotenv import load_dotenv

load_dotenv()
  
OPEN_AI_API_KEY = os.getenv('API_KEY')
print(OPEN_AI_API_KEY)
openai.api_key = OPEN_AI_API_KEY



response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)

print(response['choices'][0]['message']['content'])