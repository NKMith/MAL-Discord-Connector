import requests
import discord
from jikanpy import Jikan
from env import *

# Can't use Jikan because getUserAnimeList was discontinued
class userAnimeListShare():
    def __init__(self, username) -> None:
        self.username = username
        self.jk = Jikan()

    def get_authorization_header(self):
        return {'X-MAL-CLIENT-ID': str(MAL_CLIENT_ID)}
    
    def get_query_parameters(self, limit):
        # status, sort, limit, offset
        return {
            'limit' : limit,
            'sort' : 'list_score' #Highest to lowest
        }

    def get_request(self, resNum):
        # https://myanimelist.net/apiconfig/references/api/v2#operation/users_user_id_animelist_get
        urlstr = f"https://api.myanimelist.net/v2/users/{self.username}/animelist?fields=list_status"
        request = requests.get(urlstr, params=self.get_query_parameters(resNum), headers=self.get_authorization_header())
        
        #TODO - handle when username doesnt exist
        return request.json()
    
    # def get_list_of_jikan_animes(self) -> list: # list of dictionaries
    #     toRet = []
    #     nodes = self.get_request()['data']
    #     for node in nodes:
    #         id = node['node']['id']
    #         animeDict = self.jk.anime(id=id)
    #         toRet.append(animeDict)
    #     return toRet

    def get_embeds(self, resNum = 3):
        datalist = self.get_request(resNum)['data']
        embedList = []
        for i in range(resNum):
            anime = datalist[i]
            jikan_anime = self.jk.anime(anime['node']['id'])['data']
            #print(jikan_anime)
            imageUrl = self.grab_large_image(jikan_anime)
            link = jikan_anime['url']
            title = jikan_anime['title']

            description = f"# {title}" + '\n' + '\n'
            genresStr = f"**Genres: {self.get_genre_names_list_str(jikan_anime)}**\n"
            ratingByUser = f"Rating given by user: {anime['list_status']['score']}"

            description += genresStr
            description += ratingByUser


            embed = discord.Embed(title=link, description=description)
            embed.set_image(url=imageUrl)
            
            embedList.append(embed)

        return embedList
    
    def grab_large_image(self, anime):
        imgUrl = anime["images"]["jpg"]["large_image_url"]
        return imgUrl
    
    def get_genre_names_list_str(self, anime) -> str:
        "Given an anime, returns a string of its genres"
        lst = self.get_genre_names_list(anime)
        toRet = lst[0]
        for i in range(1, len(lst)):
            toRet += ", " + lst[i]
        return toRet
    
    def get_genre_names_list(self, anime) -> list:
        "Given an anime, returns a Python list of genres it has"
        lst = []
        for genre in anime["genres"]:
            lst.append(genre["name"])
        return lst
    
    
    

        

    



