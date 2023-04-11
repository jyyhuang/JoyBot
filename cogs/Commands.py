import discord
from discord.ext import commands
import asyncio

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  

    #event
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not member.id == self.bot.user.id:                       # checks if the bot triggers event
            return

        elif before.channel is None:                                # if None then that means bot was not in a voice channel before
            voice = after.channel.guild.voice_client
            time = 0
            while True:
                await asyncio.sleep(1)                              # sleeps for the time its not active
                time += 1
                if voice.is_playing() and not voice.is_paused():
                    time = 0
                if time == 900:
                    await voice.disconnect()
                if not voice.is_connected:                          # if not connected, break
                    break
            

    #commands
    @commands.command(pass_context = True)
    async def play(self, ctx):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("Please join a voice channel to use this command!")


    #@commands.command(pass_context = True)
    #async def pause():
    #    pass
    #@commands.command(pass_context = True)
    #async def stop():
    #    pass
    #@commands.command(pass_context = True)
    #async def skip():
    #    pass
    #@commands.command(pass_context = True)
    #async def list():
    #    pass

def setup(bot):
    bot.add_cog(Commands(bot))
