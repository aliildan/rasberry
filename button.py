from gpiozero import Button
from signal import pause
btn = Button(17)

def button_pressed():
    print("button a basildi :)")

def button_released():
    print("buton birakildi :(")

btn.when_activated= button_pressed
btn.when_deactivated= button_released

pause()