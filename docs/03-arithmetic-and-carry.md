# Arithmetic and carry model

## Decimal accumulator

Let the accumulator contain digits d0 (units), d1 (tens), ..., dn-1. To add a non-negative integer x, process one decimal digit at a time:

`t_i = d_i + x_i + c_i`

`d'_i = t_i mod 10`

`c_{i+1} = floor(t_i / 10)`

where x_i is the i-th decimal digit and c0 = 0. Continue until all input digits and carry are consumed.

For the physical first prototype, the simplest operation is increment-by-one. This isolates the wheel indexing and carry mechanism before adding a more complex multi-tooth input drive.

## Example: 099 + 1

- Units: 9 + 1 = 10 → write 0, carry 1.
- Tens: 9 + 1 = 10 → write 0, carry 1.
- Hundreds: 0 + 1 = 1.
- Result: 100.

The physical mechanism must produce exactly two carry transfers in the same complete operating cycle.

## Multi-digit addition

A later input mechanism can advance a wheel by more than one position. If the mechanism adds x_i to a digit, it must produce the correct quotient carry, not merely a single carry pulse. One approach is repeated single-step actuation; another is a shaped cam or multi-tooth sector. The repeated-step approach is easier to prototype and verify.

## Multiplication

The initial multiplier uses repeated addition:

`A × B = Σ(k=1..B) A`

The multiplicand is set on an input register. A repeat-count mechanism causes exactly B addition cycles. The accumulator stores the running result.

Important edge cases:

- A × 0 must produce 0 without an addition cycle.
- A × 1 must produce A.
- 0 × B must remain 0.
- Carry must propagate across all result digits.
- The counter must stop after exactly B cycles.
- The machine must have a defined reset / clear procedure.

## Alternative: stepped drum

A Leibniz-style stepped drum can select a number of teeth proportional to a digit setting. A carriage shift changes the decimal place, allowing partial products to be accumulated. This may be faster than repeated addition but requires more precise geometry and sequencing. It is a later design candidate, not an assumed feature of the first prototype.
