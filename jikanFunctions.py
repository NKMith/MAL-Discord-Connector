from jikanpy import Jikan
import discord

"""
"" outside
'' inside
"""


class JikanSearcher():
    
    def __init__(self):
        self.jk = Jikan()


    #https://discordpy.readthedocs.io/en/stable/faq.html#local-image
    def grabSmallImage(self, anime):
        imgUrl = anime["images"]["jpg"]["small_image_url"]
        return imgUrl
    
    def grabLargeImage(self, anime):
        imgUrl = anime["images"]["jpg"]["large_image_url"]
        return imgUrl

    
    def search_get3anime(self, searchName :str):
        """
        Search MAL with inputted name
        Returns a list of 3 discord.Embed that each correspond to results of search
        Eahc discord.Embed has format of:
            url
            TITLE (Big text)
            Genre (Bolded)
            large_image
        """
        search_results = self.jk.search('anime', searchName)["data"] # TODO - raise errors

        embedList = []

        for i in range(3):
            anime = search_results[i]
            imageUrl = self.grabLargeImage(anime)
            link = anime['url']
            title = anime['title']

            txt = '# ' + title + '\n'

            genresStr = "Genres: " + self.get_genre_names_list_str(anime)
            txt += self.boldifyText(genresStr) + '\n'

            embed = discord.Embed(title=link, description=txt)
            embed.set_image(url=imageUrl)
            
            embedList.append(embed)

        return embedList
            

    def getGenreNamesList(self, anime):
        lst = []
        for genre in anime["genres"]:
            lst.append(genre["name"])
        return lst
    
    def get_genre_names_list_str(self, anime):
        lst = self.getGenreNamesList(anime)
        toRet = lst[0]
        for i in range(1, len(lst)):
            toRet += ", " + lst[i]
        return toRet

    
    def boldifyText(self, txt :str):
        return "**" + txt + "**"

    


# Function for briefly testing things
def main():
    jkS = JikanSearcher()
    jk = Jikan()

    res = jk.search(search_type='anime', query='gundam')
    #print(res)
    print(jkS.get_genre_names_list_str(res['data'][0]))

#main()

# Format:
# (search number) Title
# URL
# Image
# Synopsis (...)
# Rating


# Format:
# URL (as embed header)
# ## TITLE
# Image
# **Genre: [..]**
# Synopsis
# Rating