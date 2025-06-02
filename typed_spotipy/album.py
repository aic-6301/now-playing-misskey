from dataclasses import dataclass
from typing import List

# Path: typed_spotipy/externalObjects.py
from typed_spotipy.externalObjects import ExternalUrls, Image
from typed_spotipy.artist import SimplifiedArtistObject

Album_Type = str
Track_Type = str


@dataclass
class Album:
    """
    The album object in the Spotify API.

    # Attributes
    - album_type : `Album_Type`
        The type of the album.
    - artists : `List[SimplifiedArtistObject]`
        A list of the artists of the album.
    - available_markets : `List[str]` | `None`
        A list of the available markets of the album.
    - external_urls : `ExternalUrls`
        The external urls of the album.
    - href : `str`
        The href of the album.
    - id : `str`
        The id of the album.
    - images : `List[Image]`
        A list of the images of the album.
    - name : `str`
        The name of the album.
    - release_date : `str`
        The release date of the album.
    - release_date_precision : `str`
        The release date precision of the album.
    - total_tracks : `int`
        The total number of tracks in the album.
    - type : `str`
        The type of the album.
    - uri : `str`
        The URI of the album.

    # Parameters
    - jsonObject : `dict`
        The AlbumObject dict object returned from the Spotify API.

    # Returns
    - `None`
    """
    album_type: Album_Type
    artists: List[SimplifiedArtistObject]
    available_markets: List[str]
    external_urls: ExternalUrls
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: str
    release_date_precision: str
    total_tracks: int
    type: str
    uri: str

    def __init__( self, jsonObject: dict ) -> None:
        self.album_type = jsonObject["album_type"]
        self.artists = [ SimplifiedArtistObject( artist ) for artist in jsonObject["artists"] ]
        self.available_markets = jsonObject["available_markets"] if "available_markets" in jsonObject else None
        self.external_urls = ExternalUrls( jsonObject["external_urls"] )
        self.href = jsonObject["href"]
        self.id = jsonObject["id"]
        self.images = [ Image( image ) for image in jsonObject["images"] ]
        self.name = jsonObject["name"]
        self.release_date = jsonObject["release_date"]
        self.release_date_precision = jsonObject["release_date_precision"]
        self.total_tracks = jsonObject["total_tracks"]
        self.type = jsonObject["type"]
        self.uri = jsonObject["uri"]
