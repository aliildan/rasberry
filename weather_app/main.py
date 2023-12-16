from RPLCD.i2c import CharLCD
from gpiozero import LED, LEDBoard
from time import sleep
from datetime import datetime
from api import API

api = API()

lcd = CharLCD('PCF8574', 0x27)
yellow = 17
blue = 27
white = 23
red = 18
while True:
    weather = api.get_weather()
    icon_binary = tuple(int(binary, 2) for binary in weather.get_icon())
    lcd.create_char(1, icon_binary)
    lcd.create_char(2, (0b00000000, 0b00011000, 0b00111110, 0b01111100, 0b11111000, 0b01111100, 0b00111110, 0b00011000))
    datetime_obj = datetime.fromisoformat(weather.get_time())
    formatted_datetime = datetime_obj.strftime("%d-%m-%Y %H:%M")
    lcd.cursor_pos = (0, 0)
    lcd.write(1)
    first_row = f' {weather.get_temperature()}C,'
    lcd.write_string(first_row)
    lcd.write(2)
    first_row_2 = f'{weather.get_wind_speed()}km/h'
    lcd.write_string(first_row_2)
    lcd.cursor_pos = (1, 0)
    lcd.write_string(formatted_datetime)

    if weather.get_description() == weather.clear_sky:
        led = LED(yellow)
    elif weather.get_description() == weather.rainy:
        led = LED(blue)
    elif weather.get_description() == weather.cloudy or weather.get_description() == weather.thunderstorm:
        led = LED(white)
    elif weather.get_description() == weather.snowy:
        led = LED(red)
    else:
        led = LEDBoard(yellow, blue, white, red)
    led.on()
    sleep(60)
    led.off()
    sleep(1)

