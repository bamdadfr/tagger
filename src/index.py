# general stuff
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
print('\n' + MY_PATH)

for folder in folders:

    print(('\n---\n')

    sleep()

    print((folder)
    print()

    files = File(folder)
    try:
        discogs = Discogs(files)
    except:
        discogs = None
    
    Tagger(files, discogs)

print('\n')