# components
from env import *

# packages
import time
import style

def DiscogsSleep():
    prefix = 'discogs api call: '
    print(prefix + style.yellow('sleeping...'))
    time.sleep(60 / ENV_DISCOGS_MAX_RATE)
    print(prefix + style.yellow('go!') + '\n')