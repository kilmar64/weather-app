from dataclasses import dataclass
from time import time
from typing import NamedTuple
from enum import Enum


class CoordinatesTuple(NamedTuple):
    latitude: float
    longitude: float


class WeatherType(Enum):
    THUNDERSTORM = "Thunderstorm"
    ##TODO

class TemperatureTuple(NamedTuple):
    current: float
    min: float
    max: float
    morn: float
    day: float
    eve: float
    night: float


@dataclass
class WeatherState:
    weather_type: WeatherType
    temp_c: TemperatureTuple # celcius
    temp_feels_like_c: TemperatureTuple # celcius
    sunrise: time
    sunset: time
    air_pressure: float
    wind_speed: float
    wind_dir: int
    humidity: float
    uvi: float
    

@dataclass
class WeatherData:
    forecast: dict[time, WeatherState]
    city: str