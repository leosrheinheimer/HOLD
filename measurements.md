# Measurements

## Encoder ticks per output-shaft turn (Oct 10, 2026)

- **Result:** 1245.5 ticks per output-shaft turn.
- **What counts as a tick:** every rising and falling edge of channel A, with direction taken from channel B. `pico/encoder.py` counts this way, using a hard interrupt.
- **Method:** a locking plier clamped on the output shaft as a handle and pointer. 10 full turns per trial, stopping on a fixed mark.
- **Trials:** 12453 and 12457 ticks over 10 turns. They differ by 4 counts (0.03%).
- **Resolution:** 360 / 1245.5 = 0.289° per tick.
- **Cross-check:** the interrupt counter read 2489 over 2 turns (expected 2491) and 6227 over 5 fast turns (expected 6227.5).
- **Against the listing:** the seller's specs imply 748 (11 pulses × 2 edges × 34:1 gearbox). The measured value is 66% higher. How it splits between encoder pulses and gear ratio is unknown. The rig only uses the product.
- **Placement:** the encoder is on the motor side of the gearbox, so gearbox backlash shows up in the reading (see Backlash).

## Pin map (updated Nov 14, 2026, after the rewire)

- **Encoder:** yellow on GP2, green on GP3, blue on 3V3, black on GND.
- **MD10C (motor controller):** PWM (orange) on GP14, DIR (brown) on GP15, GND (black) to the rail.
- **INA219:** removed Nov 7. Current sensing dropped (see INA219 section).

## Motor drive and sign convention (Nov 7, 2026)

- **PWM:** 20 kHz on GP14. The PWM frequency is separate from the control-loop rate.
- **Command:** `setMotor(command)` takes a signed percent. The sign sets DIR; the magnitude sets duty, clamped to `duty_LIMIT` = 20%.
- **Sign convention:** a positive command sets DIR = 1, turns the arm CCW, and increases the encoder count and angle.
- **Supply:** bench supply with a 0.5 A current limit (confirmed Nov 6).

## INA219 accuracy check (Oct 24, 2026). Sensor dropped Nov 7.

- **Setup:** 3.3 V rail → Vin+ → shunt → Vin− → test resistor → GND. Readings from `pico/readINA219.py`.
- **Zero check:** with no resistor, current reads 0.0 mA (±0.2 mA). No offset.
- **Bus voltage:** 3.260–3.268 V.
- **Shunt:** marked R100 (0.1 Ω).

| Resistor (kit values: 220R / 1k / 10k) | Expected (3.26 V ÷ R) | Measured | Ratio |
|---|---|---|---|
| 220 Ω | 14.8 mA | 18.2–18.6 mA | 1.24 |
| 1 kΩ | 3.27 mA | 3.9–4.4 mA | ~1.28 |
| 10 kΩ | 0.33 mA | 0.2–0.6 mA | ~1.3 (noisy) |

- **Result:** reads about 25% high, roughly constant across all three resistors. That's far outside the INA219's ~1% spec.
- **Cause:** unresolved. The resistor colour bands were hard to read, and values were matched to the kit listing.
- **Outcome:** the sensor was removed after a short on the 12 V line. Torque-from-current was dropped from scope. Torque is measured directly against the scale instead (see Torque calibration).

## Deadband test (Nov 7, 2026)

Motor unloaded. Smallest duty that starts motion.

| Direction | Positive first | Negative first | All 7 runs |
|---|---|---|---|
| Positive (CCW) | 5, 4, 6, 5% | 5, 6, 6% | 4–6%, mean 5.3% |
| Negative (CW) | 4, 4, 4% | 4, 5, 4% | 4–5%, mean 4.2% |

## Arm Mk2 mass properties (Nov 14, 2026)

| Component | Mass (g) | Distance from shaft (mm) |
|---|---|---|
| Arm Mk2 (at its CoM) | 35.50 | 76 |
| Bolt + nut, mount 1 | 10.71 | 100 |
| Bolt + nut, mount 2 | 10.71 | 149.5 |
| Dowel pin (mass assumed) | 2 | 120 |
| goBILDA 1309 hub | 14.22 | 0 (on the axis, adds no gravity torque) |

- **Arm weight at the 118 mm scale point:** 47.6 g (computed with mount 2 at 150 mm; 47.5 g with 149.5 mm, a negligible difference).

## Gearbox backlash (Nov 14, 2026)

- **Method:** arm held at the motor, tip rocked by hand, vertical free play measured at 125 mm.
- **Result:** about 8.5 mm of play at 125 mm. arctan(8.5 / 125) ≈ 3.9°, so about 4°.
- **Effect:** the encoder sits on the motor side, so it reads the motor's position within this slop, not the arm's.

## Zero pin (Nov 14, 2026)

A 3/8 in bolt is the hard stop. The reading is the angle from the pin to level.

| Placement | Trials (°) | Mean |
|---|---|---|
| Gentle | 11, 10.5, 10.5 | 10.7° |
| Hard ("slam") | 14, 14.5, 14.5, 14.5 | 14.4° |

- **Chosen method:** hard slam, repeatable to about ±0.25°.
- **Why gentle and hard differ by about 3.7°:** backlash. A hard push drives the gears to the far side of their slop; a gentle placement leaves them anywhere inside it. The arm sits on the same pin both times.
- **`autoZero()`:** drives at −20% into the pin, detects 0.3 s with no change in the encoder, then commands `pin angle + 17°`. Validated level to ±1° with a level. The 17° (against the measured 14.4°) is empirical. It absorbs backlash plus where the PI loop stops inside its ±2° band.

## Torque calibration: motor duty against scale force (Nov 14, 2026)

- **Setup:** the arm presses down on a kitchen scale at a 118 mm lever arm. 4 trials per duty.
- **Motor force** = mean scale reading − 47.6 g (the arm's own weight at the scale).
- **Motor torque** = motor force × 9.81 × 0.118 m.
- **Data:** `data/` (CSV).

| Duty (%) | Trials (g) | Mean (g) | Std dev (g) | Motor force (g) | Motor torque (N·m) |
|---|---|---|---|---|---|
| 4 | 47, 47, 47, 47 | 47.0 | 0.0 | −0.6 | −0.0007 |
| 6 | 95, 94, 95, 97 | 95.3 | 1.3 | 47.7 | 0.0552 |
| 8 | 135, 132, 130, 135 | 133.0 | 2.4 | 85.4 | 0.0989 |
| 10 | 185, 183, 180, 182 | 182.5 | 2.1 | 134.9 | 0.1562 |
| 12 | —, 224, 223, 221 | 222.7 | 1.5 | 175.1 | 0.2027 |
| 14 | 275, 270, 275, 279 | 274.8 | 3.7 | 227.2 | 0.2630 |
| 16 | 330, 340, 340, 333 | 335.8 | 5.1 | 288.2 | 0.3336 |
| 18 | 375, 378, 381, 380 | 378.5 | 2.6 | 330.9 | 0.3831 |
| 20 | 405, 408, 404, 402 | 404.8 | 2.5 | 357.2 | 0.4134 |
| 22 | 425, 435, 415, 420 | 423.8 | 8.5 | 376.2 | 0.4354 |

- **Trial 1 at 12%:** excluded as an outlier.
- **Linear fit, 6–18%:** torque ≈ 27.9 mN·m per % × (duty − 4.3%). R² = 0.996.
- **Zero-torque duty:** about 4.3%, consistent with the deadband test.
- **Above 18%:** the curve flattens. Suspected cause: the supply's 0.5 A current limit. Unconfirmed.
- **Note:** the 4% point sits on the zero intercept and is left out of the fit.