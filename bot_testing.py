from discord import message
from discord.ext import tasks
from dotenv.main import load_dotenv
from discord.ext import commands, tasks

import os

load_dotenv()
discord_key = os.getenv("KEY")


bot = commands.Bot("!listen")

target_channel_id = 702248031898173480

@tasks.loop(seconds=5)
async def called_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    #print(f"Got channel {message_channel}")
    await message_channel.send("Test Message")

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()
bot.run(discord_key)