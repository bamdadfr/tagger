# components
from env import *

# packages
import style
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3

def TaggerWriteNone(files):

    print(style.red(ENV_ERROR_DISCOGS_NULL))

    for file in files:
        try:
            file_extension = file.rsplit('.', 1)[1]
            f = None

            if file_extension == 'flac':
                f = FLAC(file)
            
            if file_extension == 'mp3':
                f = EasyID3(file)

            f['custom'] = ENV_TAGGING_TODO

            f.save()
            
            print(f['tracknumber'][0] + ' done')
        except:
            print(style.red(ENV_ERROR_TAGGING))
            continue

