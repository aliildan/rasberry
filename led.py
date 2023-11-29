from gpiozero import LED
from time import sleep

beyazLed = LED(17)
beyazLed.on()
sleep(10)
beyazLed.off()