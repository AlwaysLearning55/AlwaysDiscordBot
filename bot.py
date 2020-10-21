import discord
import random
import os

from discord.ext import commands

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print("Bot is Online!")

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Erro: {error}')

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f"Kickando {user.mention}!")

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"Banindo {user.mention}!")

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Desbanindo {user.mention}!")
            return

@client.command()
async def rickroll(ctx):
    await ctx.send("Você foi rickrollado!")

@client.command()
async def clear(ctx, amount = 3):
    await ctx.channel.purge(limit=amount)

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded extension [{extension}]!')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded extension [{extension}]!')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded extension [{extension}]!')

@client.command()
async def reloadall(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.unload_extension(f'cogs.{filename[:-3]}')
            client.load_extension(f'cogs.{filename[:-3]}')
    await ctx.send(f'Reloaded extensions!')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
async def rick(ctx):
    url = ("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    print(url)
    server = ctx.message.guild
    voice_channel = server.voice_client

    if voice_channel == None:
        await ctx.send(f"Usuário não está em um canal!")

@client.command(aliases = ['8ball', 'pergunta', '?'])
async def _8ball(ctx, *, question):
    responses = ['Até onde eu vi, sim.',
                 'Pergunta depois.',
                 'Vo vê e te conto.',
                 'Tá dificil prever isso.',
                 'Se concentra e pergunta de novo.',
                 'Se eu fosse você, não esperaria por isso.',
                 'Mais certo do que 2 + 2 = 4.',
                 'Difinitivamente, sim.',
                 'Mais errado que 2 + 2 = 5.',
                 'Definitivamente, não.',
                 'Olha... Não.',
                 'Nem fodendo.',
                 'Fodendo sim.',
                 'Cê quem sabe.',
                 'Até onde eu vejo, acho que sim.',
                 'Mais duvidoso do que produto do paraguai na 25 de março.',
                 'Sem sombra de dúvidas.',
                 'Sim.',
                 'Não.',
                 'Dá pra confiar que sim.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

fileOpen = os.open("C:\\Users\\AlwaysLWIN\\Documents\\AlwaysDiscordBOT\\Token.txt", os.O_RDONLY)
token = os.read(fileOpen, 59)
os.close(fileOpen)
tokenNew = str(token).split('\'')[1]
print(tokenNew)
client.run(f'{tokenNew}')
