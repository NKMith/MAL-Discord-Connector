from jikanpy import Jikan
import discord

class Discord_MAL_Connector():
    def __init__(self) -> None:
        self.jk = Jikan()

    def get_discord_embeds(self) -> list:
        list_of_animes = self.get_animes()
        list_of_embeds = []
        for anime in list_of_animes:
            list_of_embeds.append(self.create_embed(anime))
        return list_of_embeds

    def get_animes(self) -> list:
        # Differs by funcitonality
        pass

    def create_embed(self, anime):
        title = self.create_embed_title_str()
        description = self.create_embed_description_str()
        image_url = self.get_embed_image_url()
        embed = discord.Embed(title=title, description=description)
        embed.set_image(url=image_url)
        return embed

    def get_embed_image_url(self, anime):
        pass

    def create_embed_title_str(self):
        pass

    def create_embed_description_str(self):
        pass