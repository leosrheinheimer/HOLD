import motorDrive
import encoder
import time
import utility 

target_angle = 90.0
kP = 1
kI = 3
integral_limit = 20.0
target_deadband = 2.0
gearbox_deadband = 6.0
pid_hz = 100
max_time = 10.0

try:
    previous_time_ms = time.ticks_ms()
    prev_command = 0.0
    integral = 0
    for i in range (int(max_time * pid_hz)) :
        dt_ms = time.ticks_diff(time.ticks_ms(),previous_time_ms)
        dt = dt_ms/1000
        current_angle = encoder.getAngle()
        error = target_angle - current_angle
        previous_time_ms = time.ticks_ms()
        if abs(error) < target_deadband : 
            command = 0
        elif abs(kP * error + utility.clamp(kI*integral,-integral_limit,integral_limit)) < gearbox_deadband : 
            if prev_command > -motorDrive.duty_LIMIT and prev_command < motorDrive.duty_LIMIT :
               integral += error*dt
            integral = utility.clamp(integral,-integral_limit/kI,integral_limit/kI)
            raw = kP * error + kI * integral
            command = gearbox_deadband * raw/abs(raw)
        else : 
            if prev_command > -motorDrive.duty_LIMIT and prev_command < motorDrive.duty_LIMIT:
                    integral += error*dt
            integral = utility.clamp(integral,-integral_limit/kI,integral_limit/kI)
            command = kP*error + utility.clamp(kI*integral,-integral_limit,integral_limit)
        motorDrive.setMotor(command)
        prev_command = command 

        ##plotting
        print(f'{target_angle}, {current_angle}, {command}, {kI * integral}')  
        time.sleep(1/pid_hz)


    motorDrive.setMotor(0)

    if abs(error) > target_deadband : 
        print('ended outside tolerance')
finally:
    motorDrive.setMotor(0)



