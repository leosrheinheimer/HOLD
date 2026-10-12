# Measurements

## Encoder ticks per output-shaft turn (Oct 10, 2026)

- **Result:** 1245.5 ticks per output-shaft turn.
- **What counts as a tick:** every rising and falling edge of channel A, with direction taken from channel B. This is what `pico/readEncoder.py` and `pico/onTick.py` count.
- **Method:** a locking plier clamped on the output shaft as a handle and pointer. 10 full turns per trial, stopping on a fixed mark.
- **Trials:** 12453 and 12457 ticks over 10 turns. They differ by 4 counts (0.03%).
- **Resolution:** 360 / 1245.5 = 0.289° per tick.
- **Cross-check:** the interrupt counter read 2489 over 2 turns (expected 2491) and 6227 over 5 fast turns (expected 6227.5).
- **Against the listing:** the seller's specs imply 748 (11 pulses × 2 edges × 34:1 gearbox). The measured value is 66% higher. How it splits between encoder pulses and gear ratio is unknown. The rig only uses the product.