import requests
from env import *

# Can't use Jikan because getUserAnimeList was discontinued
class userAnimeListShare():
    def __init__(self, username) -> None:
        self.username = username

    def get_authorization_header(self):
        return {'X-MAL-CLIENT-ID': str(MAL_CLIENT_ID)}
    
    def get_query_parameters(self):
        return {
            'limit' : 10,
            'sort' : 'list_score'
        }
    
        # status, sort, limit, offset

    def get_request(self):
        # https://myanimelist.net/apiconfig/references/api/v2#operation/users_user_id_animelist_get
        urlstr = f"https://api.myanimelist.net/v2/users/{self.username}/animelist"
        request = requests.get(urlstr, params=self.get_query_parameters(), headers=self.get_authorization_header())
        return request.json()
    



