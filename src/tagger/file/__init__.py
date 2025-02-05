from pathlib import Path
from typing import List, Union

from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.id3 import ID3, ID3NoHeaderError
from mutagen.mp3 import MP3
from typing_extensions import Literal

from tagger.constants import SEPARATOR, TAG_DONE, TAG_TODO

Type = Literal["flac", "mp3"]


class File:
    path: str
    type_: Type
    meta: Union[FLAC, EasyID3]
    __track_number: List[str]
    __artists: List[str]
    __name: List[str]
    __album: List[str]
    __album_artist: List[str]
    __date: List[str]
    __genres: List[str]  # we save this in composer
    __styles: List[str]  # we save this in genre
    __publisher: List[str]
    __country: List[str]
    __custom: List[str]  # state + discogs URL

    def __init__(
        self,
        path: str,
    ) -> None:
        self.path = path
        self.type_ = self.__get_type()
        self.meta = self.__get_meta()  # type: ignore
        self.__get_tags()

    def __get_type(self) -> Type:
        suffix = Path(self.path).suffix

        if suffix == ".mp3":
            return "mp3"
        if suffix == ".flac":
            return "flac"

        raise Exception("File type not supported")

    def __get_meta(self):
        if self.type_ == "flac":
            return FLAC(self.path)
        if self.type_ == "mp3":
            try:
                return EasyID3(self.path)
            except ID3NoHeaderError:
                audio = MP3(self.path)
                audio.add_tags()
                audio.save()
                return EasyID3(self.path)

        raise Exception("File type not supported")

    def __get_tags(self):
        self.__track_number = (
            self.meta["tracknumber"] if "tracknumber" in self.meta else [""]
        )

        self.__artists = self.meta["artist"] if "artist" in self.meta else [""]
        self.__name = self.meta["title"] if "title" in self.meta else [""]
        self.__album = self.meta["album"] if "album" in self.meta else [""]

        self.__album_artist = (
            self.meta["albumartist"] if "albumartist" in self.meta else [""]
        )

        self.__date = self.meta["date"] if "date" in self.meta else [""]
        self.__genres = self.meta["composer"] if "composer" in self.meta else [""]
        self.__styles = self.meta["genre"] if "genre" in self.meta else [""]

        self.__publisher = (
            self.meta["organization"] if "organization" in self.meta else [""]
        )

        if self.type_ == "flac":
            self.__country = self.meta["country"] if "country" in self.meta else [""]
            self.__custom = self.meta["custom"] if "custom" in self.meta else [""]

        if self.type_ == "mp3":
            mp3_tags = ID3(self.path)
            mp3_country = mp3_tags.get("TXXX:country")
            mp3_custom = mp3_tags.get("TXXX:custom")

            self.__country = [str(mp3_country)] if mp3_country is not None else [""]
            self.__custom = [str(mp3_custom)] if mp3_custom is not None else [""]

    @property
    def track_number(self) -> str:
        return SEPARATOR.join(self.__track_number)

    @property
    def artists(self) -> List[str]:
        return self.__artists

    @property
    def name(self) -> str:
        return SEPARATOR.join(self.__name)

    @property
    def album(self) -> str:
        return SEPARATOR.join(self.__album)

    @property
    def album_artist(self) -> str:
        return SEPARATOR.join(self.__album_artist)

    @property
    def date(self) -> str:
        return SEPARATOR.join(self.__date)

    @property
    def genres(self) -> str:
        return SEPARATOR.join(self.__genres)

    @property
    def styles(self) -> str:
        return SEPARATOR.join(self.__styles)

    @property
    def publisher(self) -> str:
        return SEPARATOR.join(self.__publisher)

    @property
    def country(self) -> str:
        return SEPARATOR.join(self.__country)

    @property
    def custom(self) -> str:
        return SEPARATOR.join(self.__custom)

    @property
    def done(self) -> bool:
        if self.__custom == [""]:
            return False

        tag = self.__custom[0][:4]

        is_todo = tag == TAG_TODO
        is_done = tag == TAG_DONE

        return is_todo or is_done
