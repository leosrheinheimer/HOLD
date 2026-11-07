from machine import Pin, PWM

motor_pwm = PWM(Pin(14), freq=20000, duty_u16=0)
dir_pin = Pin(15,Pin.OUT)


max_possible_duty = 65535.0
duty_pct = 20.0
duty_pct = max(0, min(duty_pct, 20))
duty_LIMIT = 20


def setMotor(command) : 
    if command == 0:
        motor_pwm.duty_u16(0)
    elif command > 0 : 
        dir_pin.value(1)
    elif command < 0 :
        dir_pin.value(0)
    abs_duty = abs(command)
    duty_pct = max(0, min(abs_duty, duty_LIMIT))
    motor_pwm.duty_u16(int((duty_pct/100) * max_possible_duty))
