from gpiozero import Button
btn = Button(2)
while True:
    if btn.is_held:
        print("button basili")
    else:
        print("button basili degil")

