# Mechanical Multiplier X2D

**A fully mechanical, 3D-printable decimal/binary computing machine — designed for iteration on the Bambu Lab X2D.**

> Status: **early design / research project**. This repository currently contains the architecture, engineering notes, and a software reference model. It does **not** yet contain a validated printable multiplier. CAD parts will be added only after their geometry and fit have been tested.

The goal is to build a machine that performs arithmetic through physical motion: gears, cams, levers, detents, ratchets, shafts, and mechanical carry. No microcontroller, electronic logic, motor, or software participates in the arithmetic of the finished machine. Software in this repository is used only to verify expected arithmetic and support design.

## Project goals

1. Build and validate a repeatable mechanical carry mechanism.
2. Build a multi-digit mechanical accumulator.
3. Add a mechanical multiplication mechanism based on repeated addition and/or a stepped-drum architecture.
4. Make the design modular, documented, repairable, and printable on a Bambu Lab X2D.
5. Publish source CAD, neutral STEP exports, and print-ready STL files alongside test evidence.

## Architecture

The project is developed in stages. The first prototype is deliberately an **odometer-style decimal accumulator**, because decimal wheels, carry pawls, and detents are mechanically intuitive and provide a direct route to a practical multiplier. Binary mechanisms and 3:2 compressor concepts remain useful study references, but are not mixed into the first physical architecture.

### Planned data path

```text
User input / setting
        |
        v
Input register (multiplicand)
        |
        v
Mechanical selection / repeat-count mechanism (multiplier)
        |
        v
Accumulator <---- carry pawls + decimal digit wheels
        |
        v
Result register / readout
```

### Multiplication principle

The initial implementation will use shift-and-add or repeated addition:

`A × B = A added to the accumulator B times`

A later revision may replace repeated addition with a Leibniz-style stepped drum / selectable gear engagement. The design choice will be made from measured part count, operating force, reliability, and carry behavior—not appearance alone.

## Roadmap

| Milestone | Deliverable | Exit criterion |
|---|---|---|
| M0 | Requirements, arithmetic model, print/material guide | Repository and interfaces documented |
| M1 | Single decimal digit wheel + detent | 0–9 indexing is repeatable |
| M2 | Two-digit accumulator + carry | 09 + 1 produces 10 reliably |
| M3 | Multi-digit accumulator | Carry propagates across all digits |
| M4 | Mechanical repeat-count controller | Exactly B additions are performed |
| M5 | Integrated multiplier | Test matrix passes without electronic assistance |
| M6 | X2D release package | CAD, STEP, STL, BOM, assembly guide, test evidence |

## Repository layout

- `docs/` — design rationale, architecture, tolerances, print and assembly notes.
- `designs/` — module-level design specifications and interfaces.
- `cad/` — parametric CAD source, STEP exports, and STL files (added as designs mature).
- `simulations/` — arithmetic reference model; not part of the physical compute path.
- `tests/` — deterministic arithmetic tests for the reference model.
- `BOM.md` — prototype bill of materials and hardware assumptions.

## X2D manufacturing approach

The X2D is the target printer, but the printer's name alone does not determine tolerances. Each module will include a calibration coupon and a fit record. Start with PLA for rigid prototypes; use PETG where impact resistance or toughness is more important. Avoid relying on printed-in-place flexures for high-cycle carry parts until fatigue tests justify them.

Initial engineering rules (to be validated on the actual machine and filament):

- Use separate shafts/pins for frequently rotating joints where possible.
- Design replaceable bushings rather than making a printed shaft rub directly in a printed hole.
- Provide access to adjust detent preload and pawl engagement.
- Keep gear backlash intentional and measurable.
- Print gears flat when that gives strong tooth roots; evaluate layer orientation against actual tooth loading.
- Do not assume a nominal CAD clearance will print accurately. Print a clearance coupon first.

See [X2D print guide](docs/06-x2d-printing-guide.md) and [tolerances](docs/07-tolerances-and-materials.md).

## Current status

| Subsystem | Status |
|---|---|
| Project architecture | Documented |
| Arithmetic reference model | Implemented |
| Single-digit wheel CAD | Not yet designed |
| Carry mechanism CAD | Not yet designed |
| Accumulator CAD | Not yet designed |
| Multiplier CAD | Not yet designed |
| X2D print validation | Not yet started |

## Safety and expectations

This is an educational mechanical-computing project, not a certified product. Keep fingers clear of pinch points, use eye protection when removing supports or cutting shafts, and test mechanisms at low speed by hand. Do not motorize an unvalidated assembly.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Please include printer, filament, nozzle, layer height, orientation, measured clearances, and a short test result when submitting a print report.

## License

- Documentation and software: MIT License (see [LICENSE](LICENSE)).
- Hardware design files, once added: CERN Open Hardware Licence Version 2 - Strongly Reciprocal (CERN-OHL-S-2.0). See [HARDWARE-LICENSE](HARDWARE-LICENSE).
