import requests
import mutagen
import json

def Discogs(files):
    # get json
    audio_file = mutagen.File(files[0])
    discogs_id = audio_file['custom'][0].rsplit('/', 1)[1]

    discogs_api_base_url = 'https://api.discogs.com/releases/'

    response = requests.get(discogs_api_base_url + discogs_id)
    
    return {
        'json': json.loads(response.text),
        'url': discogs_api_base_url + discogs_id,
    }