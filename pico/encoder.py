from machine import Pin
import ticksToDeg

zero_offset_ticks = 0
ticks_per_output_turn = 1245.5
direction = 1

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


def getAngle() : 
    angle_deg = ticksToDeg.ticksToDeg(count, zero_offset_ticks, ticks_per_output_turn, direction)
    return angle_deg

