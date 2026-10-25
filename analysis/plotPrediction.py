import gravityTorque
import matplotlib.pyplot as plt
import math
import constants

angles_deg = list(range(-90,91,5))
unloaded_torque_values = []
loaded_torque_values = []

for angle in angles_deg:
    angle_rad = math.radians(angle)
    loaded_torque_values.append(gravityTorque.gravityTorque(180*angle_rad/math.pi,constants.load_mass_kg, constants.load_radius_m, constants.arm_mass_kg, constants.arm_com_radius_m))
    unloaded_torque_values.append(gravityTorque.gravityTorque(180*angle_rad/math.pi, 0, constants.load_radius_m, constants.arm_mass_kg, constants.arm_com_radius_m))


plt.plot(angles_deg, loaded_torque_values, label="loaded")
plt.plot(angles_deg, unloaded_torque_values, label="unloaded")

plt.xlabel("Angle (deg)")
plt.ylabel("Torque Value (Nm)")
plt.title("Unloaded vs Loaded Torque Predictions, Placeholder Values")
plt.legend()
plt.grid(True)

plt.savefig("data/predicted_torque.png", dpi=150)
plt.show()