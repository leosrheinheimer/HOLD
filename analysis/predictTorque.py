import gravityTorque 

arm_mass_kg = 0.030
arm_com_radius_m = 0.075
load_mass_kg = 0.050
load_radius_m = 0.150
test_angles_deg = [-90,-45,0,45,90]

print("Angle(deg), Unloaded Torque(Nm), Loaded Torque(Nm)")

for angle in test_angles_deg: 
    loaded_torque_nm= gravityTorque.gravityTorque(angle, load_mass_kg, load_radius_m, arm_mass_kg, arm_com_radius_m)
    unloaded_torque_nm= gravityTorque.gravityTorque(angle, 0, load_radius_m, arm_mass_kg, arm_com_radius_m)
    print("%.1f, %.4f, %.4f" % (angle, unloaded_torque_nm, loaded_torque_nm))
    