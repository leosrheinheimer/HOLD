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

## Pin map (updated Nov 18, 2026, baseplate rebuild)

- **Encoder:** yellow on GP2, green on GP3, blue on 3V3, black on GND.
- **MD10C (motor controller):** PWM (orange) on GP14, DIR (brown) on GP15, GND (black) to the rail.
- **Zero-pin servo:** signal (white) on GP13 (pin 17), red on VBUS (pin 40, 5 V), black on GND (pin 28). GP13 is on a different PWM slice from GP14/GP15, so its 50 Hz doesn't affect the motor's 20 kHz.
- **INA219:** removed Nov 7. Current sensing dropped (see INA219 section).

## Rig build (Nov 18, 2026)

- **Baseplate:** printed PLA plate carrying the motor, MD10C (three standoffs with heat-set inserts), breadboard and Pico, and the zero-pin servo. Screwed to the 2×4 through four counterbored holes.
- **Level reference:** the plate is not level. Its reading on the torpedo level is a per-session check that nothing has moved; the pin angle is measured against true level, so plate tilt is absorbed into it.
- **Wiring:** servo cable in a channel with retaining tabs; power leads zip-tied to printed anchors.

## Motor drive and sign convention

- **PWM:** 20 kHz on GP14. The PWM frequency is separate from the control-loop rate.
- **Command:** `setMotor(command)` takes a signed percent. The sign sets DIR; the magnitude sets duty, clamped to `duty_LIMIT`.
- **Duty cap (`duty_LIMIT`):** 50% since Nov 16 (20% on Nov 6, 30% from Nov 7). The PI loop's anti-windup cap follows it.
- **Sign convention:** a positive command sets DIR = 1, turns the arm CCW, and increases the encoder count and angle. Holding against gravity takes a positive command.
- **Supply:** bench supply at 12.0 V with a 0.5 A current limit (confirmed Nov 6). Highest draw seen: 0.25 A during the loaded lift tests at 21.25% duty (Nov 21). The CC light has never come on.

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

- **Large moves:** from +156° to 0° the command saturates at `duty_LIMIT`, overshoots the hold band, and needs about 2 s to settle back inside it.
- **Inside the hold band** the command is 0. Unloaded, gearbox friction alone holds the arm there; with the 43.44 g load at 300 mm it does not (drop threshold is positive, see Friction band).

## Servo: `pico/servoDrive.py` (Nov 18, 2026)

- **Signal:** 50 Hz (20 ms period); pulse width sets position.
- **Limits:** `duty_u16` 3000–7250 (0.92–2.21 ms), mapped linearly to 0–180°.
- **Positions:** retracted = 180° (also the power-up position), extended = 90°.

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

This is breakaway friction with no gravity load. Under gravity load the friction band is much wider (see Friction band).

## Arm Mk3.1 (Nov 21, 2026; current)

- **Arm Mk3.1 (printed PLA, bare, no screws):** 49.03 g, centre of mass 136 mm from the shaft (balance method). Gravity torque at horizontal: 49.03 g × 9.81 × 0.136 m = 65.4 mN·m.
- **Changes from Mk3:** fillet at the motor mount removed, load holes counterbored, infill increased because Mk3 was too flexible. The infill raised the mass by 17.7 g.
- **Hub screws:** 4 × M4×16 + 4 × M4 flat washers, symmetric about the shaft, so no gravity torque. The goBILDA 1309 hub (14.22 g) is on the axis.
- **Load holes:** every 50 mm from 150 to 300 mm. Nothing is fixed on the arm; the load goes on at the chosen hole.
- **Test load:** 43.44 g at 300 mm = 127.8 mN·m at horizontal.
- **Arm + load at horizontal:** 193.2 mN·m, about 44% of the highest motor torque measured (435 mN·m).
- **Resolution at 300 mm:** one 10.20 g washer = 30.0 mN·m ≈ 1.1% duty (calibration slope; the measured lift shift agrees, see Friction band).

## Arm Mk3 (Nov 17, 2026; retired)

- 31.34 g bare, centre of mass 138 mm (42.4 mN·m at horizontal). Too flexible; replaced by Mk3.1.

## Arm Mk2 (Nov 14, 2026; retired)

| Component | Mass (g) | Distance from shaft (mm) |
|---|---|---|
| Arm Mk2 (at its CoM) | 35.50 | 76 |
| Bolt + nut, mount 1 | 10.71 | 100 |
| Bolt + nut, mount 2 | 10.71 | 149.5 |
| Dowel pin (mass assumed) | 2 | 120 |
| goBILDA 1309 hub | 14.22 | 0 (on the axis, adds no gravity torque) |
| **Arm + fixed hardware (hub excluded)** | **58.92** | **95.22 (combined CoM)** |

- **Arm weight at the 118 mm scale point:** 47.6 g (computed with mount 2 at 150 mm; 47.5 g with 149.5 mm, a negligible difference).

## Gearbox backlash (Nov 14, 2026)

- **Method:** arm held at the motor, tip rocked by hand, vertical free play measured at 125 mm.
- **Result:** about 8.5 mm of play at 125 mm. arctan(8.5 / 125) ≈ 3.9°, so about 4°.
- **Effect:** the encoder sits on the motor side, so it reads the motor's position within this slop, not the arm's.

## Zero pin, servo (Mk3 Nov 18, Mk3.1 Nov 21, 2026)

