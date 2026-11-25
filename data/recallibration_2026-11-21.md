# Torque recalibration (Nov 21, 2026)

**Rig:** Arm Mk3.1, contact at the 300 mm hole, scale on the 0° side, arm tilted slightly down (about 1 in drop over 300 mm, roughly 5°; not measured with the encoder).
**Direction:** negative command (pressing down, with gravity). The sweep's lift thresholds use the positive direction.
**Scale check:** 5 quarters read 28.30 g (spec 28.35 g, 0.2% low).
**Arm weight at scale (W₀):** not recorded.
**Procedure:** duty stepped up 4 → 22% in 2% steps, one reading per step. No down-step run.

## Raw scale readings (g)

| Duty (%) | Run 0 (distrusted) | Run 1 | Run 2 | Run 3 |
|---|---|---|---|---|
| −4 | 45 | 43 | 39 | 40 |
| −6 | 56 | 61 | 60 | 56 |
| −8 | 82 | 80 | 78 | 82 |
| −10 | 99 | 106 | 106 | 101 |
| −12 | 115 | 118 | 115 | 117 |
| −14 | 112 | 121 | 108 | 123 |
| −16 | 130 | 115 | 123 | 119 |
| −18 | 141 | 122 | 130 | 124 |
| −20 | 148 | 132 | 136 | 127 |
| −22 | 152 | 140 | 137 | 123 |

## Results (runs 1–3)

- **Linear region, 4–12%:** slope 9.87 g per % (runs 9.75 / 9.90 / 9.95, R² 0.98–0.99) → **29.0 mN·m per %** at 300 mm (28.7 / 29.1 / 29.3). The Nov 14 value was 27.9: 4% apart.
- **Above 12%:** the force plateaus around 115–140 g and is non-monotonic. Not used.
- **Force decay:** at a held duty the reading fell about 1% per second (about 3% total per step). Not thermal (motor cold). Scale creep not yet ruled out.
- **Conclusion:** the calibration slope isn't the cause of the sweep's 2× miss.