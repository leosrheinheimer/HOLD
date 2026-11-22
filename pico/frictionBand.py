import autoZero
import motorDrive
import iLoop
import encoder 
import time

loaded_lift_start = {0: 17.0, 15: 16.75, 30: 16.0, 45: 15.0, 60: 13.5, 75: 11.75}
loaded_drop_start = {0: 4.75, 15: 4.5, 30: 4.0, 45: 3.25, 60: 2.25, 75: 1.25}

unloaded_lift_start = {0: 12.25, 15: 13.0, 30: 12.25, 45: 7.25, 60: 4.5, 75: 0.75}
unloaded_drop_start = {0: 4.0, 15: 3.25, 30: 3.5, 45: 3.0, 60: 2.25, 75: 0.0}

rerun_lift_start = {60: 6.0, 75: 3.0}
rerun_unloaded_lift_start = {15: 8.0, 30: 7.0}

motorDrive.setMotor(0)

for angle in range(15,45,15):
    print(f'angle ={angle} degrees above horizontal')
    if autoZero.autoZero(30) == False :
        print('not zeroed')
        autoZero.autoZero(30)
    time.sleep(1)
    iLoop.goToAngle(angle,5,False)
    try:
        for i in range(5):
            print(f'trial {i+1}')
            for i in range (int(rerun_unloaded_lift_start[angle]*4),int((rerun_unloaded_lift_start[angle]+10)*4)):
                duty = i/4
                iLoop.goToAngle(angle,1,False)
                starting_angle = encoder.getAngle()
                motorDrive.setMotor(duty)
                time.sleep(1)
                if starting_angle + 2.0 < encoder.getAngle():
                    print(f'angle ={angle}, raise duty value ={duty}')
                    motorDrive.setMotor(0)
                    iLoop.goToAngle(angle-1,2,False)
                    time.sleep(1)
                    break
    finally: 
        motorDrive.setMotor(0)


    # if autoZero.autoZero(30) == False :
    #     print('not zeroed')
    #     autoZero.autoZero(30)
    # time.sleep(1)
    # iLoop.goToAngle(angle,5,False)
    # try:
    #     for i in range(5):
    #         print(f'trial {i+1}')
    #         for i in range (int(unloaded_drop_start[angle]*4),int((unloaded_drop_start[angle]-10)*4),-1):
    #             duty = i/4
    #             iLoop.goToAngle(angle,1,False)
    #             starting_angle = encoder.getAngle()
    #             motorDrive.setMotor(duty)
    #             time.sleep(1)
    #             if starting_angle - 2.0 > encoder.getAngle():
    #                 print(f'drop duty value ={duty}')
    #                 motorDrive.setMotor(0)
    #                 iLoop.goToAngle(angle-1,2,False)
    #                 time.sleep(1)
    #                 break
    # finally: 
    #     motorDrive.setMotor(0)