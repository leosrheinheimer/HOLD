from machine import Pin
import time

pin_a = Pin(2, Pin.IN)
pin_b = Pin(3, Pin.IN)

while True:
    pin_a_value = pin_a.value()
    pin_b_value = pin_b.value()
    print (pin_a_value,pin_b_value)
    time.sleep(0.05)