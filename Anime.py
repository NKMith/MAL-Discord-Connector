class Anime():
    def __init__(self, animedict) -> None:
        self.animedict = animedict
        self.url = animedict['url']
        self.id = animedict['mal_id']
        self.title = animedict['title']
        self.large_image_url = animedict['images']['jpg']['large_image_url']
        self.genrenames :list = self.get_genre_list()

    def get_genre_list(self) -> list:
        """Given an anime, returns a Python list of genres it has"""
        lst = []
        for genre in self.animedict["genres"]:
            lst.append(genre["name"])
        return lst
    
    def get_nice_print_genres(self) -> str:
        """
        PRE: self.strgenres isn't empty
        Given an anime, returns a string of its genres nice to print
        """
        toRet = self.genrenames[0]
        for i in range(1, len(self.genrenames)):
            toRet += ", " + self.genrenames[i]
        return toRet
    


class Anime_UserList(Anime):
    def __init__(self, animedict, list_status, rank_in_user_list) -> None:
        super().__init__(animedict)
        self.user_score = list_status['score']
        self.status = list_status['status']
        self.rank_in_user_list = rank_in_user_list