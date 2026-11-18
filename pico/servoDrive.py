import time 
from machine import Pin, PWM 
import utility

min_pos = 3000
max_pos = 7250

servo_pwm = PWM(Pin(13), freq=50, duty_u16=max_pos)


def degToPwm(degrees):
    degrees = utility.clamp(degrees,0,180)
    return round(min_pos + (degrees / 180.0) * (max_pos - min_pos))

def setServo(position_deg):
    servo_pwm.duty_u16(degToPwm(position_deg))

def retract_pin():
    setServo(180)

def extend_pin():
    setServo(90)