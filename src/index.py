# components
from env import *
from folder import Folder
from file import File
from discogs import Discogs
from tagger import Tagger

# packages
import style
import logging
import traceback

folders = Folder(ENV_PATHS)
# print(style.green('\n' + MY_PATH))

for folder in folders:

    print(style.yellow('\n---\n'))

    print(style.green(folder))
    print()

    files = File(folder)
    try:
        discogs = Discogs(files)
    except Exception as e:
        print(style.red('some error happened...'))
        logging.error(traceback.format_exc())
        continue

    if discogs == ENV_TAGGING_DONE:
        print(style.yellow(ENV_TAGGING_DONE))
        continue
    
    if discogs == ENV_TAGGING_TODO:
        print(style.yellow(ENV_TAGGING_TODO))
        continue

    Tagger(files, discogs)

print('\n')