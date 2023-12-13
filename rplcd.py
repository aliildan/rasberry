from RPLCD.i2c import CharLCD
from signal import pause
LCD = CharLCD('PCF8574', 0x27)

LCD.write_string('Hello World')


pause()