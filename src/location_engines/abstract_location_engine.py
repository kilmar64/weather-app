from abc import ABC, abstractclassmethod
from ..data_types import CoordinatesTuple


class LocationEngine(ABC):
    @abstractclassmethod
    def get_current_coords(self) -> CoordinatesTuple:
        """
        Returns current coordinates
        Depends on realisation, device gps or ip coordinates
        """
        pass
    
    @abstractclassmethod
    def get_coords_for_search(self, search: str) -> CoordinatesTuple:
        """Searches location by search string via api and returns coordinates of searched city"""
        pass