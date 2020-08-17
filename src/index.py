# general stuff
from simple_chalk import chalk
import time
import datetime

# config
from env import *

# classes
from Folder import Folder
from File import File
from Discogs import Discogs, sleep
from Tagger import Tagger

# --- RUNTIME ---

folders = Folder(ENV_PATHS)
# print(chalk.green('\n' + MY_PATH))

for folder in folders:

    print(chalk.yellow('\n---\n'))

    print(chalk.green(folder))
    print()

    files = File(folder)
    try:
        discogs = Discogs(files)
    except:
        print(chalk.red('some error happened...'))
        continue

    if discogs == ENV_TAGGING_DONE:
        print(chalk.yellow(ENV_TAGGING_DONE))
        continue
    
    if discogs == ENV_TAGGING_TODO:
        print(chalk.yellow(ENV_TAGGING_TODO))
        continue

    Tagger(files, discogs)

print('\n')