import requests
import discord
from Discord_MAL_Connector import Discord_MAL_Connector
from Anime import Anime_UserList
from env import *

# Can't use Jikan because getUserAnimeList was discontinued
class UserAnimeListSharer(Discord_MAL_Connector):
    def __init__(self, username, limit) -> None:
        super().__init__(limit)
        self.username = username

    def get_authorization_header(self):
        return {'X-MAL-CLIENT-ID': str(MAL_CLIENT_ID)}
    
    def get_query_parameters(self):
        # status, sort, limit, offset
        return {
            'limit' : self.limit,
            'sort' : 'list_score' #Highest to lowest
        }

    def get_animes(self):
        # https://myanimelist.net/apiconfig/references/api/v2#operation/users_user_id_animelist_get
        urlstr = f"https://api.myanimelist.net/v2/users/{self.username}/animelist?fields=list_status"
        request = requests.get(urlstr, params=self.get_query_parameters(), headers=self.get_authorization_header()).json()
        anime_list = []
        cur_rank = 1
        for obj in request["data"]:
            jikansearch = self.jk.anime(obj["node"]["id"])["data"]
            cur_anime = Anime_UserList(jikansearch, obj["list_status"], cur_rank)
            cur_rank += 1
            anime_list.append(cur_anime)
        return anime_list
    

    def create_embed_description_str(self, anime :Anime_UserList):

        description = f"# {anime.rank_in_user_list}. {anime.title}" + '\n' + '\n'
        genresStr = f"**Genres: {anime.get_nice_print_genres()}**\n"
        ratingByUser = f"Rating given by user: {anime.user_score}"
        description += genresStr
        description += ratingByUser

        return description
    
    
    
    

        

animesharer = UserAnimeListSharer("Ipari", 3)
animesharer.get_discord_embeds()



