import os
from pathlib import Path

from rich import print
from tagger.constants import FILE_TYPES
from tagger.file import File


class Folder:
    path: str
    count: int
    done: bool

    def __init__(self, path: str) -> None:
        print(path)
        self.path = path
        self.files = self.__get_files()
        self.count = len(self.files)
        self.done = self.__compute_done()

    def __get_files(self):
        paths = []

        for root, _, files in os.walk(self.path, topdown=False):
            for name in files:
                suffix = Path(name).suffix

                if suffix in FILE_TYPES:
                    paths.append(os.path.join(root, name))

        paths.sort()
        files = [File(p) for p in paths]
        return files

    def __compute_done(self) -> bool:
        done = True

        for file in self.files:
            if file.done is False:
                done = False
                break

        return done
