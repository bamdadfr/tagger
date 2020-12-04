# components
from env import *
from utils_array_to_string import UtilsArrayToString

# packages
import style
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TXXX

def TaggerWriteData(files, discogs):

    # label
    label = discogs['json'].get('labels')[0]['name']

    # country
    country = discogs['json'].get('country')

    if country is None:
        country = ''

    # date
    date = discogs['json'].get('released')

    if date is not None:
        date = [date.replace('-', '/').replace('/00', '/01')]

    # genres
    genres = UtilsArrayToString(discogs['json'].get('genres'))
    
    # styles
    styles = UtilsArrayToString(discogs['json'].get('styles'))

    for file in files:
        try:
            file_extension = file.rsplit('.', 1)[1]

            if file_extension == 'flac':
                f = FLAC(file)

                f['organization'] = label
                f['composer'] = genres
                f['genre'] = styles
                if date is not None: f['date'] = date
                f['country'] = country
                f['custom'] = ENV_TAGGING_DONE + ' ' + f['custom'][0]

                f.save()

                print(f['tracknumber'][0] + ' done')
            
            if file_extension == 'mp3':
                f = EasyID3(file)

                f['organization'] = label
                f['composer'] = genres
                f['genre'] = styles
                if date is not None: f['date'] = date

                f.save()
                
                f2 = ID3(file)

                f2.add(TXXX(
                    desc=u'country',
                    text=[country],
                ))

                f2.add(TXXX(
                    desc=u'Custom',
                    text=[str(ENV_TAGGING_DONE + ' ' + str(f2.get('TXXX:Custom')))]
                ))
                
                f2.save()

                print(f['tracknumber'][0] + ' done')
        except:
            print(style.red(ENV_ERROR_TAGGING))
            continue
