"""A bot for IAIB2023 discord server."""
import discord
from Token import *
import asyncio
from datetime import datetime, time, timedelta

TOKEN = Token.RETURN_TOKEN()
client = discord.Client(intents=discord.Intents.default())
MESSAGE_ID = 1150070863002095617
CHANNEL_ID = 819582673592123473
BIRTHDAY_CHANNEL_ID = 819582673592123473
# user = client.user.id
SERVER_ID = 813828150098133022
server = client.get_guild(SERVER_ID)
WHEN = time(8, 0 ,0)


@client.event
async def on_ready():
    """"Send a message when the bot is connected to discord."""
    print(f'{client.user} has connected to Discord!')

today_birthday_names = ""
def parse_todays_birtday():
    today_date = datetime.today().strftime("%m/%d")
    # for i in sheets:
    #     if today_date == parsed_birtday():
    #         today_birthday_names += parsed_name
    # return today_birthday_names


async def called_once_a_day():  # Fired every day
    await client.wait_until_ready()  # Make sure your guild cache is ready so the channel can be found via get_channel
    channel = client.get_channel(BIRTHDAY_CHANNEL_ID) # Note: It's more efficient to do bot.get_guild(guild_id).get_channel(channel_id) as there's less looping involved, but just get_channel still works fine
    await channel.send(f"Happy birthday, {today_birthday_names}!")


async def background_task():
    now = datetime.now()
    if now.time() > WHEN:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
        await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start
    while True:
        now = datetime.now() # You can do now() or a specific timezone if that matters, but I'll leave it with utcnow
        target_time = datetime.combine(now.date(), WHEN)  # 6:00 PM today (In UTC)
        seconds_until_target = (target_time - now).total_seconds()
        await asyncio.sleep(seconds_until_target)  # Sleep until we hit the target time
        await called_once_a_day()  # Call the helper function that sends the message
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
        await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start a new iteration


@client.event
async def on_reaction_add(reaction, payload): # Finish implementation later.
    """Add role to a user when react to the message."""
    member = payload.member
    channel = client.get_channel(CHANNEL_ID)
    if reaction.message.channel.id == channel.id:
        if reaction.emoji == "1️⃣":
            role = discord.utils.get(member, name="IAIB11")
            await member.add_roles(role)
    return None


if __name__ == "__main__":
    client.loop.create_task(background_task())
    client.run(TOKEN)
