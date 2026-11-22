import autoZero 
import iLoop
import encoder
import motorDrive

duty_data = []
scale_data = []
autoZero.autoZero(30)
current_angle = encoder.getAngle()
zero_angle = current_angle 
iLoop.goToAngle(zero_angle ,1,False)
try:
    for duty_value in range(-4,-24,-2):
        motorDrive.setMotor(duty_value)
        scale_value = float(input(f'motor duty: {duty_value}, scale value (grams) = '))
        motorDrive.setMotor(0)
        duty_data.append(duty_value)
        scale_data.append(scale_value)

        iLoop.goToAngle(zero_angle ,3,False)
finally:
    motorDrive.setMotor(0)
print('duty_data:')
print(duty_data)
print('scale data:')
print(scale_data)

