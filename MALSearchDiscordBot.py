""" 
Author: NKMith

"""
from env import *

import discord
import jikanFunctions
from discord.ext import commands


myIntents = discord.Intents.all()
bot = commands.Bot(intents = myIntents, command_prefix=['/', '!'])

@bot.event
async def on_ready():
    print(f"Bot {bot.user} has booted")

@bot.command(name="ohayo")
async def test_respond(ctx :discord.ext.commands.Context):
    print(f"Ohayo ohayo ohayo yo")

@bot.command(name="searchAnime")
async def simple_search(ctx :commands.Context, search_name, searchNumber=3):
    """
    Get top 3 search match results using an anime title
    """
    if search_name == None:
        await ctx.channel.send("Give me a name to search!")
        return
    jkSearcher = jikanFunctions.JikanSearcher()
    lstOfEmbeds = jkSearcher.search_getAnimes(search_name, searchNumber)

    for embed in lstOfEmbeds:
        await ctx.channel.send(embed=embed)

@bot.command(name="searchAnimeWithDetail")
async def detailed_search(ctx :commands.Context, search_name):
    """
    Get the top search match results using an anime title
    Show detailed information about it
    """
    if search_name == None:
        await ctx.channel.send("Give me a name to search!")
        return
    
    jkSearcher = jikanFunctions.JikanSearcher()
    lstOfEmbeds = jkSearcher.search_getAnimes(search_name, 1, True)
    for embed in lstOfEmbeds:
        await ctx.channel.send(embed=embed)



bot.run(BOT_TOKEN)