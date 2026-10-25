# Measurements

## Encoder ticks per output-shaft turn (Oct 10, 2026)

- **Result:** 1245.5 ticks per output-shaft turn.
- **What counts as a tick:** every rising and falling edge of channel A, with direction taken from channel B. This is what `pico/readEncoder.py` and `pico/onTick.py` count.
- **Method:** a locking plier clamped on the output shaft as a handle and pointer. 10 full turns per trial, stopping on a fixed mark.
- **Trials:** 12453 and 12457 ticks over 10 turns. They differ by 4 counts (0.03%).
- **Resolution:** 360 / 1245.5 = 0.289° per tick.
- **Cross-check:** the interrupt counter read 2489 over 2 turns (expected 2491) and 6227 over 5 fast turns (expected 6227.5).
- **Against the listing:** the seller's specs imply 748 (11 pulses × 2 edges × 34:1 gearbox). The measured value is 66% higher. How it splits between encoder pulses and gear ratio is unknown. The rig only uses the product.

## Pin Map (Oct 24, 2026)
- **Encoder** Yellow on GP2, Green on GP3, Blue on 3V3, Black on GND
- **INA219 (amp sensor)** SDA (purple) on GP0, SCL (gray) on GP1, VCC (red) and GND (black) to the rails
- **MD10C (motor controller)** PWM (orange) on GP14, DIR (brown) on GP15, GND (black) to the rail

## INA219 accuracy check (Oct 24, 2026)

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
- **Cause:** unresolved. The resistor colour bands were hard to read, and values were matched to the kit listing. The multimeter gave drifting readings that didn't flip sign symmetrically when the probes were reversed (likely a weak battery), so it couldn't serve as a reference.
- **Impact:** a constant scale error is absorbed by the torque calibration against the scale.
- **Next:** check against the bench supply's current display during the power-up.