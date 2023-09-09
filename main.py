"""A bot for IAIB2023 discord server."""
import discord
from Token import *
from datetime import datetime
import gspread
from discord.ext import tasks

service_account = gspread.service_account()
sheet = service_account.open("test")
worksheet = sheet.worksheet("Sheet1")
TOKEN = Token.RETURN_TOKEN()
client = discord.Client(intents=discord.Intents.default())
BIRTHDAY_CHANNEL_ID = 819582673592123473


@client.event
async def on_ready():
    """Send a message when the bot is connected to discord."""
    print(f'{client.user} has connected to Discord!')
    parse_todays_birthday.start()


async def send_congratulations(name):
    birthday_channel = client.get_channel(BIRTHDAY_CHANNEL_ID)
    await birthday_channel.send(f"Happy birthday, {name}!")
    print("Sent")


@tasks.loop(seconds=1.0)
async def parse_todays_birthday():
    today_date = datetime.today().strftime("%m/%d")
    for i in range(2, 4):
        if worksheet.get("C" + str(i))[0][0] == today_date:
            birthday_name = worksheet.get("A" + str(i))[0][0]
            await send_congratulations(birthday_name)
    return


if __name__ == "__main__":
    client.run(TOKEN)
