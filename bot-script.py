#Written by the most talented programmer in the world, Kirieshka.
import discord
from discord.ext import commands, tasks
import random as rd
# Importing libraries

client = commands.Bot(command_prefix='.')
prohibited_words = ['kys','fuck', 'dick', 'bitch', 'faen', 'jævel', 'mongo', 'sug meg', 'homse', 'nigger', 'nigga', 'homs', 'pussy', 'cock', 'pedo' ]
responces = ['din jævla neger', 'homsefaen']


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Pornhub'))
    channel = client.get_channel(500270127229698070)
    await channel.send("yes daddy uzi")
    print('Logged in as {0.user}'.format(client))


@client.command()
async def members(message):
    await message.channel.send(message.guild.members)


@client.event
async def on_message(message):
    channel = client.get_channel(500270127229698070)
    if 'daddy uzi' in message.content.lower():
        await message.channel.send(responces[rd.randint(0,1)])
    if message.author == client.user:
        return
    if message.author.bot: return
        print(message.author, '{0.user}'.format(client))
        print(message.content, message.author)
        for i in prohibited_words:
            if i in message.content.lower():
                await auto_kick(message.author)
                await clear(message, 1)
                await channel.send(f'{message.author.mention} was a whiny bitch')
        await client.process_commands(message)
# Cheking the message for prohibited words

@client.command()
@commands.has_role('Admin')
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    print('fuck you')


@client.command()
@commands.has_role('Admin')
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} got shiton')


@client.command()
async def auto_kick(member: discord.Member):
    await member.kick()


@client.command()
@commands.has_role('Admin')
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} got fucked')

@client.command()
async def rules(ctx):
    await ctx.send('ver toxic mot usman')

@client.command()
async def spam(ctx):
    for i in range(20):
        await ctx.send('Nigger')

@client.command()
async def send(ctx, message):
    channel = client.get_channel(500270127229698070)
    await channel.send(message)

@client.command()
@commands.has_role('Admin')
async def shutdown(ctx):
    await ctx.bot.logout()


client.run('')
