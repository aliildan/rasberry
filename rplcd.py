from RPLCD.gpio import CharLCD
from signal import pause
LCD = CharLCD()

LCD.write_string('Hello World')

pause()
