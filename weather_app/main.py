from RPLCD.i2c import CharLCD
from time import sleep
from datetime import datetime
from api import API

api = API()


lcd = CharLCD('PCF8574', 0x27)

while True:
    weather = api.get_weather()
    lcd.create_char(1,weather.get_icon())
    datetime_obj = datetime.fromisoformat(weather.get_time())
    formatted_datetime = datetime_obj.strftime("%d-%m-%Y %H:%M")
    lcd.cursor_pos(0,0)
    lcd.write(1)
    first_row = f'{weather.get_temperature()} C , Wind: {weather.get_wind_speed()}km/h'
    lcd.write_string(first_row)
    lcd.cursor_pos(0, 1)
    lcd.write_string(formatted_datetime)
    sleep(120)
