import motorDrive
import encoder
import time

target_angle = 90.0
kP = 1
target_deadband = 2.0
gearbox_deadband = 6.0
pid_hz = 100
max_time = 10.0

try:
    for i in range (int(max_time * pid_hz)) :
        current_angle = encoder.getAngle()
        error = target_angle - current_angle
        if abs(error) < target_deadband : 
            command = 0
        elif abs(kP * error) < gearbox_deadband : 
            command = error/abs(error) * gearbox_deadband
        else : 
            command = kP*error
        motorDrive.setMotor(command)

        ##plotting
        print(f'{target_angle}, {current_angle}, {command}')    
        time.sleep(1/pid_hz)

    motorDrive.setMotor(0)

    if abs(error) > target_deadband : 
        print('ended outside tolderance')
finally:
    motorDrive.setMotor(0)



