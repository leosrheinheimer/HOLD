import time
from machine import Pin, PWM

pwm0 = PWM(Pin(25), freq=2000, duty_u16=32768)

while True:
    for i in range(0,10,1) :
        increment = (i/10)* 65535.0
        pwm0.duty_u16(int(increment))
        print(pwm0.duty_u16())
        time.sleep(0.1)
    for i in range(10,0,-1) :
        increment = (i/10)* 65535.0
        pwm0.duty_u16(int(increment))
        print(pwm0.duty_u16())
        time.sleep(0.1)

