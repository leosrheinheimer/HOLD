import motorDrive
import encoder 
import time


for i in range(10) : 
    print('motor duty: '+ str(-i))
    motorDrive.setMotor(-i)
    for i in range (5) : 
        print(f'encoder angle {i} = {encoder.getAngle()}')
        time.sleep(0.1)
    print()
motorDrive.setMotor(0)

for i in range(10) : 
    print('motor duty: '+ str(i))
    motorDrive.setMotor(i)
    for i in range (5) : 
        print(f'encoder angle {i} = {encoder.getAngle()}')
        time.sleep(0.1)
    print()
motorDrive.setMotor(0)


