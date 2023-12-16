class Weather:
    clear_sky = "Clear sky"
    cloudy = "Cloudy"
    rainy = "Rainy"
    thunderstorm = "Thunderstorm"
    snowy = "Snowy"

    def __init__(self):
        self.temperature = None
        self.weatherCode = None
        self.windSpeed = None
        self.description = None
        self.icon = None
        self.time = None

    def set_temperature(self, temperature: float):
        self.temperature = temperature

    def set_weather_code(self, weather_code: int):
        self.weatherCode = weather_code

    def set_wind_speed(self, wind_speed: float):
        self.windSpeed = wind_speed

    def set_description(self, description: str):
        self.description = description

    def set_icon(self, icon_byte_array: tuple):
        self.icon = icon_byte_array

    def get_temperature(self) -> float:
        return self.temperature

    def set_time(self, time: str):
        self.time = time

    def get_weather_code(self) -> int:
        return self.weatherCode

    def get_wind_speed(self) -> float:
        return self.windSpeed

    def get_description(self) -> str:
        return self.description

    def get_icon(self) -> tuple:
        return self.icon

    def get_time(self) -> str:
        return self.time
