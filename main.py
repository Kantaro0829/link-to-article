import os
import openai
#from IPython.display import display, Markdown
from dotenv import load_dotenv

load_dotenv()
  
OPEN_AI_API_KEY = os.getenv('API_KEY')
print(OPEN_AI_API_KEY)
#openai.api_key = os.environ["OPENAI"]
  