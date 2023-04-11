import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix = "/", intents = discord.Intents.all())


for file in os.listdir("./cogs"):
	if file.endswith(".py"):
		bot.load_extension("cogs." + file[:-3])  # removes .py

bot.run(os.getenv("TOKEN"))  # token in env file