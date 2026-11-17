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

## Motor drive and sign convention

- **PWM:** 20 kHz on GP14. The PWM frequency is separate from the control-loop rate.
- **Command:** `setMotor(command)` takes a signed percent. The sign sets DIR; the magnitude sets duty, clamped to `duty_LIMIT`.
- **Duty cap (`duty_LIMIT`):** 50% since Nov 16 (20% on Nov 6, 30% from Nov 7). The PI loop's anti-windup cap follows it.
- **Sign convention:** a positive command sets DIR = 1, turns the arm CCW, and increases the encoder count and angle. Holding against gravity takes a positive command.
- **Supply:** bench supply at 12.0 V with a 0.5 A current limit (confirmed Nov 6).

## Position control loop: `goToAngle()` in `pico/iLoop.py` (Nov 9–14, 2026)

| Setting | Value |
|---|---|
| Kp | 1 (% duty per degree) |
| Ki | 3 |
| Integral limit | 20% duty (integral clamped to ±20 / Ki) |
| Hold band | ±2°: command 0 and integral frozen inside it |
| Anti-windup | integral frozen while the previous command is at the duty cap |
| Loop rate | set to 100 Hz; measured about 85 Hz (each pass 11–12 ms) |
| Timing | `time.ticks_us()` with `ticks_diff` |

## INA219 accuracy check (Oct 24, 2026). Sensor dropped Nov 7.

- **Setup:** 3.3 V rail → Vin+ → shunt → Vin− → test resistor → GND.
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

Arm off, motor unloaded. Smallest duty that starts motion.

| Direction | Positive first | Negative first | All 7 runs |
|---|---|---|---|
| Positive (CCW) | 5, 4, 6, 5% | 5, 6, 6% | 4–6%, mean 5.3% |
| Negative (CW) | 4, 4, 4% | 4, 5, 4% | 4–5%, mean 4.2% |

This is breakaway friction with no gravity load. It is not the holding friction band (see Not yet measured).

## Arm Mk2 mass properties (Nov 14, 2026)

| Component | Mass (g) | Distance from shaft (mm) |
|---|---|---|
| Arm Mk2 (at its CoM) | 35.50 | 76 |
| Bolt + nut, mount 1 | 10.71 | 100 |
| Bolt + nut, mount 2 | 10.71 | 149.5 |
| Dowel pin (mass assumed) | 2 | 120 |
| goBILDA 1309 hub | 14.22 | 0 (on the axis, adds no gravity torque) |
| **Arm + fixed hardware (hub excluded)** | **58.92** | **95.22 (combined CoM)** |

- **Arm weight at the 118 mm scale point:** 47.6 g (computed with mount 2 at 150 mm; 47.5 g with 149.5 mm, a negligible difference).
- **Test load:** 3 large washers, 30.60 g (10.20 g ± 0.02 g each), on mount 2 at 149.5 mm.

## Gearbox backlash (Nov 14, 2026)

- **Method:** arm held at the motor, tip rocked by hand, vertical free play measured at 125 mm.
- **Result:** about 8.5 mm of play at 125 mm. arctan(8.5 / 125) ≈ 3.9°, so about 4°.
- **Effect:** the encoder sits on the motor side, so it reads the motor's position within this slop, not the arm's.

## Zero pin (Nov 14, 2026)

A 3/8 in bolt (0.3675 in, 9.33 mm measured) is the hard stop below level. The reading is the angle from the pin to level, taken with `pico/callibrateZero.py`.

| Placement | Trials (°) | Mean |
|---|---|---|
| Gentle | 11, 10.5, 10.5 | 10.7° |
| Hard ("slam") | 14, 14.5, 14.5, 14.5 | 14.4° |

- **Chosen method:** hard slam, repeatable to about ±0.25°.
- **Why gentle and hard differ by about 3.7°:** backlash. A hard push drives the gears to the far side of their slop; a gentle placement leaves them anywhere inside it. The arm sits on the same pin both times.
- **Pin position (shaft centre to bolt centre):** not yet measured.

## Auto-zero: `autoZero()` in `pico/autoZero.py` (updated Nov 16, 2026)

1. Drives at −20% into the pin until the encoder reading stops changing for 0.3 s (4 s timeout).
2. At the pin, sets `encoder.zero_offset_ticks` with `ticksToDeg.zeroOffsetTicks()` so that `getAngle()` reads −14.4° there. Level is then 0°.
3. Drives to 0° with `goToAngle()`. Returns True; on timeout prints a failure, doesn't move, and returns False.

- **Expected result:** the arm stops up to about 2° below level (the loop's hold band), and `getAngle()` reports that true angle.
- **History:** the Nov 14 version never set the offset. It drove to `pin angle + 17°`, an empirical number that hid the loop's stopping error and was validated level to ±1° with a level.
- **Status:** new version not yet tested on the rig.

## Torque calibration: motor duty against scale force (Nov 14, 2026)

- **Setup:** the arm presses down on a kitchen scale at a 118 mm lever arm, duty stepped up from 4 to 22% in steps of 2. 4 trials per duty. Script: `pico/calibrateTorque.py`.
- **Motor force** = mean scale reading − 47.6 g (the arm's own weight at the scale).
- **Motor torque** = motor force × 9.81 × 0.118 m.
- **Data:** `data/dutyVsTorque.csv`.

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
- **Direction:** positive command only, the same direction as holding against gravity. Duty stepped up only; no down-step run yet.

## Gravity model check, Mk2 (Nov 16, 2026)

- **Predicted torque at horizontal** (`analysis/predictTorque.py`): 55.0 mN·m unloaded, 99.9 mN·m loaded.
- **Measured arm torque:** at 4% duty the motor adds about nothing, and the scale read 47.0 g at 118 mm = 54.4 mN·m. That's 1% below the prediction. Assumes the arm was level on the scale and the dowel pin weighs 2 g.
- **Predicted holding duty at horizontal** (from the fit): 6.3% unloaded, 7.9% loaded.
- **Load sizing:** peak loaded gravity torque is 23% of the highest measured motor torque (99.9 / 435 mN·m), below the 30–40% target. Load choice is pending the friction band.

## Not yet measured

- **Holding friction band** at horizontal, unloaded and with 3 washers: the sag-to-lift duty range. It decides the load and whether the washer-count demo can resolve single washers. To resolve one 10.20 g washer at radius r: r ≥ 279 mm × band width (% duty).
- **Zero pin position:** shaft centre to bolt centre.
- **Dowel pin mass** (2 g assumed).
- **Supply CC light at 20% and 22% duty.**
- **Calibration down-step run** (hysteresis).