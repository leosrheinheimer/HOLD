# Angle sweep: unloaded (Nov 21, 2026)

**Rig:** Arm Mk3.1 (49.03 g, CoM 136 mm), no load. Supply 12.0 V, 0.5 A limit. `duty_LIMIT` 30%.
**Method:** same as the loaded run (`sweepLoaded_2026-11-21.md`): `autoZero`, 5 s move to the angle, lift and drop threshold searches, 0.25% steps, 1 s per step, re-level before each step, threshold = 2° of motion, 5 trials each.
**Timing:** run 8:36–9:26 pm, after the loaded run (7:51–8:31 pm).

## Search starts used

| Angle (°) | Lift start (%) | Drop start (%) |
|---|---|---|
| 0 | 12.25 | 4.0 |
| 15 | 13.0 → rerun 8.0 | 3.25 |
| 30 | 12.25 → rerun 7.0 | 3.5 |
| 45 | 7.25 | 3.0 |
| 60 | 4.5 | 2.25 |
| 75 | 0.75 | 0.0 |

**Invalid:**
- Lift at 15° (5 × 13.0) and 30° (5 × 12.25) triggered on the first step every trial, so the threshold was below the start. Rerun with lower starts; the rerun values are below.
- Lift at 0°, trial 1 (12.25 = start), excluded. Trials 2–5 are valid.

## Raw thresholds (% duty)

| Angle (°) | Lift trials | Drop trials |
|---|---|---|
| 0 | ~~12.25~~, 14.0, 13.75, 13.75, 13.75 | −1.75, −1.0, −1.0, −1.0, −1.0 |
| 15 | 12.0, 11.0, 12.0, 11.25, 12.0 (rerun) | −1.0, −1.0, −1.0, −1.0, −1.0 |
| 30 | 9.75, 11.0, 14.0, 14.0, 14.25 (rerun) | −1.5, −1.5, −1.5, −1.5, −1.5 |
| 45 | 9.0, 9.0, 9.0, 9.0, 9.0 | −1.5, −1.25, −1.25, −1.25, −1.25 |
| 60 | 8.25, 7.75, 8.0, 8.0, 7.25 | −2.5, −2.0, −2.0, −2.0, −2.0 |
| 75 | 6.25, 6.25, 6.25, 6.25, 6.25 | −3.75, −2.25, −2.25, −2.25, −2.25 |

## Summary

| Angle (°) | Lift mean | Lift spread | Drop mean | Drop spread | Band width | Midpoint |
|---|---|---|---|---|---|---|
| 0 | 13.81 (trials 2–5) | 0.25 | −1.15 (−1.0 without trial 1) | 0.75 | 14.96 | 6.33 |
| 15 | 11.65 | 1.0 | −1.0 | 0 | 12.65 | 5.33 |
| 30 | 12.6 | **4.5** | −1.5 | 0 | 14.1 | 5.55 |
| 45 | 9.0 | 0 | −1.3 | 0.25 | 10.3 | 3.85 |
| 60 | 7.85 | 1.0 | −2.1 | 0.5 | 9.95 | 2.88 |
| 75 | 6.25 | 0 | −2.55 (−2.25 without trial 1) | 1.5 | 8.8 | 1.85 |

## Notes

- **30° lift is unreliable:** the trials climbed 9.75 → 14.25 during the set.
- **Drift:** unloaded lift at 0° was 16.4% at about 6:25 pm (friction-band test) and 13.81% here at about 8:40 pm. The loaded run came first, so the halves were measured at different friction levels.
- **Trial-1 outliers** again at 0° (lift and drop) and 75° (drop).

## Comparison with the locked prediction (`prediction.md`)

Load torque (mN·m), using the stall calibration slope of 27.9 mN·m per %:

| Angle (°) | Predicted | Headline: lift shift | Error | Midpoint shift | Error |
|---|---|---|---|---|---|
| 0 | 127.8 | 179.6 | +41% | 134.4 | +5% |
| 15 | 123.4 | 260.9 | +111% | 161.1 | +31% |
| 30 | 110.7 | 213.4 | +93% | 147.2 | +33% |
| 45 | 90.4 | 175.8 | +95% | 120.0 | +33% |
| 60 | 63.9 | 131.1 | +105% | 99.0 | +55% |
| 75 | 33.1 | 67.0 | +102% | 41.2 | +24% |

- **Outside the locked 20%** on the headline at every angle.
- From 45° to 75° the headline ratio is a near-constant ~2×, which would fit a calibration slope that is wrong at breakaway.
- **Next:** check the scale against nickels, recalibrate on Mk3.1 stepping up and down, recompute alongside this table, then an interleaved loaded/unloaded re-test.