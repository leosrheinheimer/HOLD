import motorDrive
import encoder 
import time

print('test starting')
motorDrive.setMotor(20)
for i in range (50) : 
    print(f'motor degrees: {encoder.getAngle()}')
    time.sleep(0.1)
motorDrive.setMotor(0)
print('test complete')