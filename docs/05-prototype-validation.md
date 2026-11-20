# Prototype validation and test plan

This document defines the physical evidence required before a mechanism is promoted from designed to tested.

## M1 — single-digit wheel

**Purpose:** prove ten-position indexing before adding carry.

### Required behavior
- The wheel has ten equally spaced states, 36 degrees apart.
- One crank/index action advances exactly one state.
- The detent holds the wheel when the input is released.
- The wheel can complete repeated full revolutions without binding.

### Test
1. Mark the ten positions 0–9.
2. Advance one step at a time through 0 → 9 → 0.
3. Repeat for 100 complete indexing steps.
4. Record missed steps, double steps, drift, wear, and approximate operating force.

**Pass condition:** 100 consecutive commanded single steps produce the correct final state with no missed or double index. Any adjustment between steps restarts the count.

## M2 — two-digit carry

**Purpose:** prove the carry event and its timing.

### Required cases
- 07 + 1 → 08
- 08 + 1 → 09
- 09 + 1 → 10
- 19 + 1 → 20
- 99 + 1 → 100 (requires at least three wheels for the full test)

### Test
Start each case from a clearly marked state. Perform exactly one complete crank cycle and inspect every digit wheel. Repeat boundary cases at least 20 times.

**Pass condition:** every boundary crossing causes exactly one carry to the next digit, with no carry on non-boundary steps.

## M3 — accumulator

Test a matrix including no-carry, one-carry, and cascading-carry cases. Include:
- 123 + 456 = 579
- 099 + 001 = 100
- 999 + 001 = 1000
- 500 + 500 = 1000

The initial mechanical incrementer may only support +1. Do not claim general addition until the input mechanism can supply arbitrary addends and the full test matrix passes.

## M4/M5 — multiplier

Test:
- 0 × 0 = 0
- 0 × 9 = 0
- 9 × 0 = 0
- 1 × 9 = 9
- 7 × 8 = 56
- 12 × 13 = 156
- 99 × 99 = 9801

For each test, record input settings, number of crank cycles, result, and any intervention. The operator must not count cycles manually for a release claiming an automatic repeat counter.

## Evidence template

- Hardware revision:
- CAD revision:
- Printer / nozzle:
- Filament and slicer profile:
- Print orientation:
- Assembly notes:
- Test case:
- Expected result:
- Observed result:
- Cycle count:
- Failure / wear observations:
- Photos or video:
- Pass / fail:
