
import spotipy
from typed_spotipy.searchJsonObject import ReturnSearchjsonObject, TrackObject

class TypedSpotipy:
    __spotipy_client__ : spotipy.Spotify
    
    def __init__( self, client : spotipy.Spotify ) -> None:
        self.__spotipy_client__ = client

    def search( 
            self, 
            query : str, 
            search_type : str, 
            limit : int = 20, 
            offset : int = 0, 
            market : str = None 
    ) -> ReturnSearchjsonObject:
        """
        Search for an item in the Spotify API.

        # Parameters
        - query : `str`
            The search query.
        - search_type : `str`
            The type of the search.
        - limit : `int`
            The number of items to return.
        - offset : `int`
            The offset of the search.
        - market : `str`
            The market to search in.

        # Returns
        - `ReturnSearchjsonObject`
            The search result object.
        """
        result = self.__spotipy_client__.search( query, type=search_type, limit=limit, offset=offset, market=market )
        return ReturnSearchjsonObject( result )
    
    def track( self, track_id : str ) -> TrackObject:
        """
        Get a track from the Spotify API.

        # Parameters
        - track_id : `str`
            The id of the track.

        # Returns
        - `TrackObject`
            The track object.
        """
        result = self.__spotipy_client__.track( track_id )
        return TrackObject( result )
    
    def __get_internal_client__( self ) -> spotipy.Spotify:
        return self.__spotipy_client__