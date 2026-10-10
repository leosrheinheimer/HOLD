from ticksToDeg import ticksToDeg
from machine import Pin
import time

pin_a = Pin(2, Pin.IN, Pin.PULL_UP)
pin_b = Pin(3, Pin.IN, Pin.PULL_UP)

count = 0
last_a = 0

while True:
    pin_a_value = pin_a.value()
    pin_b_value = pin_b.value()

    if last_a != pin_a_value :
        if pin_b_value == pin_a_value : 
            count += 1
        elif pin_b_value != pin_a_value:
            count -= 1
        print(str(count) , " " +"encoder degrees: " , str(ticksToDeg(count,0,1245.5,1,+1)))
    last_a = pin_a_value
