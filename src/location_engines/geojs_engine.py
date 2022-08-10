import config
import requests
from .abstract_location_engine import LocationEngine
from ..data_types import CoordinatesTuple
from ..exceptions import ApiNotSupportingException, CantGetCoordinatesException


class GeoJsLocationEngine(LocationEngine):
    def get_current_coords(self) -> CoordinatesTuple:
        httpresponse = requests.get(config.GEOJS_API_LINK)
        
        if(httpresponse.status_code != 200):
            raise CantGetCoordinatesException
        
        jsonresponse = httpresponse.json()
        
        if ("latitude" not in jsonresponse) or ("longitude" not in jsonresponse):
            raise CantGetCoordinatesException
        
        return CoordinatesTuple(
            latitude = jsonresponse["latitude"],
            longitude = jsonresponse["longitude"]
        )
     
    def get_coords_for_search(self, search: str) -> None:
        raise ApiNotSupportingException