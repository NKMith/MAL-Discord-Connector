import requests

# Can't use Jikan because getUserAnimeList was discontinued
class userAnimeListShare():
    def __init__(self, username) -> None:
        self.username = username

    def get_request(self):
        # curl 'https://api.myanimelist.net/v2/users/@me/animelist?fields=list_status&limit=4' \
        # -H 'Authorization: Bearer YOUR_TOKEN'

        # https://myanimelist.net/apiconfig/references/api/v2#operation/users_user_id_animelist_get

        request = requests.get(f"https://api.myanimelist.net/v2/users/{self.username}/animelist?fields=list_status&limit=4")
        return request.json()
    



