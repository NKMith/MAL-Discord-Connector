from jikanpy import Jikan
import discord

class JikanSearcher():
    """
    The 'main' class of MAL-Discord connector
    Uses JikanPy to search animes on MAL
    """
    
    def __init__(self):
        self.jk = Jikan()
    
    def search_getAnimes(self, searchName :str, resNum=3, detailed=False) -> discord.Embed:
        """
        Search MAL with inputted name
        Returns a list of 3 discord.Embed that each correspond to results of search
        Each discord.Embed has format of:
            url
            TITLE (Big text)
            Genre (Bolded)
            Synopsis (if detailed=True)
            Score (if detailed=True)
            large_image
        """
        search_results = self.jk.search('anime', searchName)["data"] # TODO - raise errors

        embedList = []

        for i in range(resNum):
            anime = search_results[i]
            imageUrl = self.grab_large_image(anime)
            link = anime['url']
            title = anime['title']

            description = f"# {title}" + '\n' + '\n'
            genresStr = f"**Genres: {self.get_genre_names_list_str(anime)}**\n"
            description += genresStr + '\n'

            if detailed:
                synopsis_str = "**Synopsis:** " + anime['synopsis'] + '\n'
                rating_str = f"**Score:** {anime['score']}, rated by {anime['scored_by']} users\n"
                description += synopsis_str + '\n' + rating_str

            embed = discord.Embed(title=link, description=description)
            embed.set_image(url=imageUrl)
            
            embedList.append(embed)

        return embedList
    

    def grab_small_image(self, anime):
        imgUrl = anime["images"]["jpg"]["small_image_url"]
        return imgUrl
    
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
