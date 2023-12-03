from gpiozero import Button
btn = Button(17)
while True:
    if btn.is_held:
        print("button basili")
    else:
        print("button basili degil")

