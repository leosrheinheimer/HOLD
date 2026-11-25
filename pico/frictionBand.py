import autoZero
import motorDrive
import iLoop
import encoder 
import time


unloaded_lift_start = {0: 9.75, 15: 7.0, 30: 5.75, 45: 5.0, 60: 3.25, 75: 2.25}
unloaded_drop_start = {0: 2.0, 15: 2.0, 30: 1.5, 45: 1.75, 60: 1.0, 75: 0.75}
loaded_lift_start = {0: 16.25, 15: 16.75, 30: 16.25, 45: 11.25, 60: 8.5, 75: 3.0}
loaded_drop_start = {0: 5.5, 15: 4.25, 30: 4.5, 45: 4.0, 60: 3.75, 75: 1.0}

motorDrive.setMotor(0)

autoZero.autoZero(30)

print('\a')


for angle in range(75,90,15):
    print(f'angle ={angle} degrees above horizontal')
    if autoZero.autoZero(30) == False :
        print('not zeroed')
        autoZero.autoZero(30)
    time.sleep(1)
    iLoop.goToAngle(angle,5,False)
    try:
        for i in range(3):
            print(f'trial {i+1}')
            for i in range (int(unloaded_lift_start[angle]*4),int((unloaded_lift_start[angle]+10)*4)):
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
        print('UNLOADED COMPLETE, LOAD WASHERS')
        for i in range(20):
            print(f'You have {20-i} seconds left to load the washers \a')
            time.sleep(1)
        print('COMMENCING LOADED TEST')
        iLoop.goToAngle(angle,5,False)

        for i in range(3):
            print(f'trial {i+1}')
            for i in range (int(loaded_lift_start[angle]*4),int((loaded_lift_start[angle]+10)*4)):
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
        
        print('LOADED COMPLETE, UNLOAD WASHERS')
        for i in range(20):
            print(f'You have {20-i} seconds left to unload the washers \a')
            time.sleep(1)
        print('COMMENCING UNLOADED TEST')

            
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