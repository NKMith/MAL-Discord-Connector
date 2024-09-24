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


    def searchOne(self, searchName :str):
        search_result = self.jk.search('anime', searchName) # TODO - raise errors
        return search_result["data"][0]
    
    def simpleSearch3(self, searchName :str):
        """
        Search MAL with inputted name
        Give out top 3 results
        """
        search_results = self.jk.search('anime', searchName) # TODO - raise errors

        embedList = []

        for i in range(3):
            anime = search_results[i]
            imageUrl = self.grabSmallImage(anime)
            link = anime['url']
            title = anime['title']

            txt = '# ' + title + '\n'
            txt += self.boldifyText(self.get_genre_names_list_str(anime)) + '\n'

            embed = discord.Embed(title=link)
            embed.set_image(imageUrl)
            
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

    
    def boldifyText(txt :str):
        return "**" + txt + "**"




    def get_formatted_str(self, anime :dict):
        toRet = f"## TITLE: {anime['title']}\n"
        toRet += f"# Synopsis: {anime['synopsis']}"
        return toRet
    


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