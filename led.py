from gpiozero import LED
from time import sleep
led = LED(19)

def LED_blink_time(led_on, led_off):
    """Defines length of blinks and time betweem blinks"""
    while True:
        led.on()
        sleep(led_on)
        led.off()
        sleep(led_off)

led_on= float(input("How long should the LED stay on?"))
led_off= float(input("How long sohuld the LED stay off?"))

LED_blink_time(led_on, led_off)


