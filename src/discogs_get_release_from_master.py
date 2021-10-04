# components
from discogs_sleep import DiscogsSleep

# packages
import requests
import json
import logging
import traceback

def DiscogsGetReleaseFromMaster(master_id):
    DiscogsSleep()

    base_url = 'https://api.discogs.com/masters/'
    response = requests.get(base_url + master_id)
    response_json = json.loads(response.text)
    release_id = None

    try:
        release_id = response_json['main_release_url'].rsplit('/', 1)[1]
    except Exception as e:
        logging.error(traceback.format_exc())

    return release_id
