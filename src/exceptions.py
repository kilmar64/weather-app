class CantGetCoordinatesException(Exception):
    """Program can't get coordinates with api"""
    
class ApiNotSupportingException(Exception):
    """Raises when api doesn't support specific feature"""
    
class CantLoadJsonException(Exception):
    """Raises when error occured while reading json"""
    
class SettingNotExistsException(Exception):
    """Raises when trying to get setting which doesn't exists"""