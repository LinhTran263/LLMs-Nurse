import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
client = OpenAI(
    api_key = API_KEY #change your APIKEY in .env file
)

#change prompt here
prompt = "what is the capital of UAE?"

#you can read more documentation about the modification of this: https://platform.openai.com/docs/introduction
chat_completion = client.chat.completions.create(
    messages=[
        {
            "roles": "users",
            "content":prompt
        }
    ],
    model="gpt-3.5"
)

print(chat_completion.choices[0])