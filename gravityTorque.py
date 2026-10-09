import math
G = 9.81

## 0 deg is horizontal, positive torque is pulling the same direction gravity pulls at 0 deg
def gravityTorque(angle_deg, load_mass_kg, load_radius_m, arm_mass_kg, arm_com_radius_m):
    angle_rad = angle_deg * math.pi / 180
    load_torque_nm = load_radius_m * load_mass_kg * math.cos(angle_rad) * G
    arm_torque_nm = arm_com_radius_m * arm_mass_kg * math.cos(angle_rad) * G
    net_torque_nm = arm_torque_nm + load_torque_nm
    return net_torque_nm 