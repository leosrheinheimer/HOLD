import encoder 
import servoDrive as servo

#MANUAL METHOD:
servo.extend_pin()
print(f'current angle is {encoder.getAngle()} degrees')
print()
input('enter y when arm is level...')
zero_angle = encoder.getAngle()
print('level angle saved.')
print()
input('enter y when touching zeroing bolt...')
zeroing_bolt_angle = encoder.getAngle()
angle_diff = zero_angle - zeroing_bolt_angle
print(angle_diff)