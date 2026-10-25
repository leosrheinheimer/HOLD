import gravityTorque
import matplotlib.pyplot as plt
import constants

angles_deg = list(range(-90,91,5))
unloaded_torque_values = []
loaded_torque_values = []

for angle in angles_deg:
    loaded_torque_values.append(gravityTorque.gravityTorque(angle,constants.load_mass_kg, constants.load_radius_m, constants.arm_mass_kg, constants.arm_com_radius_m))
    unloaded_torque_values.append(gravityTorque.gravityTorque(angle, 0, constants.load_radius_m, constants.arm_mass_kg, constants.arm_com_radius_m))


plt.plot(angles_deg, loaded_torque_values, label="loaded")
plt.plot(angles_deg, unloaded_torque_values, label="unloaded")

plt.xlabel("Angle (deg)")
plt.ylabel("Torque Value (Nm)")
plt.title("Unloaded vs Loaded Torque Predictions, 3 Large Washers @10.20g Each")
plt.legend()
plt.grid(True)

plt.savefig("data/predicted_torque.png", dpi=150)
plt.show()