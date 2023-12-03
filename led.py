from gpiozero import LED
from gpiozero import PWMLED
from time import sleep

# led = LED(17)

# for loop
# for i in range(10):
#     print(i)
#     print("led on")
#     led.on()
#     sleep(2)
#     print("led off")
#     led.off()
#     sleep(1)
#     i = i + 1

# forever loop
# while True:
#     led.on()

led = PWMLED(17)

for index in range(11):
    print(index)
    brightness = index * 0.1
    print(f'aydinlik seviyesi:{brightness}')
    led.value=brightness
    index=index+1
    sleep(2)
