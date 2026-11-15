import encoder
import motorDrive
import time 
import iLoop



def autoZero() : 
    prev_angle = 100000
    frozen_angle_s = 0.0
    minimum_frozen_s = 0.3
    dt = 0.01
    run_time = 0.0
    max_runtime = 4
    imperical_zero_diff = 17

    try:
        run_time = 0.0
        while True :

            motorDrive.setMotor(-20)
            current_angle = encoder.getAngle()
            if current_angle == prev_angle :
                    frozen_angle_s += dt
            else :
                 frozen_angle_s = 0.0

            if frozen_angle_s >= minimum_frozen_s : 
                 motorDrive.setMotor(0)
                 print('zeroing bolt reached')
                 actual_zero = current_angle + imperical_zero_diff
                 break

            #angle resetting
            prev_angle = current_angle

            #time management
            time.sleep(dt)
            run_time += dt

            if run_time >= max_runtime : 
                 break

        #going back to zero
        iLoop.goToAngle(actual_zero,1,False)

    finally:
        motorDrive.setMotor(0)

