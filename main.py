import discord
from constants import DISCORD_TOKEN
from api import requestIfWhale


def is_question(s):
    question_initiators = ("who", "what", "where", "when", "why", "how", "isnt", "isn't")
    

    starts_with_initiator = s.lower().startswith(question_initiators)
    
    contains_question_mark = "?" in s
    
    return starts_with_initiator or contains_question_mark

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == client.user:
            return
        if is_question(message.content):
            print("is a question")
            if requestIfWhale(message.content):
                await message.add_reaction('🐳')
            else:
                await message.reply("valid question")


intents = discord.Intents.all()

client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)