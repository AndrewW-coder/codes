import discord
import math
from math import sqrt
from discord.ext import commands
import random
import os
import time
import wikipedia

#prefix
client = commands.Bot(command_prefix = ('yeet.', 'yeet ', 't.', 'no '))
#IDK
for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')
#startup
@client.event
async def on_ready():
    print("bot has connected to discord")
    game = discord.Game('Minecraft')
    await client.change_presence(status=discord.Status.idle, activity=game)

# @client.command()
# async def wiki(ctx, *, terms):
#     try:
#         searchterm = ' '.join(terms)
#         await ctx.send(wikipedia.summary(searchterm, sentences = 3))
#     except wikipedia.DisambiguationError:
#         await ctx.send('Try being more specific.')
    

#maths
@client.command()
async def add(ctx, a:int, b:int):
    await ctx.send(a + b)

@client.command()
async def multiply(ctx, a:int, b:int):
    await ctx.send(a * b)

@client.command()
async def subtract(ctx, a:int, b:int):
    await ctx.send(a - b)

@client.command()
async def divide(ctx, a:int, b:int):
    await ctx.send(a / b)

@client.command()
async def squarert(ctx, a:int):
    await ctx.send(sqrt(a))

@client.command()
async def square(ctx, a:int):
    await ctx.send(a ** 2)




@client.command()
async def eightball(ctx, a):
    l = ['It is certain',
 'It is decidedly so', 
 'Outlook good', 
 'Ask again later, you noob',
 'Better not tell you now', 
 "Don't count on it", 
 'my sources say no', 
 'Very doubtful',
 'What type of question is that?!',
 'How do you not know the answer?!',
 'Bruh']

    n = random.randint(0, len(l) - 1)
    await ctx.send(l[n]) 
    
@client.command()
async def say(ctx, *, sentence):
    await ctx.send(sentence)

@client.command()
async def fib(ctx, a : int):
    def fibbonacci(a):

        if a == 1:
            return 1

        old_num = 1
        new_num = 1
        
        for i in range (a - 2):
            
            current_num = old_num + new_num
            old_num = new_num
            new_num = current_num
            
        return current_num
    await ctx.send(fibbonacci(a))
    

@client.command()
async def spam(ctx, b:int, *, a):
    if b > 100:
        await ctx.send("Sorry, that is too much. (max is 100)")
    elif b < 1:
        await ctx.send("Sorry, that is too little.")
    else:
        await ctx.send((a + '\n') * b) 

@client.command(pass_context=True)
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")

@client.command(aliases = ["delete", "clear"])
async def purge(ctx, a:int):
    await ctx.channel.purge(limit = a + 1)

@client.command()
async def u(ctx):
    await ctx.send('no u')

@client.command()
async def embed(ctx, title, *, content):
    embed = discord.Embed(
        title = f'{title}',
        description = f'{title}',
        color = ctx.author.color
    )
    embed.add_field(name = '', value = f"{content}", inline = False)
    await ctx.send(embed = embed)
    


client.run('NzMxOTY0MDM0ODY1Mjk5NTM3.XwtsoQ.e4qi-CNSjtWVHk25KMzpO6cZU88')