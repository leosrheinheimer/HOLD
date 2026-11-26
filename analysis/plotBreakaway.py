# analysis/plotBreakaway.py
import numpy as np
import matplotlib.pyplot as plt

rawData = np.loadtxt("data/loadTorque.csv", delimiter=",", skiprows=1)
predictedMNm = rawData[:, 1]
liftShift1125MNm = rawData[:, 4]
dropShift1125MNm = rawData[:, 5]

stallTorquePerPct = 27.9
liftDuty = liftShift1125MNm / stallTorquePerPct
dropDuty = dropShift1125MNm / stallTorquePerPct

fitX = predictedMNm[:5]
liftSlope = np.sum(fitX * liftDuty[:5]) / np.sum(fitX * fitX)
dropSlope = np.sum(fitX * dropDuty[:5]) / np.sum(fitX * fitX)

liftTorquePerPct = 1.0 / liftSlope
dropTorquePerPct = 1.0 / dropSlope
geoMeanTorquePerPct = np.sqrt(liftTorquePerPct * dropTorquePerPct)

print(f"Lifting (breakaway): {liftTorquePerPct:.1f} mN·m per %")
print(f"Dropping (back-driven): {dropTorquePerPct:.1f} mN·m per %")
print(f"Geometric mean: {geoMeanTorquePerPct:.1f} mN·m per %")

xLine = np.array([0.0, 140.0])

plt.figure(figsize=(8, 5))
plt.plot(fitX, liftDuty[:5], color="tab:blue", marker="o", linestyle="None")
plt.plot(predictedMNm[-1], liftDuty[-1], color="tab:blue", marker="o", markerfacecolor="none", linestyle="None")
plt.plot(xLine, liftSlope * xLine, color="tab:blue", linestyle="-", label=f"Lifting (breakaway): {liftTorquePerPct:.1f} mN·m per %")

plt.plot(fitX, dropDuty[:5], color="tab:orange", marker="o", linestyle="None")
plt.plot(predictedMNm[-1], dropDuty[-1], color="tab:orange", marker="o", markerfacecolor="none", linestyle="None")
plt.plot(xLine, dropSlope * xLine, color="tab:orange", linestyle="-", label=f"Dropping (back-driven): {dropTorquePerPct:.1f} mN·m per %")

plt.plot(xLine, xLine / stallTorquePerPct, color="black", linestyle="--", label="Stall calibration: 27.9 mN·m per %")

plt.xlabel("Known load torque (mN·m)")
plt.ylabel("Duty shift (%)")
plt.title("HOLD: stall vs breakaway calibration")
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("data/breakawayCalibration.png", dpi=150)
plt.show()