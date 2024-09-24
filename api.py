from openai import OpenAI
from constants import OPENROUTER_API_KEY, DISCORD_TOKEN

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENROUTER_API_KEY # make a file called constants.py to store the api key
)

def requestIfWhale(contentMessage):
  completion = client.chat.completions.create(
    extra_headers={
      "HTTP-Referer": "https://github.com/htauk",
      "X-Title": "Whaleinator",
    },
    model="deepseek/deepseek-chat",
    messages=[
      {
        "role": "system",
        "content": "You are an AI made to only say 'whale' or 'NO'. You are given questions. say whale if it's a stupid question, and NO if it's a good question. For example: 'how to I reenroll' say 'whale', 'how do I unenroll using bookmarklets' say 'whale' THIS IS IN A CHROMEBOOK HACKING CONTEXT. if they say 'how do i do this on so and so' its whale",
      },
      {
        "role": "user",
        "content": contentMessage,
      },
    ],
  )
  if completion.choices[0].message.content == "whale":
    return True
  else:
    return False

