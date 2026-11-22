import autoZero
import motorDrive
import iLoop
import encoder 
import time


motorDrive.setMotor(0)

# if autoZero.autoZero(30) == False :
#     print('not zeroed')
# time.sleep(1)
# try:
#     for i in range(5):
#         print(f'trial {i+1}')
#         for i in range (19*4,30*4):
#             duty = i/4
#             iLoop.goToAngle(0,1,False)
#             starting_angle = encoder.getAngle()
#             motorDrive.setMotor(duty)
#             time.sleep(1)
#             if starting_angle + 2.0 < encoder.getAngle():
#                 print(f'raise duty value ={duty}')
#                 motorDrive.setMotor(0)
#                 iLoop.goToAngle(-1,2,False)
#                 time.sleep(1)
#                 break
# finally: 
#     motorDrive.setMotor(0)


if autoZero.autoZero(30) == False :
    print('not zeroed')
time.sleep(1)
try:
    for i in range(5):
        print(f'trial {i+1}')
        for i in range (-5*4,30*4):
            duty = -i/4
            iLoop.goToAngle(0,1,False)
            starting_angle = encoder.getAngle()
            motorDrive.setMotor(duty)
            time.sleep(1)
            if starting_angle - 2.0 > encoder.getAngle():
                print(f'drop duty value ={duty}')
                motorDrive.setMotor(0)
                iLoop.goToAngle(-1,2,False)
                time.sleep(1)
                break
finally: 
    motorDrive.setMotor(0)