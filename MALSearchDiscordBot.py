from env import *

import discord
import jikanFunctions
import userAnimeListShare
from discord.ext import commands


myIntents = discord.Intents.all()
bot = commands.Bot(intents = myIntents, command_prefix=['/', '!'])

@bot.event
async def on_ready():
    print(f"Bot {bot.user} has booted")

@bot.command(name="ohayo")
async def test_respond(ctx :discord.ext.commands.Context):
    print(f"Ohayo ohayo ohayo yo")


searchAnimeDescription = "Search anime on Mal, optionally specify how many (eg. searchAnime 'JJK' 3)"
@bot.command(name="search-anime", description=searchAnimeDescription)
async def simple_search(ctx :commands.Context, search_name, search_number=3):
    """
    Get top 3 search match results using an anime title
    """
    if search_name == None:
        await ctx.channel.send("Give me a name to search!")
        return
    if search_number > 10:
        await ctx.channel.send("I can only search upto 10 animes at once.")
        return
    jkSearcher = jikanFunctions.AnimeSearcher(search_name, False, search_number)
    lstOfEmbeds = jkSearcher.get_discord_embeds()

    for embed in lstOfEmbeds:
        await ctx.channel.send(embed=embed)



searchAnime_d_Description = "Get detailed information about the top search result using anime name (d stands for detailed)"
@bot.command(name="search-anime_d", description=searchAnime_d_Description)
async def detailed_search(ctx :commands.Context, search_name):
    """
    Get the top search match results using an anime title
    Show detailed information about it
    """
    if search_name == None:
        await ctx.channel.send("Give me a name to search!")
        return
    
    jkSearcher = jikanFunctions.AnimeSearcher(search_name, True, 1)
    lstOfEmbeds = jkSearcher.get_discord_embeds()
    for embed in lstOfEmbeds:
        await ctx.channel.send(embed=embed)


@bot.command(name="share-anime-list")
async def share_anime_list(ctx :commands.Context, username, limit = 3):
    """
    Get the top search match results using an anime title
    Show detailed information about it
    """
    if username == None:
        await ctx.channel.send("Give me a username to search!")
        return
    
    sharer = userAnimeListShare.UserAnimeListSharer(username, limit)
    lstOfEmbeds = sharer.get_discord_embeds()
    for embed in lstOfEmbeds:
        await ctx.channel.send(embed=embed)

bot.run(BOT_TOKEN)