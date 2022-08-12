import config
from pathlib import Path
from src.settings_storage import SettingsStorage

# API imports
from src.location_engines.geojs_engine import GeoJsLocationEngine

def setup():
    data_dir = Path(config.DATA_DIR_PATH)
    if not data_dir.exists():
        data_dir.mkdir()


def main():
    setup()
    settings = SettingsStorage(config.SETTINGS_FILE_PATH, config.SETTINGS_KEYS)
    print(settings.get_api_key(config.SETTINGS_KEYS["api_openweather_key"]))
    geojs = GeoJsLocationEngine()
    coords = geojs.get_current_coords()
    print(coords)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        ## TODO save state (when state will be created)
        pass