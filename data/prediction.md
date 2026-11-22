# HOLD: Locked prediction

**Committed:** Nov 21, 2026, before any angle sweep data. Model: `analysis/predictTorque.py` (statics, τ = m·g·r·cos θ).

## Setup

| Item | Value |
|---|---|
| Arm | Mk3.1, 49.03 g, centre of mass 136 mm from the shaft |
| Load | 43.44 g at the 300 mm hole |
| Motor calibration | 27.9 mN·m per % duty (stall calibration, Nov 14) |

## Predicted gravity torque (mN·m)

| Angle (°) | Arm only | Arm + load | Load alone | Load alone as duty (%) |
|---|---|---|---|---|
| 0 | 65.4 | 193.3 | 127.8 | 4.58 |
| 15 | 63.2 | 186.7 | 123.5 | 4.43 |
| 30 | 56.7 | 167.4 | 110.7 | 3.97 |
| 45 | 46.3 | 136.7 | 90.4 | 3.24 |
| 60 | 32.7 | 96.6 | 63.9 | 2.29 |
| 75 | 16.9 | 50.0 | 33.1 | 1.19 |

## Method

- **Angles:** 0, 15, 30, 45, 60, 75°.
- **At each angle,** unloaded and loaded: measure the friction band with the same process as `pico/frictionBand.py` (lift and drop thresholds, 0.25% steps, 2° motion threshold), 5 trials each.
- **Headline result: load torque.** (Loaded lift − unloaded lift) × 27.9 mN·m per %, against the "Load alone" column. Friction mostly cancels in the difference.
- **Secondary result: total torque.** Midpoint of lift and drop, converted with the calibration, against the "Arm only" and "Arm + load" columns.

## Expected error

- **Within 20%** overall. **Within 10%** if the motor calibration holds at breakaway. The calibration was taken in stall, and breakaway friction is larger.
- If the error exceeds 10%, I'll retest the motor torque. Any recalibrated result will be reported alongside this one, not in place of it.
- Expect the % error to grow with angle: at 75° the load signal (1.19% duty) is about the size of the threshold spread (0.25–1.25%).

## Disclosure

The 0° point was measured on Nov 21, before this commit: lift shift 4.7% duty = 131 mN·m measured, against 127.8 predicted (+2.6%). The other five angles are untested.