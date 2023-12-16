from RPLCD.i2c import CharLCD
from time import sleep
from datetime import datetime
from api import API

api = API()

lcd = CharLCD('PCF8574', 0x27)

while True:
    weather = api.get_weather()
    icon_binary = tuple(int(binary, 2) for binary in weather.get_icon())
    lcd.create_char(1, icon_binary)
    lcd.create_char(2, (0b00000000, 0b00011000, 0b00111110, 0b01111100, 0b11111000, 0b01111100, 0b00111110, 0b00011000))
    datetime_obj = datetime.fromisoformat(weather.get_time())
    formatted_datetime = datetime_obj.strftime("%d-%m-%Y %H:%M")
    lcd.write(1)
    first_row = f' {weather.get_temperature()}C,'
    lcd.write_string(first_row)
    lcd.write(2)
    first_row_2 = f' {weather.get_wind_speed()}km/h'
    lcd.write_string(first_row_2)
    lcd.write_string(formatted_datetime)
    sleep(120)
