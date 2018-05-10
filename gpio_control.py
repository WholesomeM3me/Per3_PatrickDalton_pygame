from gpiozero import LED, Button
from time import sleep

led = LED(19)
button = Button(22)

while True:
    button.wait_for_press()
    led.toggle()
    sleep(0.5)
