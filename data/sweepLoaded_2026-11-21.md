# Angle sweep: loaded (Nov 21, 2026)

**Rig:** Arm Mk3.1 (49.03 g, CoM 136 mm) + load 43.44 g at 300 mm. Supply 12.0 V, 0.5 A limit. `duty_LIMIT` 30%.
**Method:** per `prediction.md`. At each angle: `autoZero`, 5 s move to the angle, then lift and drop threshold searches. 0.25% duty steps, 1 s per step, `goToAngle(angle, 1)` re-level before each step, threshold = 2° of motion. 5 trials each.
**Locked before this run:** `prediction.md`.

## Search starts used

| Angle (°) | Lift start (%) | Drop start (%) |
|---|---|---|
| 0 | 17.0 | 4.75 |
| 15 | 16.75 | 4.5 |
| 30 | 16.0 | 4.0 |
| 45 | 15.0 | 3.25 |
| 60 | 13.5 → rerun 6.0 | 2.25 |
| 75 | 11.75 → rerun 3.0 | 1.25 |

**Invalid first run:** lift at 60° (5 × 13.5) and 75° (5 × 11.75) triggered on the first step every trial, so the threshold was below the start. Rerun with lower starts; the rerun values are below.

## Raw thresholds (% duty)

| Angle (°) | Lift trials | Drop trials |
|---|---|---|
| 0 | 20.25, 20.25, 20.25, 20.25, 20.25 | 2.5, 2.0, 2.0, 1.75, 2.0 |
| 15 | 21.25, 21.0, 20.75, 21.0, 21.0 | 1.25, 1.25, 1.0, 1.25, 1.25 |
| 30 | 20.25, 20.25, 20.25, 20.25, 20.25 | 1.25, 1.5, 1.25, 1.5, 1.5 |
| 45 | 15.5, 15.25, 15.25, 15.25, 15.25 | 1.0, 1.0, 1.0, 1.0, 1.0 |
| 60 | 12.5, 12.5, 12.5, 12.75, 12.5 (rerun) | −0.25, 0.5, 0.0, 0.75, 0.5 |
| 75 | 7.0, 9.25, 9.25, 9.0, 8.75 (rerun) | −2.0, −2.0, −2.0, −2.0, −2.0 |

## Summary

| Angle (°) | Lift mean | Lift spread | Drop mean | Drop spread | Band width | Midpoint |
|---|---|---|---|---|---|---|
| 0 | 20.25 | 0 | 2.05 | 0.75 | 18.2 | 11.15 |
| 15 | 21.0 | 0.5 | 1.2 | 0.25 | 19.8 | 11.1 |
| 30 | 20.25 | 0 | 1.4 | 0.25 | 18.85 | 10.83 |
| 45 | 15.3 | 0.25 | 1.0 | 0 | 14.3 | 8.15 |
| 60 | 12.55 | 0.25 | 0.3 | 1.0 | 12.25 | 6.43 |
| 75 | 8.65 (9.06 without trial 1) | 2.25 (0.5 without trial 1) | −2.0 | 0 | 10.65 | 3.33 |

## Notes

- **Trial-1 outliers** recur: 75° lift trial 1 here (7.0), and 0° drop trial 1 in the Nov 21 friction-band test. Likely warm-up.
- **0° lift drift:** 21.1% in the friction-band test earlier the same day, 20.25% here.
- **The band narrows with angle,** about 19% → 11% as gravity torque falls. Possibly gear friction that scales with transmitted torque; to be checked against the unloaded run.
- Unloaded run: not yet done.