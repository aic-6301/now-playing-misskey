from dataclasses import dataclass

@dataclass
class LinkedFrom:
    """
    The linked from object in the Spotify API.

    # Attributes
    None :)
    # Parameters
    None :)
    # Returns
    None :)
    """
    def __init__( self ) -> None:
        pass

@dataclass
class Image:
    """
        The image object in the Spotify API.

        # Attributes
        - height : `int`
        - url : `str`
        - width : `int`

        # Parameters
        - jsonObject : `dict`
            The Image dict object returned from the Spotify API.

        # Returns
        - `None`
    """
    height: int
    url: str
    width: int

    def __init__( self, jsonObject: dict ) -> None:
        self.height = jsonObject["height"]
        self.url = jsonObject["url"]
        self.width = jsonObject["width"]


@dataclass
class ExternalUrls:
    """
    The external urls object in the Spotify API.

    # Attributes
    - spotify : `str`
        The Spotify URL of the object.

    # Parameters
    - jsonObject : `dict`
        The ExternalUrls dict object returned from the Spotify API.
    """
    spotify: str

    def __init__( self, jsonObject: dict ) -> None:
        self.spotify = jsonObject["spotify"]


@dataclass
class ReasonsObject:
    """
    The reasons object in the Spotify API.

    # Attributes
    - reason : `str`
        The reason for the restriction.

    # Parameters
    - jsonObject : `dict`
        The ReasonsObject dict object returned from the Spotify API.
    """
    reason: str

    def __init__( self, jsonObject: dict ) -> None:
        self.reason = jsonObject["reason"]


@dataclass
class Followers:
    """
    The followers object in the Spotify API.

    # Attributes
    - href : `str`
        A link to the Web API endpoint providing full details of the followers.
    - total : `int`
        The total number of followers.

    # Parameters
    - jsonObject : `dict`
        The Followers dict object returned from the Spotify API.

    # Returns
    - `None`
    """
    href: str
    total: int

    def __init__( self, jsonObject: dict ) -> None:
        self.href = jsonObject["href"]
        self.total = jsonObject["total"]

@dataclass
class ExternalIds:
    """
    The external ids object in the Spotify API.

    # Attributes
    - isrc : `str` | `None`
        The International Standard Recording Code (ISRC) of the track.
    - ean : `str` | `None`
        The International Article Number (EAN) of the track.
    - upc : `str` | `None`
        The Universal Product Code (UPC) of the track.

    # Parameters
    - jsonObject : `dict`
        The ExternalIds dict object returned from the Spotify API.
    """
    isrc: str
    ean: str
    upc: str

    def __init__( self, jsonObject: dict ) -> None:
        self.isrc = jsonObject["isrc"] if "isrc" in jsonObject else None
        self.ean = jsonObject["ean"] if "ean" in jsonObject else None
        self.upc = jsonObject["upc"] if "upc" in jsonObject else None