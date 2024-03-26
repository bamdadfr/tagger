import os
from pathlib import Path
from typing import List

import yaml
from rich import print

from tagger.constants import FILE_TYPES
from tagger.folder import Folder


class Config:
    token: str
    paths: List[str]
    folders: List[Folder]

    def __init__(self) -> None:
        token, paths = self.__parse_yaml()

        self.token = token
        self.paths = paths
        self.folders = self.__get_folders()

    def __parse_yaml(self):
        cwd = os.getcwd()
        path = f"{cwd}/config.yaml"

        file = open(path)
        data = yaml.load(file, Loader=yaml.SafeLoader)
        file.close()

        docker = data["docker"]
        token = data["token"]

        if docker is True:
            paths = [f"/mount{p}" for p in data["paths"]]
        else:
            paths = data["paths"]

        return token, paths

    def __get_folders(self):
        paths = []

        for path in self.paths:
            for root, dirs, _ in os.walk(path, topdown=False):
                for dir in dirs:
                    if dir == ".AppleDouble":
                        continue

                    path = os.path.join(root, dir)
                    paths.append(path)

        paths.sort()
        print(f"[orange]{len(paths)} folders founds.[/orange]\n")

        folders: List[Folder] = []
        for path in paths:
            children = os.listdir(path)
            directory_is_empty = len(children) == 0

            if directory_is_empty is True:
                continue

            # if directory has no valid file types
            has_valid_files = False
            for child in children:
                suffix = Path(child).suffix
                if suffix in FILE_TYPES:
                    has_valid_files = True
                    break

            if has_valid_files is False:
                continue

            folders.append(Folder(path))

        return folders
