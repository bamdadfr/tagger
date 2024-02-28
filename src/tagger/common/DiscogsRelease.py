from dataclasses import dataclass
from typing import List, Union


@dataclass(frozen=True, order=True)
class DiscogsRelease:
    id: int
    artists: List[str]
    name: str
    date: str
    genres: List[str]
    styles: Union[List[str], None]
    label: str
    country: str
    url: str
