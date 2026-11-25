# Interleaved drop re-test (Nov 25, 2026)

**Purpose:** test the gearbox-efficiency explanation for the lift-side miss. If losses in the gearbox cause it, lifting needs gravity torque ÷ η, while back-driving lets through only about gravity torque × η. So the drop shift should come out **smaller** than the predicted load torque, where the lift shift came out larger.
**Rig:** Arm Mk3.1, load 43.62 g (re-weighed today) at the 300 mm hole. Supply 12.0 V, 0.5 A limit. `duty_LIMIT` 30%.
**Method:** per angle: `autoZero`, 5 s move to the angle, 3 unloaded drop trials, load added during a 20 s countdown, 5 s re-settle, 3 loaded drop trials, load removed. Duty stepped **down** 0.25% per step, 1 s per step, re-level before each step. A drop is recorded when the arm falls more than 2° below the angle at the start of the step. Search span: start to start − 10%. No warm-up drops.
**Sessions:** 0–75° in one run (about 1:55–2:15 pm); 45° rerun (about 2:20 pm).
**Invalid first 45° set:** all six trials read 1.0%. The "unloaded" value sat off the trend between 30° (−1.67) and 60° (−2.5). Likely cause: the load was not removed after the 30° loaded set, so both 45° sets ran loaded. The rerun's unloaded value (−2.0) falls on the trend. Not used.

## Search starts used (%)

| Angle (°) | Unloaded drop | Loaded drop |
|---|---|---|
| 0 | 2.0 | 5.5 |
| 15 | 2.0 | 4.25 |
| 30 | 1.5 | 4.5 |
| 45 | 1.75 | 4.0 |
| 60 | 1.0 | 3.75 |
| 75 | 0.75 | 1.0 |

## Raw drop thresholds (% duty)

| Angle (°) | Unloaded | Loaded |
|---|---|---|
| 0 | −1.75, 1.0, 0.25 | 2.75, 1.75, 2.25 |
| 15 | −1.0, −1.0, −1.0 | 1.5, 1.5, 1.75 |
| 30 | −2.0, −1.5, −1.5 | 1.0, 1.0, 1.5 |
| 45 (rerun) | −2.0, −2.0, −2.0 | 0.75, 0.75, 0.75 |
| 45 (first set, invalid) | ~~1.0, 1.0, 1.0~~ | ~~1.0, 1.0, 1.0~~ |
| 60 | −2.5, −2.5, −2.5 | −1.25, −1.25, −1.25 |
| 75 | −3.5, −2.75, −2.75 | −1.75, −1.5, −1.5 |

No trial hit its search start or the end of its span.

## Summary: drop shift

| Angle (°) | Unloaded mean (spread) | Loaded mean (spread) | Shift (%) | Measured (mN·m) | Predicted (mN·m) | Error |
|---|---|---|---|---|---|---|
| 0 | −0.17 (2.75) | 2.25 (1.0) | 2.42 | 67.4 | 127.8 | −47% |
| 15 | −1.00 (0) | 1.58 (0.25) | 2.58 | 72.1 | 123.4 | −42% |
| 30 | −1.67 (0.5) | 1.17 (0.5) | 2.83 | 79.0 | 110.7 | −29% |
| 45 | −2.00 (0) | 0.75 (0) | 2.75 | 76.7 | 90.4 | −15% |
| 60 | −2.50 (0) | −1.25 (0) | 1.25 | 34.9 | 63.9 | −45% |
| 75 | −3.00 (0.75) | −1.58 (0.25) | 1.42 | 39.5 | 33.1 | +19% (low confidence) |

Torque uses the locked slope, 27.9 mN·m per %.

## Combined with the interleaved lifts (same day)

| Angle (°) | Lift shift (mN·m) | Drop shift (mN·m) | Midpoint (mN·m) | Midpoint error | √(lift × drop) (mN·m) | √ error | Implied η = √(drop ÷ lift) |
|---|---|---|---|---|---|---|---|
| 0 | 290.6 | 67.4 | 179.0 | +40% | 140.0 | +10% | 0.48 |
| 15 | 325.5 | 72.1 | 198.8 | +61% | 153.2 | +24% | 0.47 |
| 30 | 244.1 | 79.0 | 161.6 | +46% | 138.9 | +26% | 0.57 |
| 45 | 188.3 | 76.7 | 132.5 | +47% | 120.2 | +33% | 0.64 |
| 60 | 167.4 | 34.9 | 101.1 | +58% | 76.4 | +20% | 0.46 |
| 75 | 61.6 | 39.5 | 50.6 | +53% | 49.3 | +49% | 0.80 (low confidence) |

## Notes

- **The efficiency test passed, in direction.** From 0° to 60° the drop shift is 15–47% **below** the predicted load torque, while the lift shift is 108–164% **above** it. A fixed offset or a wrong calibration slope would move both sides the same way. An error that splits by direction is the signature of gearbox losses.
- **Implied efficiency is 0.46–0.64 (0–60°).** This is computed by assuming the same η lifting and back-driving. It is close to the 0.43 estimated from the lift data alone.
- **The √(lift × drop) estimate is post-hoc.** It cancels a symmetric η. It reads +10% to +33% against the prediction (0–60°), against +108% to +164% for the locked lift-shift method. It is reported alongside the locked result, not in its place.
- **Some error remains unexplained.** The midpoint still reads 40–61% high. Lift error × drop error is 1.2–1.8, not the 1.0 that symmetric efficiency would give. Possible causes: the gearbox loses more lifting than back-driving, or a remaining scale error of about 20%. The Nov 21 recalibration slope (29.0) would add 4%, not remove it.
- **0° unloaded is noisy:** a 2.75% spread, against 0–0.75% at the other angles.
- **75° is noise-limited:** the predicted signal (1.19% duty) is about the size of the threshold spread, as the lock anticipated.