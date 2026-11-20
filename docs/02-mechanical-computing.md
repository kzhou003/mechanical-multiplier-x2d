# Mechanical computing primitives

## Physical state

A mechanical digit is represented by the angular position of a wheel. For a decimal wheel, ten stable states are spaced by 36 degrees:

`360° / 10 = 36°`

A detent or indexing mechanism holds the wheel at one of these positions. The printed wheel should not be expected to stop accurately from friction alone.

## Motion and logic

A mechanism transforms an input displacement or rotation into another displacement or rotation. Useful primitives include:

- **Lever:** changes direction, travel, or force according to its arm lengths.
- **Cam:** converts rotation into a prescribed follower motion.
- **Ratchet and pawl:** permits indexed motion while resisting reverse motion.
- **Detent:** creates discrete stable positions.
- **Gear pair:** couples angular motion with a defined ratio and direction.
- **Carry pawl:** transfers one indexed step to the next digit when a lower digit rolls over.

These are mechanical functions, not electronic gates. A lever-and-cam assembly should be described by its geometry, motion sequence, and force path rather than by merely labeling it AND or XOR.

## Carry as a state transition

For a decimal digit d in {0,...,9}, adding one gives:

- if d < 9: advance the wheel by one detent;
- if d = 9: advance the wheel to 0 and trigger exactly one carry to the next wheel.

For an increment k, the carry count is determined by the number of digit-boundary crossings. A practical mechanism must ensure the carry is neither missed nor repeated during one crank cycle.

## Mechanical timing

A multi-digit accumulator needs a controlled sequence:

1. The drive engages the units wheel.
2. The units wheel advances.
3. If it crosses 9 → 0, the carry pawl is armed and transfers one step to the tens wheel.
4. The carry element disengages or resets.
5. The drive returns to a known home position.

The exact phase relationship must be designed into cams, stops, and pawls. A carry that occurs too early can collide with the driving pawl; one that occurs too late can be lost before the next cycle.

## Backlash and lost motion

Gear backlash is the angular free play between meshing teeth. Some backlash is necessary to avoid binding, but excessive backlash causes uncertain indexing. Measure it in the assembled mechanism and test both directions. Where possible, make the output state depend on a detent rather than on gear tooth contact alone.
