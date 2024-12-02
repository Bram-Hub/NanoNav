from machine import Pin
import time

LED = Pin(6, Pin.OUT)

while True:
    LED.off()
    time.sleep(2)
    LED.on()
