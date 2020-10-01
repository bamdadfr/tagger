# general stuff
import time
import datetime
import style

# config
from env import *

# classes
from Folder import Folder
from File import File
from Discogs import Discogs, sleep
from Tagger import Tagger

# --- RUNTIME ---

folders = Folder(ENV_PATHS)
# print(style.green('\n' + MY_PATH))

for folder in folders:

    print(style.yellow('\n---\n'))

    print(style.green(folder))
    print()

    files = File(folder)
    try:
        discogs = Discogs(files)
    except:
        print(style.red('some error happened...'))
        continue

    if discogs == ENV_TAGGING_DONE:
        print(style.yellow(ENV_TAGGING_DONE))
        continue
    
    if discogs == ENV_TAGGING_TODO:
        print(style.yellow(ENV_TAGGING_TODO))
        continue

    Tagger(files, discogs)

print('\n')