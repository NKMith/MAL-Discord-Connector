""" 
Author: NKMith

"""
from env import *

import discord
import jikanFunctions
from discord.ext import commands


myIntents = discord.Intents.all()
bot = commands.Bot(intents = myIntents, command_prefix=['!'])

@bot.event
async def on_ready():
    print(f"Bot {bot.user} has booted")

@bot.command(name="ohayo")
async def test_respond(ctx :discord.ext.commands.Context):
    print(f"Ohayo ohayo ohayo yo")

@bot.command(name="search")
async def search_anime(ctx :commands.Context, search_name):
    if search_name == None:
        await ctx.channel.send("Give me a name to search!")
        return
    jkSearcher = jikanFunctions.JikanSearcher()
    myStr = jkSearcher.searchTop3(search_name)
    await ctx.channel.send(myStr)

# @bot.command(name='test_image')
# async def test_image(ctx :commands.Context, search_name):
#     if search_name == None:
#         await ctx.channel.send("Give me a name to search!")
#         return
#     jkSearcher = jikanFunctions.JikanSearcher()
#     anime = jkSearcher.searchOne(search_name)
#     url = jkSearcher.grabImage(anime)
#     print(url)
#     embed = discord.Embed()
#     embed.set_image(url=url)

#     myStr = jkSearcher.searchTop3(search_name)

#     await ctx.channel.send(myStr, embed=embed)

@bot.command(name='test')
async def test_embed(ctx :commands.Context, search_name):
    if search_name == None:
        await ctx.channel.send("Give me a name to search!")
        return
    jkSearcher = jikanFunctions.JikanSearcher()
    anime = jkSearcher.searchOne(search_name)
    url = jkSearcher.grabImage(anime)
    myStr = jkSearcher.searchTop3(search_name)
    embed = discord.Embed(title="https://cdn.myanimelist.net/images/anime/4/78330l.jpg", description=myStr)
    embed.set_image(url="https://cdn.myanimelist.net/images/anime/4/78330l.jpg")

    await ctx.channel.send(embed=embed)


# **bold**
# # BIG
#

bot.run(BOT_TOKEN)