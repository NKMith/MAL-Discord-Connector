from jikanpy import Jikan
import discord
from Anime import Anime
from Discord_MAL_Connector import Discord_MAL_Connector

class AnimeSearcher(Discord_MAL_Connector):
    """
    The 'main' class of MAL-Discord connector
    Uses JikanPy to search animes on MAL
    """
    
    def __init__(self, search_name, detailed = False, limit = 4):
        super().__init__(limit)
        self.search_name = search_name
        self.want_detailed_info = detailed

    def get_animes(self) -> list:
        search_results = self.jk.search('anime', self.search_name)["data"] # TODO - raise errors
        anime_list = []
        for obj in search_results:
            cur_anime = Anime(obj)
            anime_list.append(cur_anime)
        return anime_list

    def create_embed_description_str(self, anime :Anime):
        description = f"# {anime.title}" + '\n' + '\n'
        genresStr = f"**Genres: {anime.get_nice_print_genres()}**\n"
        description += genresStr

        if self.want_detailed_info:
            synopsis_str = "**Synopsis:** " + anime.synopsis + '\n'
            rating_str = f"**Score:** {anime.score}, rated by {anime.scored_by} users\n"
            description += synopsis_str + '\n' + rating_str

        return description
    
    

