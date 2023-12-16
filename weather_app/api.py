from typing import Type

import requests
import json

from weather_app.weather import Weather


class API:

    def __init__(self):
        self.api_url = "https://api.open-meteo.com/v1/forecast?latitude=48.2085&longitude=16.3721&current=temperature_2m,weather_code,wind_speed_10m&timezone=auto&forecast_days=1"
        self.wmo_codes_file = "wmo_codes.json"

    def get_weather(self) -> Weather | None:
        wmo_codes = open(self.wmo_codes_file, 'r')
        response = requests.get(self.api_url)
        if response.status_code != 200:
            print(f'ERROR: statusCode: {response.status_code} -- {response.content}')
            return None

        print(f'Response: {response.json()}')

        data = json.loads(response.json())
        wmo = json.loads(wmo_codes.read())

        weather = Weather()
        weather.set_weather_code(data['current']['weather_code'])
        weather.set_temperature(data['current']['temperature_2m'])
        weather.set_wind_speed(data['current']['wind_speed_10m'])
        weather.set_wind_speed(data['current']['time'])

        for d in wmo:
            if weather.get_weather_code() in d["codes"]:
                weather.set_description(d['description'])
                weather.set_icon(tuple(d['icon']))

        return weather
