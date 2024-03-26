from typing import Union

from mutagen.id3 import ID3, TXXX
from rich import print

from tagger.common.DiscogsRelease import DiscogsRelease
from tagger.config import Config
from tagger.constants import TAG_DONE, TAG_TODO
from tagger.file import File
from tagger.folder import Folder


class Updater:
    config: Config

    def __init__(
        self,
        config: Config,
    ) -> None:
        self.config = config

    def apply(
        self,
        folder: Folder,
        release: Union[DiscogsRelease, None],
    ) -> None:
        output = ""

        for file in folder.files:
            if file.type_ == "flac":
                output = self.__apply_flac(file, release)
                continue

            if file.type_ == "mp3":
                output = self.__apply_mp3(file, release)
                continue

        print(f"{output}\n")

    def __apply_flac(
        self,
        file: File,
        release: Union[DiscogsRelease, None],
    ) -> str:
        if release is None:
            file.meta["composer"] = TAG_TODO
            file.meta["genre"] = TAG_TODO
            file.meta["custom"] = TAG_TODO
            file.meta.save()

            return f"[yellow]{TAG_TODO}...[/yellow]"

        file.meta["date"] = release.date
        file.meta["composer"] = release.genres
        file.meta["genre"] = release.styles if release.styles is not None else TAG_TODO
        file.meta["organization"] = release.label
        file.meta["country"] = release.country
        file.meta["custom"] = f"{TAG_DONE} {release.url}"
        file.meta.save()

        return f"[green]{TAG_DONE}...[/green]"

    def __apply_mp3(
        self,
        file: File,
        release: Union[DiscogsRelease, None],
    ) -> str:
        tags = ID3(file.path)

        if release is None:
            file.meta["composer"] = TAG_TODO
            file.meta["genre"] = TAG_TODO
            file.meta.save()

            tags.add(TXXX(desc="custom", text=[TAG_TODO]))
            tags.save()

            return f"[yellow]{TAG_TODO}...[/yellow]"

        file.meta["date"] = release.date
        file.meta["composer"] = release.genres
        file.meta["genre"] = release.styles if release.styles is not None else TAG_TODO
        file.meta["organization"] = release.label
        file.meta.save()

        tags.add(TXXX(desc="country", text=[release.country]))
        tags.add(TXXX(desc="custom", text=[f"{TAG_DONE} {release.url}"]))
        tags.save()

        return f"[green]{TAG_DONE}...[/green]"
