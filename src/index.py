# general stuff
from simple_chalk import chalk
import time

# tagging libraries
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3

# config and functions
from config import *
from utils import arrayToString

# classes
from Folder import Folder
from File import File
from Discogs import Discogs, sleep

# --- RUNTIME ---

folders = Folder(MY_PATH)
print ()

for folder in folders:

    sleep()

    print(chalk.green(folder))
    print()

    files = File(folder)
    # print(files)
    # print()

    discogs = Discogs(files)
    if discogs is None:
        print(chalk.red('No discogs URL specified, skipping...\n'))
        continue

    print(chalk.blue(discogs['json'].get('artists_sort') + ' - ' + discogs['json'].get('title')))
    print(chalk.blue(discogs['url']))
    print()

    label = discogs['json'].get('labels')[0]['name']
    date = discogs['json'].get('released')

    if date is None:
        date = ['1234/01/01']
    else:
        date = [date.replace('-', '/').replace('/00', '/01')]

    genres = arrayToString(discogs['json'].get('genres'))
    styles = arrayToString(discogs['json'].get('styles'))

    for file in files:
        file_extension = file.rsplit('.', 1)[1]

        if file_extension == 'flac':
            f = FLAC(file)

            f['organization'] = label
            f['composer'] = genres
            f['genre'] = styles
            f['date'] = date

            print(f['tracknumber'][0] + ' done')

            f.save()
        
        if file_extension == 'mp3':
            f = EasyID3(file)

            f['organization'] = label
            f['composer'] = genres
            f['genre'] = styles
            f['date'] = date

            print(f['tracknumber'][0] + ' done')

            f.save()

    print(chalk.yellow('\n---\n'))