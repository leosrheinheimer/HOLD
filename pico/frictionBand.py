import autoZero
import motorDrive
import iLoop
import encoder 
import time

loaded_lift_start = {0: 17.0, 15: 16.75, 30: 16.0, 45: 15.0, 60: 13.5, 75: 11.75}
loaded_drop_start = {0: 4.75, 15: 4.5, 30: 4.0, 45: 3.25, 60: 2.25, 75: 1.25}

motorDrive.setMotor(0)

for angle in range(0,90,15):
    print(f'angle ={angle} degrees above horizontal')
    if autoZero.autoZero(30) == False :
        print('not zeroed')
        autoZero.autoZero(30)
    time.sleep(1)
    try:
        for i in range(5):
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
    finally: 
        motorDrive.setMotor(0)


    if autoZero.autoZero(30) == False :
        print('not zeroed')
        autoZero.autoZero(30)
    time.sleep(1)
    try:
        for i in range(5):
            print(f'trial {i+1}')
            for i in range (int(loaded_drop_start[angle]*4),int((loaded_drop_start[angle]-10)*4),-1):
                duty = i/4
                iLoop.goToAngle(angle,1,False)
                starting_angle = encoder.getAngle()
                motorDrive.setMotor(duty)
                time.sleep(1)
                if starting_angle - 2.0 > encoder.getAngle():
                    print(f'drop duty value ={duty}')
                    motorDrive.setMotor(0)
                    iLoop.goToAngle(angle-1,2,False)
                    time.sleep(1)
                    break
    finally: 
        motorDrive.setMotor(0)