from typing import List

from typed_spotipy.externalObjects import ExternalUrls, ExternalIds, LinkedFrom, ReasonsObject
from typed_spotipy.album import Album, SimplifiedArtistObject

Album_Type = str
Track_Type = str

class TrackObject:
    """
    The track object in the Spotify API.

    # Attributes
    - album : `Album`
        The album of the track.
    - artists : `List[SimplifiedArtistObject]`
        A list of the artists of the track.
    - available_markets : `List[str]`
        A list of the available markets of the track.
    - disc_number : `int`
        The disc number of the track.
    - duration_ms : `int`
        The duration of the track in milliseconds.
    - explicit : `bool`
        Whether the track is explicit or not.
    - external_ids : `ExternalIds`
        The external ids of the track.
    - external_urls : `ExternalUrls`
        The external urls of the track.
    - href : `str`
        The href of the track.
    - id : `str`
        The id of the track.
    - is_playable : `bool`
        Whether the track is playable or not.
    - linked_from : `LinkedFrom`
        The linked from object of the track.
    - restrictions : `ReasonsObject`
        The restrictions of the track.
    - name : `str`
        The name of the track.
    - popularity : `int`
        The popularity of the track.
    - preview_url : `str` | `None`
        A link to a 30 second preview (MP3 format) of the track. Can be `None`.
    - track_number : `int`
        The track number of the track.
    - type : `Track_Type`
        The type of the track.
    - uri : `str`
        The URI of the track.
    - is_local : `bool`
        Whether the track is local or not.

    # Parameters
    - jsonObject : `dict`
        The TrackObject dict object returned from the Spotify API.

    # Returns
    - `None`
    """
    album: Album
    artists: List[SimplifiedArtistObject]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: ExternalIds
    external_urls: ExternalUrls
    href : str
    id: str
    is_playable: bool
    linked_from: LinkedFrom
    restrictions: ReasonsObject
    name: str
    popularity: int
    preview_url: str | None
    """
    A link to a 30 second preview (MP3 format) of the track. Can be `None`

    # !!! Important Policy Note

    Spotify Audio preview clips can not be a standalone service

    Audio Preview Clips may not be offered as a standalone service or product.
    [ More Infomation ](https://developer.spotify.com/policy#ii-respect-content-and-creators)
    """
    track_number: int
    type: Track_Type
    uri: str
    is_local: bool

    def __init__( self, jsonObject: dict ):
        self.album = Album( jsonObject["album"] )
        self.artists = [ SimplifiedArtistObject( artist ) for artist in jsonObject["artists"] ]
        self.available_markets = jsonObject["available_markets"] if "available_markets" in jsonObject else None
        self.disc_number = int(jsonObject["disc_number"])
        self.duration_ms = int(jsonObject["duration_ms"])
        self.explicit = bool(jsonObject["explicit"])
        self.external_ids = ExternalIds( jsonObject["external_ids"] )
        self.external_urls = ExternalUrls( jsonObject["external_urls"] )
        self.href = str( jsonObject["href"] )
        self.id = str( jsonObject["id"] )
        self.is_playable = bool( jsonObject["is_playable"] if "is_playable" in jsonObject else False )
        self.linked_from = LinkedFrom()
        self.restrictions = ReasonsObject( jsonObject["restrictions"] if "restrictions" in jsonObject else { "reason": None })
        self.name = str( jsonObject["name"] )
        self.popularity = int( jsonObject["popularity"] )
        self.preview_url = str( jsonObject["preview_url"] ) if "preview_url" in jsonObject else None
        self.track_number = int( jsonObject["track_number"] )
        self.type = jsonObject["type"]
        self.uri = str( jsonObject["uri"] )
        self.is_local = bool( jsonObject["is_local"] )