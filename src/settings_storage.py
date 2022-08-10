import json
from .exceptions import CantLoadJsonException, SettingNotExistsException
from pathlib import Path
from typing import Any, Union

class SettingsStorage:
    """
    SettingsStorage class manages all settings of application including API keys.
    Settings stored in specific json file and loaded and accessed
    only by methods of this class.
    """

    def __init__(self,settings_file_path: str) -> None:
        self.__initial_json = """{"API": {}}"""
        self.__api_setting_name = "API"
        self._file_path = ""
        self._settings = {}
        
        self.set_settings_file_path(settings_file_path)
        self.init_settings_file()
        self.load()
    
    def set_settings_file_path(self, path: str) -> None:
        """Set file path to work within all class methods"""
        self._file_path = path
    
    def init_settings_file(self) -> None:
        """If key file not exists, create valid json file"""
        file = Path(self._file_path)
        
        if not file.exists():
            file.touch()
            file.write_text(self.__initial_json)
    
    def load(self) -> None:
        """Loads Settings from file"""
        file = Path(self._file_path)
        
        try:
            self._settings = json.loads(file.read_text())
        except Exception as e:
            raise CantLoadJsonException from e
    
    def save(self) -> None:
        """Saves Settings to file"""
        file = Path(self._file_path)
        file.write_text(json.dumps(self._settings))
    
    def set(self, setting_name: str, setting_value: Any) -> None:
        """Sets specific Setting and saves it to file"""
        self._settings[setting_name] = setting_value
        self.save()
    
    def get(self, setting_name: str) -> Any:
        """Returns specific Setting"""
        if setting_name not in self._settings:
            raise SettingNotExistsException
        
        return self._settings[setting_name]
    
    def unset(self, setting_name: str) -> None:
        """Removes specific setting from file"""
        if setting_name not in self._settings:
            return
        
        del self._settings[setting_name]
        self.save()
    
    def get_api_key(self, key_name: str) -> Union[str, None]:
        """Returns specific api key if exists or None if not"""
        api_keys = self.get(self.__api_setting_name)
        if key_name not in api_keys:
            return None
        
        return api_keys[key_name]
    
    def set_api_key(self, key_name: str, key_value: str) -> None:
        """Sets specific api key"""
        api_keys = self.get(self.__api_setting_name)
        api_keys[key_name] = key_value
        self.set(self.__api_setting_name, api_keys)
        