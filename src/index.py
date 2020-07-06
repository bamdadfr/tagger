from simple_chalk import chalk
from mutagen.flac import FLAC

from config import *
from utils import arrayToString

from Folder import Folder
from File import File
from Discogs import Discogs

# --- RUNTIME ---

folders = Folder(MY_PATH)
print ()

for folder in folders:
    print(chalk.green(folder))
    print()

    files = File(folder)
    # print(files)
    # print()

    discogs = Discogs(files)
    print(chalk.blue(discogs['json']['artists_sort'] + ' - ' + discogs['json']['title']))
    print(chalk.blue(discogs['url']))
    print()

    label = discogs['json']['labels'][0]['name']
    date = [discogs['json']['released'].replace('-', '/').replace('/00', '/01')]
    genres = arrayToString(discogs['json']['genres'])
    styles = arrayToString(discogs['json']['styles'])

    for file in files:
        f = FLAC(file)
        
        f['organization'] = label
        f['composer'] = genres
        f['genre'] = styles
        f['date'] = date

        print(f['tracknumber'][0] + ' done')

        f.save()

    print(chalk.yellow('\n---\n'))