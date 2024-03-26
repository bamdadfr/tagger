from rich import print

from tagger.config import Config
from tagger.discogs import Discogs
from tagger.updater import Updater


def main():
    config = Config()
    discogs = Discogs(config)
    updater = Updater(config)

    for folder in config.folders:
        if folder.done is True:
            print(f'SKIP "{folder.path}"')
            continue

        release = discogs.search(folder)
        updater.apply(folder, release)

    print("\nFinished")
