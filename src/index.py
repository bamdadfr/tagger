# general stuff
from simple_chalk import chalk
import time
import datetime

# tagging libraries
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TXXX
import mutagen

# config and functions
from config import *
from utils import arrayToString

# classes
from Folder import Folder
from File import File
from Discogs import Discogs, sleep

# --- RUNTIME ---

folders = Folder(MY_PATH)

for folder in folders:

    print(chalk.yellow('\n---\n'))

    sleep()

    print(chalk.green(folder))
    print()

    files = File(folder)
    # print(files)
    # print()

    discogs = Discogs(files)
    if discogs is None:
        print(chalk.red('No discogs URL specified, skipping...'))
        continue

    print(chalk.blue(discogs['json'].get('artists_sort') + ' - ' + discogs['json'].get('title')))
    print(chalk.blue(discogs['url']))
    print()

    # label
    label = discogs['json'].get('labels')[0]['name']

    # country
    country = discogs['json'].get('country')

    # date
    date = discogs['json'].get('released')

    if date is None:
        date = [str(datetime.datetime.now().year)]
    else:
        date = [date.replace('-', '/').replace('/00', '/01')]

    # genres
    genres = arrayToString(discogs['json'].get('genres'))
    
    # styles
    styles = arrayToString(discogs['json'].get('styles'))

    for file in files:
        file_extension = file.rsplit('.', 1)[1]

        if file_extension == 'flac':
            f = FLAC(file)

            f['organization'] = label
            f['composer'] = genres
            f['genre'] = styles
            f['date'] = date
            f['country'] = country

            f.save()

            print(f['tracknumber'][0] + ' done')
        
        if file_extension == 'mp3':
            f = EasyID3(file)

            f['organization'] = label
            f['composer'] = genres
            f['genre'] = styles
            f['date'] = date

            f.save()
            
            f2 = ID3(file)
            
            f2.add(TXXX(
                desc=u'country',
                text=[country],
            ))
            
            f2.save()

            print(f['tracknumber'][0] + ' done')

