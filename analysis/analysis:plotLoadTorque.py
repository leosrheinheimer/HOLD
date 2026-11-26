# analysis/plotLoadTorque.py
import numpy as np
import matplotlib.pyplot as plt

rawData = np.loadtxt("data/loadTorque.csv", delimiter=",", skiprows=1)
angleDeg = rawData[:, 0]
predictedMNm = rawData[:, 1]
liftShift1121MNm = rawData[:, 2]
dropShift1121MNm = rawData[:, 3]
liftShift1125MNm = rawData[:, 4]
dropShift1125MNm = rawData[:, 5]
geoMean1125MNm = rawData[:, 6]

thetaDeg = np.arange(0, 76, 1)
thetaRad = np.deg2rad(thetaDeg)
smoothPredictedMNm = 127.8 * np.cos(thetaRad)

plt.figure(figsize=(8, 5))
plt.fill_between(angleDeg, dropShift1125MNm, liftShift1125MNm, color="tab:blue", alpha=0.3, label="Nov 25 lift–drop band (interleaved)")
plt.plot(angleDeg, liftShift1121MNm, color="tab:orange", linestyle="--", label="Nov 21 lift–drop band (locked test)")
plt.plot(angleDeg, dropShift1121MNm, color="tab:orange", linestyle="--")
plt.plot(thetaDeg, smoothPredictedMNm, color="black", linestyle="-", linewidth=2, label="Predicted (statics model)")
plt.plot(angleDeg[:-1], geoMean1125MNm[:-1], color="tab:blue", marker="o", linestyle="None", label="Nov 25 √(lift × drop)")
plt.plot(angleDeg[-1], geoMean1125MNm[-1], color="tab:blue", marker="o", markerfacecolor="none", linestyle="None", label="75° point (noise-limited)")

plt.xlabel("Arm angle above horizontal (°)")
plt.ylabel("Load torque (mN·m)")
plt.title("HOLD: predicted vs measured load torque")
plt.xticks(np.arange(0, 76, 15))
plt.ylim(bottom=0)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("data/loadTorque.png", dpi=150)
plt.show()