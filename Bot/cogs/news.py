import discord
import requests
from discord.ext import commands
import newsapi
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='fc8161efb13742f6a0e4a75c7b54dbab')
def setup(client):
    client.add_cog(News(client))

class News(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['News'])
    async def news(self, ctx):  
        url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=fc8161efb13742f6a0e4a75c7b54dbab')
        response = requests.get(url)
        a = response.json()
        info = a['articles']
        info = info[0]
        author = info['source']['name']
        title = info['title']
        embed = discord.Embed(
            title = title,
            description = info['description'] + '.',
            color = ctx.author.color
        )
        embed.add_field(name = 'Article', value = info['content'][:-13], inline = False)
        embed.set_image(url = info['urlToImage'])
        embed.add_field(name = 'Full story here', value = info['url'], inline = False)
        embed.set_footer(text = author)
        await ctx.send(embed = embed)