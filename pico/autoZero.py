import encoder
import motorDrive
import time 
import iLoop
import ticksToDeg
import servoDrive as servo


def autoZero(start_duty) : 
    prev_angle = 100000
    frozen_angle_s = 0.0
    minimum_frozen_s = 0.3
    dt = 0.01
    run_time = 0.0
    max_runtime = 10
    zeroing_bolt_deg = 155.9 # from trials (in measurements.md)
    pin_reached = False

    try:
        run_time = 0.0
        servo.extend_pin()
        time.sleep(1.5)
        while True :
            motorDrive.setMotor(start_duty)
            current_angle = encoder.getAngle()
            if current_angle == prev_angle :
                    frozen_angle_s += dt
            else :
                 frozen_angle_s = 0.0

            if frozen_angle_s >= minimum_frozen_s : 
                 motorDrive.setMotor(0)
                 encoder.zero_offset_ticks = ticksToDeg.zeroOffsetTicks(encoder.count,zeroing_bolt_deg,encoder.ticks_per_output_turn,encoder.direction)
                 pin_reached = True
                 break

            #angle resetting
            prev_angle = current_angle

            #time management
            time.sleep(dt)
            run_time += dt

            if run_time >= max_runtime : 
                 break
            

        if pin_reached == False : 
            print('zeroing bolt not reached, runtime limit hit')
            servo.retract_pin()
            return False
        else :  
            #going back to zero
            iLoop.goToAngle(0,2,False)
            servo.retract_pin()
            return True
        
    finally:
        motorDrive.setMotor(0)
