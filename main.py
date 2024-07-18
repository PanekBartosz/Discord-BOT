import discord
from discord.ext import commands

# Open the file in read mode
with open('./token.txt', 'r') as file:
    # Read the token from the file and strip any surrounding whitespace
    token = file.read().strip()

# Define the intents required for the bot to read messages and execute commands
intents = discord.Intents.default()
intents.message_content = True

# Create an instance of the Bot with a command prefix '!' and the specified intents
client = commands.Bot(command_prefix='!', intents=intents)

# Define an event when the bot is ready
@client.event
async def on_ready():
    print('BOT is ready for use!')

# Define a command 'hello' which can be invoked with the command prefix (e.g., !hello)
@client.command()
async def hello(ctx):
    await ctx.send('Hello, I am the BOT')

# Run the bot with the token read from 'token.txt'
client.run(token)
