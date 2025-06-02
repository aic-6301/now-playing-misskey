from dataclasses import dataclass

from typed_spotipy.album import Album
from typed_spotipy.artist import ArtistObject
from typed_spotipy.track import TrackObject
from typed_spotipy.baseResposeSearch import BaseResponseSearch



@dataclass
class ReturnTracksObject( BaseResponseSearch[ TrackObject ] ):
    """
    The return tracks object in the Spotify API.

    # Extends
    - `BaseResponseSearch [ TrackObject ]`

    # Attributes
    - items : `List[TrackObject]`
        A list of the tracks.

    # Parameters
    - jsonObject : `dict`
        The ReturnTracksObject dict object returned from the Spotify API.

    # Returns
    - `None`
    """
    def __init__( self, jsonObject : dict ) -> None:
        super().__init__( jsonObject )
        self.items = [ TrackObject( item ) for item in jsonObject["items"] ]

    def __iter__(self):
        return iter(self.items)
    
@dataclass
class ReturnAlbumsObject( BaseResponseSearch[ Album ] ):
    """
    The return albums object in the Spotify API.

    # Extends
    - `BaseResponseSearch [ Album ]`

    # Attributes
    - items : `List[Album]`
        A list of the albums.

    # Parameters
    - jsonObject : `dict`
        The ReturnAlbumsObject dict object returned from the Spotify API.

    # Returns
    - `None`
    """
    def __init__(self, jsonObject: dict ) -> None:
        super().__init__( jsonObject )
        self.items = [ Album( item ) for item in jsonObject["items"] ]

    def __iter__(self):
        return iter(self.items)
    
@dataclass
class ReturnArtistsObject( BaseResponseSearch[ ArtistObject ] ):
    """
    The return artists object in the Spotify API.

    # Extends
    - `BaseResponseSearch [ ArtistObject ]`

    # Attributes
    - items : `List[ArtistObject]`
        A list of the artists.

    # Parameters
    - jsonObject : `dict`
        The ReturnArtistsObject dict object returned from the Spotify API.

    # Returns
    - `None`
    """
    def __init__(self, jsonObject: dict) -> None:
        super().__init__( jsonObject )
        self.items = [ ArtistObject( item ) for item in jsonObject["items"] ]

    def __iter__(self):
        return iter(self.items)
    
@dataclass
class ReturnSearchjsonObject:
    """
    The return search object in the Spotify API.

    # Attributes
    - tracks : `ReturnTracksObject`
        The tracks object.
    - albums : `ReturnAlbumsObject`
        The albums object.
    - artists : `ReturnArtistsObject`
        The artists object.

    # Parameters
    - jsonjsonObject : `dict`
        The ReturnSearchjsonObject dict object returned from the Spotify API.

    # Returns
    - `None`
    """
    tracks: ReturnTracksObject | None
    albums: ReturnAlbumsObject | None
    artists: ReturnArtistsObject | None

    def __init__( self, jsonjsonObject: dict ):
        if jsonjsonObject is None:
            return
        
        if "tracks" not in jsonjsonObject:
            jsonjsonObject["tracks"] = None
        else:
            self.tracks = ReturnTracksObject( jsonjsonObject["tracks"] if "tracks" in jsonjsonObject else None )
        
        if "albums" not in jsonjsonObject:
            jsonjsonObject["albums"] = None
        else:
            self.albums = ReturnAlbumsObject( jsonjsonObject["albums"] if "albums" in jsonjsonObject else None )

        if "artists" not in jsonjsonObject:
            jsonjsonObject["artists"] = None
        else:
            self.artists = ReturnArtistsObject( jsonjsonObject["artists"] if "artists" in jsonjsonObject else None )
