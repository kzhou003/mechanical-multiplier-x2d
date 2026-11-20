# Multiplier architecture

## V1: hand-driven repeated-addition machine

The first integrated multiplier is intentionally conservative:

1. Set multiplicand A on a mechanical input register.
2. Set multiplier B on a repeat-count wheel.
3. Clear the result accumulator.
4. Turn the crank through one complete cycle.
5. The mechanism adds A to the accumulator and advances the repeat counter by one.
6. When the counter reaches B, a mechanical stop or disengagement prevents another addition.

The arithmetic path is entirely mechanical. The operator supplies energy by turning the crank.

## Candidate modules

### Input register

Digit wheels with ten detented positions. A setting knob or thumbwheel changes each digit. The input register must not change while a calculation is running.

### Accumulator

A bank of decimal digit wheels. Each addition cycle advances the wheels according to the multiplicand. Carry transfers between adjacent wheels.

### Repeat counter

A digit wheel or countdown register tracks the number of remaining additions. The stop mechanism must be positive and must not depend on the operator counting crank turns.

### Crank and cycle cam

A single crank revolution defines one operation. A cam sequence should separate drive, carry, reset, and home phases. Add a visible home indicator.

## V2: stepped-drum investigation

Study a Leibniz-style stepped drum with selectable tooth engagement. The number of teeth engaged represents a digit. A sliding carriage shifts the engagement by decimal place. This can implement multiplication through partial products.

Before choosing this architecture, compare:
- number of moving parts;
- torque required at the crank;
- sensitivity to alignment;
- carry reliability;
- ease of printing and assembly;
- ease of clearing and reversing.

## Mechanical interfaces

Each module should specify:
- shaft diameter and bearing/bushing interface;
- mounting datum and hole pattern;
- permitted rotation and travel;
- home position;
- input and output state;
- maximum expected hand force;
- adjustment points;
- service access.

No dimensions are frozen yet. The first CAD iteration should use measured X2D calibration coupons and common fasteners selected in the BOM.
