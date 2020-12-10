import os
import discord
import logging

LOG = logging.getLogger()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    LOG.info("Started")


@client.event
async def on_message(message):
    LOG.info(f"{message.author}: {message.content}")

client.run(TOKEN)
