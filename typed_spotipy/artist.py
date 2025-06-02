from dataclasses import dataclass

from typed_spotipy.externalObjects import ExternalUrls, Image, Followers

@dataclass
class ArtistObject:
    """
    The artist object in the Spotify API.

    # Attributes
    - external_urls : `ExternalUrls`
        The external urls of the artist.
    - followers : `Followers`
        The followers of the artist.
    - genres : `List[str]`
        A list of the genres the artist is associated with.
    - href : `str`
        The href of the artist.
    - id : `str`
        The id of the artist.
    - images : `List[Image]`
        A list of the images of the artist.
    - name : `str`
        The name of the artist.
    - popularity : `int`
        The popularity of the artist.
    - type : `str`
        The type of the artist.
    - uri : `str`
        The URI of the artist.
    
    # Parameters
    - jsonObject : `dict`
        The ArtistObject dict object returned from the Spotify API.

    # Returns
    - `None`
    """
    external_urls: ExternalUrls
    followers: Followers
    genres: list[ str ]
    href: str
    id: str
    images: list[ Image ]
    name: str
    popularity: int
    type: str
    uri: str

    def __init__( self, jsonObject: dict ) -> None:
        self.external_urls = ExternalUrls( jsonObject["external_urls"] )
        self.followers = Followers( jsonObject["followers"] )
        self.genres = jsonObject["genres"]
        self.href = jsonObject["href"]
        self.id = jsonObject["id"]
        self.images = [ Image( image ) for image in jsonObject["images"] ]
        self.name = jsonObject["name"]
        self.popularity = jsonObject["popularity"]
        self.type = jsonObject["type"]
        self.uri = jsonObject["uri"]

@dataclass
class SimplifiedArtistObject:
    """
    The simplified artist object in the Spotify API.

    # Attributes
    - external_urls : `ExternalUrls`
        The external urls of the artist.
    - href : `str`
        The href of the artist.
    - id : `str`
        The id of the artist.
    - name : `str`
        The name of the artist.
    - type : `str`
        The type of the artist.
    - uri : `str`
        The URI of the artist.

    # Parameters
    - jsonObject : `dict`
        The SimplifiedArtistObject `dict` object returned from the Spotify API.

    # Returns
    - `None`
    """
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    type: str
    uri: str

    def __init__( self, jsonObject: dict ) -> None:
        self.external_urls = ExternalUrls( jsonObject["external_urls"] )
        self.href = jsonObject["href"]
        self.id = jsonObject["id"]
        self.name = jsonObject["name"]
        self.type = jsonObject["type"]
        self.uri = jsonObject["uri"]