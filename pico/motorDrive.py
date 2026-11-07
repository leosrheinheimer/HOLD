import time 
from machine import Pin, PWM

motor_pwm = PWM(Pin(14), freq=20000, duty_u16=0)
dir_pin = Pin(15,Pin.OUT)


max_possible_duty = 65535.0
duty_pct = 20.0
duty_pct = max(0, min(duty_pct, 20))

print('cycle started')
dir_pin.value(0)
motor_pwm.duty_u16(int((duty_pct/100) * max_possible_duty))
time.sleep(2)
motor_pwm.duty_u16(0)
print('complete')