# general stuff
from simple_chalk import chalk
import time
import datetime

# config
from config import *

# classes
from Folder import Folder
from File import File
from Discogs import Discogs, sleep
from Tagger import Tagger

# --- RUNTIME ---

folders = Folder(MY_PATH)
# print(chalk.green('\n' + MY_PATH))

for folder in folders:

    print(chalk.yellow('\n---\n'))

    print(chalk.green(folder))
    print()

    files = File(folder)
    try:
        discogs = Discogs(files)
    except FileNotFoundError as err:
        print(chalk.red(err))
        continue

    if discogs == TAGGING_DONE:
        print(chalk.yellow(TAGGING_DONE))
        continue
    
    if discogs == TAGGING_TODO:
        print(chalk.yellow(TAGGING_TODO))
        continue

    Tagger(files, discogs)

print('\n')