# components
from env import *
from discogs_sleep import DiscogsSleep
from discogs_get_release_from_master import DiscogsGetReleaseFromMaster

# packages
import requests
import json
import mutagen
from mutagen.mp3 import MP3

def Discogs(files):
    # get json
    discogs_api_base_url = 'https://api.discogs.com/releases/'
    file_extension = files[0].rsplit('.', 1)[1]

    # logics by extensions
    # FLAC
    if file_extension == 'flac':
        file = mutagen.File(files[0])

        if file.get('custom') is None:
            return None

        if file.get('custom')[0][:4] == ENV_TAGGING_DONE:
            return ENV_TAGGING_DONE
        
        if file.get('custom')[0][:4] == ENV_TAGGING_TODO:
            return ENV_TAGGING_TODO
        
        discogs_url = file.get('custom')[0]
        discogs_slug = discogs_url.rsplit('/', 1)[1]
        discogs_id = discogs_slug.split('-', 1)[0]

    # MP3
    elif file_extension == 'mp3':
        file = MP3(files[0])

        if file.get('TXXX:Custom') is None:
            return None
        
        if str(file.get('TXXX:Custom'))[:4] == ENV_TAGGING_DONE:
            return ENV_TAGGING_DONE
        
        if str(file.get('TXXX:Custom'))[:4] == ENV_TAGGING_TODO:
            return ENV_TAGGING_TODO
        
        discogs_url = str(file.get('TXXX:Custom'))
        discogs_id = discogs_url.rsplit('/', 1)[1]

    # logics if discogs/master
    if '/master/' in discogs_url:
        discogs_id = DiscogsGetReleaseFromMaster(discogs_id)

    DiscogsSleep()
    
    response = requests.get(discogs_api_base_url + discogs_id)
    
    return {
        'json': json.loads(response.text),
        'url': discogs_api_base_url + discogs_id,
    }