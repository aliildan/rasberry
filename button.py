from gpiozero import Button
btn = Button(2)
btn.wait_for_press()
print("buton a basildi")

