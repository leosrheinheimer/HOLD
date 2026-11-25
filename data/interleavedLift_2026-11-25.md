# Interleaved lift re-test (Nov 25, 2026)

**Purpose:** separate drift from load-dependent friction. On Nov 21 the loaded set ran about an hour before the unloaded set.
**Rig:** Arm Mk3.1, load at the 300 mm hole (mass not re-weighed this session; intended 43.44 g). Supply 12.0 V, 0.5 A limit. `duty_LIMIT` 30%.
**Method:** per angle: `autoZero`, 5 s move to the angle, 3 unloaded lift trials, load added during a 20 s countdown, 5 s re-settle, 3 loaded lift trials, load removed. 0.25% steps, 1 s per step, re-level before each step, 2° threshold. No warm-up lifts.
**Sessions:** 0–60° in one run (about 10:35–11:05 am); 75° separately (about 1:40 pm).
**Aborted first attempt:** the load was left on during the first unloaded set at 0°; no thresholds were found (the search topped out at 19.5%). Not used.

## Search starts used (%)

| Angle (°) | Unloaded lift | Loaded lift |
|---|---|---|
| 0 | 9.75 | 16.25 |
| 15 | 7.0 | 16.75 |
| 30 | 5.75 | 16.25 |
| 45 | 5.0 | 11.25 |
| 60 | 3.25 | 8.5 |
| 75 | 2.25 | 3.0 |

## Raw lift thresholds (% duty)

| Angle (°) | Unloaded | Loaded |
|---|---|---|
| 0 | 13.5, 13.75, 13.5 | 24.0, 24.0, 24.0 |
| 15 | 12.75, 15.0, 14.5 | 25.75, 25.75, 25.75 |
| 30 | 12.25, 12.5, 10.25 | 21.0, 19.75, 20.5 |
| 45 | 9.0, 10.25, 11.5 | 17.0, 17.0, 17.0 |
| 60 | 8.0, 8.75, 8.5 | 13.25, 16.5, 13.5 |
| 75 | 7.25, 5.75, 7.0 | ~~3.25~~, 10.5, 7.25 |

**Invalid:** 75° loaded trial 1 (3.25%, second step after the start, right after loading; the arm was likely still settling).

## Summary

| Angle (°) | Unloaded mean (spread) | Loaded mean (spread) | Shift (%) | Measured (mN·m) | Predicted (mN·m) | Error | Predicted ÷ measured |
|---|---|---|---|---|---|---|---|
| 0 | 13.58 (0.25) | 24.0 (0) | 10.42 | 290.6 | 127.8 | +127% | 0.44 |
| 15 | 14.08 (2.25) | 25.75 (0) | 11.67 | 325.5 | 123.4 | +164% | 0.38 |
| 30 | 11.67 (2.25) | 20.42 (1.25) | 8.75 | 244.1 | 110.7 | +121% | 0.45 |
| 45 | 10.25 (2.5) | 17.0 (0) | 6.75 | 188.3 | 90.4 | +108% | 0.48 |
| 60 | 8.42 (0.75) | 14.42 (3.25) | 6.0 | 167.4 | 63.9 | +162% | 0.38 |
| 75 | 6.67 (1.5) | 8.88 (3.25, n = 2) | 2.21 | 61.6 | 33.1 | +86% | 0.54 (low confidence) |

Torque uses the locked slope, 27.9 mN·m per %. The Nov 21 recalibration (29.0) would raise every measured value by 4%.

## Notes

- **Interleaving did not reduce the error.** It's larger than Nov 21 (+41 to +111%). Drift was not the main cause.
- **The ratio predicted ÷ measured is consistent, at 0.38–0.48 (mean about 0.43, 0–60°).** Consistent with gearbox efficiency: lifting requires gravity torque ÷ η.
- **Unloaded lifts match Nov 21** (13.58 against 13.81 at 0°). **Loaded lifts are about 4% higher** (24.0 against 20.25 at 0°; 25.75 against 21.0 at 15°). The load mass was not re-weighed this session; to confirm.
- **75° is noise-limited:** the predicted signal (1.19% duty) is about the size of the threshold spread, as the lock anticipated.
- **Next:** interleaved drop sets, to test the efficiency explanation (the predicted drop shift should come out smaller than gravity, not larger).