from RPLCD.gpio import CharLCD
from signal import pause
lcd = CharLCD(numbering_mode=26)

lcd.write_string('Hello World')

pause()
