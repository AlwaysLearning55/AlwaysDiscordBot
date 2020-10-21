import discord
from discord.ext import commands

    # Example of Cog. Just a vanilla cog without real purpose.

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Exemple.py loaded!')

    @commands.command()
    async def pong(self, ctx):
        await ctx.send('Ping.')

def setup(client):
    client.add_cog(Example(client))
