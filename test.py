# https://github.com/abhinavk99/jikanpy?tab=readme-ov-file
from jikanpy import Jikan
import pprint
import json
jikan = Jikan()

search_result = jikan.search('anime', 'Gundam')
pprint.pprint(search_result["data"][0])


with open('animeobj_sample.txt', 'w') as file:
     file.write(json.dumps(search_result["data"][0], indent=4))