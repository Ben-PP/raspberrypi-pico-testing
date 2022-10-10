from machine import Pin
import time

led = Pin('LED', Pin.OUT)

i  = 0
while i < 10:
    led.value(1)
    time.sleep_ms(500)
    led.value(0)
    time.sleep_ms(500)
    i += 1