- **Pin angle:** +155.9° from level, past vertical, outside the −90° to +90° sweep. 5 hand trials on Mk3 with `callibrateZero.py`: 154.92, 156.66, 154.35, 156.08, 157.24° (spread 2.9°).
- **Repeatability on Mk3 (motor-driven, +30%):** encoder count at the pin 546, 548, 547, 546 over 4 runs: 2 ticks (0.58°) spread. The hand trials' larger spread came from hand placement, not the pin.
- **Check on Mk3.1 (+20%):** 4 zeros; the level agreed with `getAngle()` each time. The arm parks at −1 to −2° (hold band). Counts at the pin aren't comparable between these runs (the count restarts each run, and the arm was moved between them).
- **Backlash:** driving positive into the pin loads the gears on the same side as holding against gravity across the sweep.

## Zero pin, Mk2 (3/8 in bolt, Nov 14, 2026; retired)

| Placement | Trials (°) | Mean |
|---|---|---|
| Gentle | 11, 10.5, 10.5 | 10.7° |
| Hard ("slam") | 14, 14.5, 14.5, 14.5 | 14.4° |

- **Why gentle and hard differ by about 3.7°:** backlash. A hard push drives the gears to the far side of their slop; a gentle placement leaves them anywhere inside it.
- **Retired because:** washers on the 150 mm bolt reached the pin when loaded.

## Auto-zero: `autoZero()` in `pico/autoZero.py` (updated Nov 18, 2026)

1. Extends the servo pin, waits 1.5 s.
2. Drives at +20% into the pin until the encoder reading stops changing for 0.3 s (10 s timeout).
3. At the pin, sets `encoder.zero_offset_ticks` with `ticksToDeg.zeroOffsetTicks()` so that `getAngle()` reads +155.9° there. Level is then 0°.
4. Drives to 0° with `goToAngle(0, 2, …)`, retracts the pin, returns True.
5. On timeout: prints a failure, retracts the pin, returns False, doesn't move.

- **Result:** parks at −1 to −2° (inside the ±2° hold band, approaching from above). Level check agrees.
- **Failure path tested:** with the pin not extended, the arm spun until the 10 s timeout and returned False.
- **Known gap:** any stall counts as "pin reached". An obstruction elsewhere would set a wrong zero. No guard yet.
- **History:** Nov 14, no offset set (drove to pin + 17°). Nov 16, offset set at a bolt pin (−14.4°), 4 s timeout. Nov 18, servo pin at +155.9°; the 4 s timeout ended zeroing mid-travel and was raised to 10 s.

## Torque calibration: motor duty against scale force (Nov 14, 2026, Mk2)

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
- **Above 18%:** the curve flattens. The supply is likely not the cause: on Nov 21 it peaked at 0.25 A with the CC light off up to 21.25% duty (brief lifts, not a sustained stall). Cause unknown.
- **Direction:** positive command only, the same direction as holding against gravity. Duty stepped up only; no down-step run yet.
- **Applies to any arm:** the calibration measures the motor, not the arm.
- **Limit:** it describes torque in a stall, not the start of motion. Lifting the arm from rest needs about 10% more duty than this fit predicts (see Friction band).

## Gravity model check, Mk2 (Nov 16, 2026)

- **Predicted torque at horizontal** (`analysis/predictTorque.py`): 55.0 mN·m unloaded, 99.9 mN·m loaded.
- **Measured arm torque:** at 4% duty the motor adds about nothing, and the scale read 47.0 g at 118 mm = 54.4 mN·m. That's 1% below the prediction. Assumes the arm was level on the scale and the dowel pin weighs 2 g.
- `analysis/constants.py` still holds the Mk2 values. Next: update it to Mk3.1 (49.03 g at 136 mm) and the 43.44 g load at 300 mm, then lock the prediction.

## Friction band at horizontal, Mk3.1 (Nov 21, 2026)

Open loop at horizontal after autoZero. Lift = smallest duty that raises the arm 2°; drop = largest duty at which it falls 2°. 0.25% steps, 5 trials each. Loaded searches started from a duty that holds the arm.

| Load | Lift (%) | Drop (%) | Band | Midpoint |
|---|---|---|---|---|
| Unloaded | 15.75, 16.5, 16.25, 16.5, 17.0 (mean 16.4) | −2.75, −1.25, −1.25, −1.25, −1.25 (mean −1.55) | 18.0 | 7.4 |
| 43.44 g at 300 mm | 21.25, 21.25, 21.0, 21.0, 21.0 (mean 21.1) | 1.5, 1.75, 1.5, 1.75, 1.25 (mean 1.55) | 19.6 | 11.3 |

- **Friction dominates:** the band (about 18–20% duty) is about 8× the arm's own gravity duty.
- **Before 2° of real motion:** the encoder shows a small nudge (motor-side slack), then roughly 5% more duty is needed to break static friction.
- **Lift shift with load:** 4.7% (predicted 4.6% from the calibration slope). The drop side moved 3.1%, so the band widens about 1.6% with load.
- **Midpoint unloaded:** 7.4%, against 6.6% predicted.
- **Lift threshold spread:** 1.25% unloaded (drifting upward over the trials), 0.25% loaded. One washer at 300 mm shifts it about 1.1%.
- **Supply:** peak 0.25 A, CC never on, up to 21.25% duty.
- **Load chosen:** 43.44 g at 300 mm.

## Not yet measured

- **Mk3.1 print settings** (infill %, wall count), so a reprint matches.
- **Bolt + nut alone at 300 mm** (for the washer-count demo, which has to subtract it).
- **Lift threshold against washer count** (0, 1, 2, 3 … washers) for the demo, with a few warm-up lifts first.
- **Plate level reference reading.**
- **Calibration down-step run** (hysteresis).