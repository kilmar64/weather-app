import os

DATA_DIR_PATH = os.getcwd() + "/data/"
SETTINGS_FILE_PATH = DATA_DIR_PATH + "settings.json"

# Settings keys
SETTINGS_KEYS = {
    "api_keys": "API",
    "api_openweather_key": "openweather"
}

# API
GEOJS_API_LINK = "https://get.geojs.io/v1/ip/geo.json"