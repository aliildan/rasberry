from RPLCD.i2c import CharLCD
from time import sleep
from datetime import datetime
from api import API

api = API()


lcd = CharLCD('PCF8574', 0x27)

while True:
    weather = api.get_weather()
    icon_binary = tuple(int(binary, 2) for binary in weather.get_icon())
    lcd.create_char(1,icon_binary)
    datetime_obj = datetime.fromisoformat(weather.get_time())
    formatted_datetime = datetime_obj.strftime("%d-%m-%Y %H:%M")
    lcd.cursor_pos(0, 0)
    lcd.write(1)
    first_row = f'{weather.get_temperature()}Â°C , {weather.get_wind_speed()}km/h'
    lcd.write_string(first_row)
    lcd.cursor_pos(0, 1)
    lcd.write_string(formatted_datetime)
    sleep(120)
