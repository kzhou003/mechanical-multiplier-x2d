# Project overview

## Why build a mechanical multiplier?

A mechanical calculator makes arithmetic visible. A carry is no longer an abstract Boolean signal: it is a pawl, tooth, cam, or latch that moves a neighboring digit wheel by one position. The project uses this visibility to explore computation, mechanism design, tolerances, and additive manufacturing.

## Design constraints

- The finished arithmetic path must be mechanical.
- The operator may set input wheels and turn a crank by hand.
- No powered actuator or electronic controller is required.
- Printed parts should be replaceable and inspectable.
- Each milestone must be testable independently.
- A design is not marked printable until an actual print and fit check have been recorded.

## Why decimal first?

A decimal wheel with ten stable positions and a carry after 9 → 0 is a clear, demonstrable mechanical primitive. It also maps naturally to traditional mechanical calculators and odometers. Binary mechanical logic remains a possible parallel research branch, but combining binary gates and decimal stepped drums in the first prototype would add complexity without improving the first useful result.

## Reference projects and inspiration

These projects are study references, not dependencies and not proof that their parts fit this design:

- [Babbage Cubes](https://github.com/High-Desert-Institute/Babbage-Cubes) — modular 3D-printed mechanical logic and clocked motion.
- [mechanical-computation](https://github.com/nvoorhies/mechanical-computation) — compliant-mechanism logic gates.
- [3D printed Difference Engine](https://github.com/MechRedPanda/difference_engine_3d_print) — digit wheels and mechanical carry ideas.
- [Leibniz Stepped Reckoner reconstruction](https://github.com/wixette/leibniz-stepped-reckoner) — stepped drum and carriage concepts.
- [STREAM fluidic circuits](https://lehong-wang.github.io/_projects/fluidic_circuits.html) — an alternative physical-computing approach; fluidic rather than rigid mechanical.

Check each upstream project's license before reusing geometry, code, or documentation. This project will independently document any adapted component and its provenance.

## Design philosophy

Prefer simple kinematics over clever but fragile mechanisms. Favor adjustable stops, accessible fasteners, replaceable wear surfaces, and visible state. Optimize for repeatable operation before minimizing size or part count.
