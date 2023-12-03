from gpiozero import Button
btn = Button(2)
while True:
    if btn.is_pressed:
        print("button basili")
    else:
        print("button basili degil")

