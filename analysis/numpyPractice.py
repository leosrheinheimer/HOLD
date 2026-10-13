import numpy as np
import matplotlib.pyplot as plt

angles_deg = np.arange(-90,91,1)
angles_rad = np.radians(np.arange(-90,91,1))
cos_angles = np.cos(angles_rad)
sin_angles = np.sin(angles_rad)

plt.plot(angles_deg, sin_angles, label="sin")
plt.plot(angles_deg,cos_angles, label="cos")

plt.xlabel("Angle (deg)")
plt.ylabel("cos and sin values")
plt.title("degrees vs sin/cos values")
plt.grid(True)
plt.legend()
plt.show()