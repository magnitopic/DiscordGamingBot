import discord
import os
from webServer import keep_alive

#my_secret = os.environ['TOKEN']

client = discord.Client()


@client.event
async def on_ready():
    print("We have loged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send('Hello!')

# Calls the keep_alive function form webServer.py
keep_alive()

# When using .env file:
# process.env.TOKEN
client.run(os.environ['TOKEN'])
