# components
from discogs_sleep import DiscogsSleep

# packages
import requests
import json

def DiscogsGetReleaseFromMaster(master_id):
    DiscogsSleep()

    base_url = 'https://api.discogs.com/masters/'
    response = requests.get(base_url + master_id)
    response_json = json.loads(response.text)
    print(response.text)
    print(response_json)

    release_id = response_json['main_release_url'].rsplit('/', 1)[1]

    return release_id
