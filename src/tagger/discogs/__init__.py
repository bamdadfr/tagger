import time
from typing import List, Union

import discogs_client
import requests
from discogs_client import Master, Release
from rich import print

from tagger.common.DiscogsRelease import DiscogsRelease
from tagger.config import Config
from tagger.folder import Folder
from tagger.utils.limit import limit


class Discogs:
    token: str
    client: discogs_client.Client

    def __init__(
        self,
        config: Config,
    ) -> None:
        self.config = config
        self.client = discogs_client.Client("Tagger", user_token=self.config.token)

    @limit()
    def __fetch_release_details(
        self,
        release: Release,
    ):
        url = f"https://api.discogs.com/releases/{release.id}"

        response = requests.get(url)
        if response.status_code != 200:
            print("Sleeping...")
            time.sleep(5)
            return self.__fetch_release_details(release)

        json = response.json()
        return json

    @limit()
    def search(
        self,
        folder: Folder,
    ) -> Union[DiscogsRelease, None]:
        file = folder.files[0]
        file_artist = file.artists[0]
        query = f"{file_artist} {file.album}"
        print(f"[bold blue]{query}[/bold blue]")

        selected: Union[Release, None] = None

        masters_results = self.client.search(query, type="master")
        masters = list(masters_results)

        if len(masters) > 0:
            print("Found master")

            master: Master = masters[0]
            master_tracklist = [t for t in master.tracklist]  # type: ignore

            if folder.count == len(master_tracklist):
                selected = master.main_release  # type: ignore

        if selected is not None:
            details = self.__fetch_release_details(selected)
        else:
            releases_results = self.client.search(query, type="release")
            releases: List[Release] = list(releases_results)

            print(f"Found {len(releases)} results")

            releases = releases[:10]  # considering only the first ten releases

            for release in releases:
                release_tracklist = [t for t in release.tracklist]  # type: ignore
                if folder.count != len(release_tracklist):
                    continue

                selected = release
                break

            if selected is None:
                return selected

            # getting additional details
            details = self.__fetch_release_details(selected)

        discogs_release = DiscogsRelease(
            id=selected.id,  # type: ignore
            artists=selected.artists,  # type: ignore
            name=selected.title,  # type: ignore
            date=details["released"] if "released" in details else str(details["year"]),
            genres=selected.genres,  # type: ignore
            styles=selected.styles,  # type: ignore
            label=selected.labels[0].name,  # type: ignore
            country=selected.country,  # type: ignore
            url=selected.url,  # type: ignore
        )

        print(f"Found release id {discogs_release.id}")
        print(discogs_release.url)

        return discogs_release
