from jikanpy import Jikan
import discord
from Anime import Anime

class Discord_MAL_Connector():
    def __init__(self, limit) -> None:
        """
        LIMIT: number of results to get
        """
        self.jk = Jikan()
        self.limit = limit

    def get_discord_embeds(self) -> list:
        """
        Each discord.Embed has basic format of:
            url
            TITLE (Big text)
            Genre (Bolded)
            large_image
        """
        list_of_animes = self.get_animes()
        list_of_embeds = []
        for i in range(self.limit):
            anime = list_of_animes[i]
            list_of_embeds.append(self.create_embed(anime))
        return list_of_embeds

    def get_animes(self) -> list:
        # Differs by funcitonality
        pass

    def create_embed(self, anime :Anime):
        title = self.create_embed_title_str(anime)
        description = self.create_embed_description_str(anime)
        image_url = self.get_embed_image_url(anime)
        embed = discord.Embed(title=title, description=description)
        embed.set_image(url=image_url)
        return embed

    def get_embed_image_url(self, anime :Anime):
        return anime.large_image_url
        
    def create_embed_title_str(self, anime :Anime):
        return anime.url

    def create_embed_description_str(self, anime :Anime):
        pass