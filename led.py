from gpiozero import LED
from time import sleep

led = LED(17)

for i in range(10):
    print(i)
    print("led on")
    led.on()
    sleep(2)
    print("led off")
    led.off()
    sleep(1)
    i = i + 1
