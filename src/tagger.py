# components
from env import *
from tagger_write_none import TaggerWriteNone
from tagger_write_data import TaggerWriteData

# packages
import style

def Tagger(files, discogs):

    if discogs is None:
        TaggerWriteNone(files)
        return

    print(style.blue(discogs['json'].get('artists_sort') + ' - ' + discogs['json'].get('title')))
    print(style.blue(discogs['url']))
    print()

    TaggerWriteData(files, discogs)

    return
