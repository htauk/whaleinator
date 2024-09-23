from openai import OpenAI
from constants import OPENROUTER_API_KEY

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENROUTER_API_KEY # make a file called constants.py to store the api key
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "https://github.com/htauk",
    "X-Title": "Whaleinator",
  },
  model="deepseek/deepseek-chat",
  messages=[
    {
      "role": "user",
      "content": "Say this is a test",
    },
  ],
)
print(completion.choices[0].message.content)