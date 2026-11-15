import motorDrive
import encoder
import time
import utility 




def goToAngle(target_angle: float,max_time: float,logging: bool):
    try:
        pid_hz = 100
        kP = 1
        kI = 3
        integral_limit = 20.0
        target_deadband = 2.0
        command = 0
        integral = 0
        prev_time = time.ticks_us()

        if logging == True :
            print("Target Angle, Current Angle, Command, kI * Integral")

        for i in range(int(max_time * pid_hz)):
            
            #time
            current_time = time.ticks_us()
            dt = time.ticks_diff(current_time,prev_time)/1000000
            prev_time = current_time
        
            #angle
            current_angle = encoder.getAngle()
            error = target_angle - current_angle

            #command
            prev_command = command

            #pi loop
            if abs(error) < target_deadband : 
                command = 0
            else : 
                if prev_command > -motorDrive.duty_LIMIT and prev_command < motorDrive.duty_LIMIT:
                    integral += error * dt
                # anti windup
                integral = utility.clamp(integral,-integral_limit/kI,integral_limit/kI)
                command = kP * error + kI * integral

            #motor commanding
            motorDrive.setMotor(command)

            if logging == True :
                #logging
                print(f'{target_angle}, {current_angle}, {command}, {kI * integral}')

            #pause for hz
            time.sleep(1/pid_hz)

    finally:
        motorDrive.setMotor(0)
