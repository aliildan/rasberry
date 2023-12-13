from RPLCD.i2c import CharLCD
from gpiozero import Button, LED, LEDBoard, DistanceSensor, LEDBarGraph, MotionSensor
from signal import pause
from time import sleep

lcd = CharLCD('PCF8574', 0x27)
lcd.write_string('Hello World')
lcd.clear()


#leds = LEDBoard(17,18,27,23)
#leds.on()



led_graph = LEDBarGraph(17,18,27,23, pwm=True)

distance_sensor= DistanceSensor(24,25)
while True:
    print('Distance to nearest object is', distance_sensor.distance, 'm')
    lcd.write_string(f'Uzaklik: {distance_sensor.distance} metre')
    led_graph.value = 1 - distance_sensor.distance
    sleep(1)
    lcd.clear()

#for i in range(300):
#    yellow = 1 if i%2==0 else 0
#    red = 1 if i%3==0 else 0
#    blue = 1 if i%5==0 else 0
#    white = 1 if i%7==0 else 0
#    print(f'index: {i} TAM BOLUNME iki: {yellow}  uc: {red} bes: {blue} yedi: {white}')
#    leds.value=(yellow,red,blue,white)
#    i=i+1
#    sleep(2)

#pause()


