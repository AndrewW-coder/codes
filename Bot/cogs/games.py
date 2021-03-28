import discord
import requests
from discord.ext import commands
import aiohttp
import random
import html


def setup(client):
    client.add_cog(Games(client))


class Games(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.headers = {
            "User-Agent": "yeetbot",
            "Accept": "text/plain",
        }
    @commands.command()
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://icanhazdadjoke.com', headers = self.headers) as r:
                if r.status == 200:
                    result = await r.text()
                    result = result.encode("utf-8").decode("utf-8")
                    embed = discord.Embed(
                        title = ':rofl: funniez jokes :rofl:',
                        description = f"{result}",
                        colour = ctx.author.color                     
                    )
                    await ctx.send(embed=embed)  
    @commands.command()
    async def trivia(self, ctx):
        data = requests.get("https://opentdb.com/api.php?amount=1&type=multiple").json()
        results = data['results'][0]
        embed = discord.Embed(
            title = ":question: Trivia",
            description = f"Category: {results['category']} | Difficulty: {results['difficulty'].capitalize()}",
            color = ctx.author.color
        )
        pos = random.randint(0, 3)
        if pos == 3:
            answers = results['incorrect_answers'] + [results['correct_answer']]
        else:
            answers = results['incorrect_answers'][0:pos] + [results['correct_answer']] + results['incorrect_answers'][pos:]
        value = ''
        letters = ['a', 'b', 'c', 'd']
        for a in range(len(answers)):
            value += f"{letters[a].capitalize()}) {answers[a]}\n"
        
        embed.add_field(name = html.unescape(results['question']), value = value)
        embed2 = embed
        question = await ctx.send(embed = embed)
        available_commands = letters + [a.lower() for a in answers]
        def check(m):
            return m.channel == ctx.channel and m.content.lower() in available_commands
        try:
            msg = await self.client.wait_for('message', timeout = 20.0, check = check)
        except asyncio.TimeoutError:
            return
        answer_string = f"The answer was **{letters[pos].upper()}) {results['correct_answer']}**"
        if msg.content.lower() == letters[pos] or msg.content.lower() == results['correct_answer'].lower():
            name = ":white_check_mark:  Correct"
        else:
            name = ":x:  Incorrect"
        embed2.clear_fields()
        embed2.add_field(name = name, value = answer_string)
        await question.edit(embed = embed2)