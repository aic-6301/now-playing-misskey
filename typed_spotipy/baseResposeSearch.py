from dataclasses import dataclass
import typing
from typing import TypeVar, Generic, List, Dict, Union

SearchGenericTypeT = TypeVar('SearchGenericTypeT')

@dataclass
class BaseResponseSearch( Generic[SearchGenericTypeT] ):
    """
    Base class for all search responses. This class is generic and should be used with the specific search response class.

    # Attributes
    - href : `str`
    - limit : `int`
    - next : `str`
    - offset : `int`
    - previous : `str`
    - total : `int`

    # Generic Attributes
    - items : `List[SearchGenericTypeT]`
        `SearchGenericTypeT` is the type of the items in the search response.
        You should replace SearchGenericTypeT with the specific type of the items in the search response.

    # Parameters
    - jsonObject : `dict`
        The JSON object returned from the Spotify API.

    # Returns
    - `None`
    """
    href : str
    limit: int
    next: str
    offset: int
    previous: str
    total: int
    items : List[SearchGenericTypeT]

    def __init__( self , jsonObject : dict ) -> None:
        super().__init__()
        self.href = jsonObject["href"]
        self.limit = jsonObject["limit"]
        self.next = jsonObject["next"]
        self.offset = jsonObject["offset"]
        self.previous = jsonObject["previous"]
        self.total = jsonObject["total"]