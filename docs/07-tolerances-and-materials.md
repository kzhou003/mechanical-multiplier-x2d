# Tolerances, materials, and wear

## Do not copy nominal clearances blindly

FDM dimensions depend on filament, temperature, cooling, orientation, flow calibration, geometry, and slicer compensation. The values below are **experimental starting points only**, not guaranteed X2D settings.

| Interface | First coupon range to investigate | Acceptance test |
|---|---:|---|
| Free-running printed pin / hole | 0.20–0.40 mm diametral clearance | Rotates without binding; wobble acceptable |
| Sliding printed parts | 0.25–0.50 mm total clearance | Slides through full travel without stick-slip |
| Gear backlash | Set from module, tooth geometry, and coupon | Full revolution without tight spots |
| Detent engagement | Tune spring/pawl preload | Holds state, indexes without excessive force |

Clarify whether a CAD clearance is radial, diametral, or total gap. Never use the table without a calibration coupon.

## Wear strategy

- Use replaceable bushings at rotating joints.
- Avoid sustained high preload in PLA.
- Make pawls and detents replaceable.
- Use washers or spacers to prevent printed faces rubbing.
- Inspect tooth tips, pawl edges, and shaft holes after cycling.

## Flexures

Printed flexures are attractive because they eliminate separate hinges, but fatigue life depends on material, strain, layer orientation, geometry, and environment. Do not use a flexure as a critical carry spring until a dedicated coupon has passed repeated-cycle testing.

## Test record template

| Field | Value |
|---|---|
| Part / revision | |
| Filament / profile | |
| Nozzle / layer height | |
| Orientation | |
| CAD clearance definition | |
| Measured dimensions | |
| Cycle count | |
| Result / failure mode | |
