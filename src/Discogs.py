import requests
import mutagen
import json

def getReleaseFromMaster(master_id):
    base_url = 'https://api.discogs.com/masters/'
    response = requests.get(base_url + master_id)
    response_json = json.loads(response.text)
    
    release_id = response_json['main_release_url'].rsplit('/', 1)[1]

    return release_id

def Discogs(files):
    # get json
    file = mutagen.File(files[0])
    base_url = 'https://api.discogs.com/releases/'

    print(file)

    url = file['custom'][0]
    id = url.rsplit('/', 1)[1]

    if '/master/' in url:
        id = getReleaseFromMaster(id)

    response = requests.get(base_url + id)
    
    return {
        'json': json.loads(response.text),
        'url': base_url + id,
    }