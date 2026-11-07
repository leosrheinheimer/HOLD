from machine import Pin

pin_a = Pin(2, Pin.IN, Pin.PULL_UP)
pin_b = Pin(3, Pin.IN, Pin.PULL_UP)
count = 0
last_a = pin_a.value()

def onTick(pin) : 
    global count, last_a
    current_a = pin_a.value()
    if current_a == last_a : 
        return 
    current_b = pin_b.value()
    if current_a != current_b : 
        count += 1 
    else : 
        count -= 1 
    last_a = current_a

pin_a.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=onTick, hard=True)


