from machine import Pin
import time
import ticksToDeg

pin_a = Pin(2, Pin.IN, Pin.PULL_UP)
pin_b = Pin(3, Pin.IN, Pin.PULL_UP)
count = 0

def onTick(pin) : 
    global count
    current_a = pin_a.value()
    current_b = pin_b.value()
    if current_a != current_b : 
        count += 1 
    else : 
        count -= 1 

pin_a.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=onTick)

while True :
    print(count, " ", str(ticksToDeg.ticksToDeg(count,0,22,1,+1)))
    time.sleep(0.1) 