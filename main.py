import discord
from discord.ext import commands
from api_keys import SERVER_TOKEN
import requests
import json

# Define the intents required for the bot to read messages and execute commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create an instance of the Bot with a command prefix '!' and the specified intents
client = commands.Bot(command_prefix='!', intents=intents)

# Define an event when the bot is ready
@client.event
async def on_ready():
    print('BOT is ready for use!')

# Define a command 'hello/goodbye' which can be invoked with the command prefix (e.g., !hello)
@client.command()
async def hello(ctx):
    await ctx.send('Hello, I am the BOT')

@client.command()
async def goodbye(ctx):
    await ctx.send('Goodybye, hope you come back soon')

# Define an event handler 'on_member_join' which can be invoked when new member join server
# It sends a welcome message along with a joke to a specified channel
@client.event
async def on_member_join(member):

    jokeurl = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"

    response = requests.get(jokeurl)
    response_json = response.json()

    if 'joke' in response_json:
        joke = response_json['joke']
    else:
        joke = 'I could not fetch a joke at the moment.'

    channel = client.get_channel(315541123781099520)
    await channel.send(f'Hello, {member.display_name}! Welcome to the server. Here is a joke for you:')
    await channel.send(joke)

# Run the bot with the token read from 'token.txt'
client.run(SERVER_TOKEN)
