import gravityTorque 
import constants

test_angles_deg = [-90,-45,0,45,90]
unloaded_torque_values = []
loaded_torque_values = []

print("Angle(deg), Unloaded Torque(Nm), Loaded Torque(Nm)")

with open("data/torque_predictions.csv", "w") as f:
    f.write("angle, unloaded_torque, loaded_torque" "\n")
    for angle in test_angles_deg: 
        current_loaded_torque = gravityTorque.gravityTorque(angle,constants.load_mass_kg, constants.load_radius_m, constants.arm_mass_kg, constants.arm_com_radius_m)
        current_unloaded_torque = gravityTorque.gravityTorque(angle, 0, constants.load_radius_m, constants.arm_mass_kg, constants.arm_com_radius_m)
        loaded_torque_values.append(current_loaded_torque)
        unloaded_torque_values.append(current_unloaded_torque)
        print("%.1f, %.4f, %.4f" % (angle, current_unloaded_torque, current_loaded_torque))
        f.write("%.1f, %.4f, %.4f\n" % (angle, current_unloaded_torque, current_loaded_torque))
