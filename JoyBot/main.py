import discord # pip install
from discord.ext import commands
import os
from dotenv import load_dotenv # pip install

load_dotenv()

# Since I am using discord.py v2.0 I had to create a subclass of commands.Bot for setup hook to my cog
# super().__init__ calls class commands.Bot to pass in command_prefix and intents
class MyBot(commands.Bot): 			
	def __init__(self):
		super().__init__(command_prefix = "/", intents = discord.Intents.all())		

	async def setup_hook(self):
		await self.load_extension("cogs.Commands")

JoyBot = MyBot()

JoyBot.run(os.getenv("TOKEN"))  # token in env file