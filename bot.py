import discord
import requests
import os
import json
from dotenv import load_dotenv, find_dotenv
from requests.api import get
from webServer import keep_alive

#my_secret = os.environ['TOKEN']

client = discord.Client()
load_dotenv(find_dotenv())


@client.event
async def on_ready():
    print("We have loged in as {0.user}".format(client))


def get_apod():
    # When using .env file:
    # os.getenv('API_TOKEN')
    resp = requests.get(
        "https://api.nasa.gov/planetary/apod?api_key=" + os.environ['API_TOKEN'])
    content = json.loads(resp.content)
    #print(content)     Prints all the JSON


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send('Hello!')
    elif message.content.startswith("$apod") or message.content.startswith("$APOD"):
        get_apod()

# Calls the keep_alive function form webServer.py
keep_alive()

# When using .env file:
# os.getenv('BOT_TOKEN')
client.run(os.getenv('BOT_TOKEN'))  # os.environ['BOT_TOKEN'])
