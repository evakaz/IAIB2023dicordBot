"""A bot for IAIB2023 discord server."""
import discord
from Token import *
from datetime import date

TOKEN = Token.RETURN_TOKEN()
client = discord.Client(intents=discord.Intents.default())
current_date = date.today().strftime("%m/%d")
MESSAGE_ID = 1150070863002095617
CHANNEL_ID = 819582673592123473
user = client.user.id


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_reaction_add(reaction, user):
    channel = client.get_channel(CHANNEL_ID)
    if reaction.message.channel.id == channel.id:
        if reaction.emoji == "1️⃣":
            role = discord.utils.get(user.server.roles, name="IAIB11")
            await user.add_roles(role)
    return None

client.run(TOKEN)
