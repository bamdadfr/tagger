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
print(chalk.green('\n' + MY_PATH))

for folder in folders:

    print(chalk.yellow('\n---\n'))

    sleep()

    print(chalk.green(folder))
    print()

    files = File(folder)
    try:
        discogs = Discogs(files)
    except:
        discogs = None
    
    Tagger(files, discogs)

print('\n')