# Bambu Lab X2D printing guide

This guide is a starting process, not a claim of printer-specific calibration. Record actual slicer settings and measured results for every released part.

## Prototype materials

- **PLA:** first choice for rigid geometry prototypes, housings, digit wheels, and fit coupons. It is easy to print but can creep or deform under sustained load and heat.
- **PETG:** candidate for tougher pawls, brackets, and parts that may experience impact. It can string and may have different dimensional behavior from PLA.
- **TPU:** use only where a compliant or friction element is intentionally required. It is not a default material for precision gears or rigid indexing components.

## Print validation sequence

1. Confirm nozzle diameter and filament profile in the slicer.
2. Print a small dimensional coupon with holes, pins, and clearance steps.
3. Measure with calipers after cooling.
4. Test a shaft in each hole size; record free rotation and wobble.
5. Print a single gear pair and test mesh through a full revolution.
6. Print a detent sample and cycle it at least 100 times by hand.
7. Only then print a larger assembly.

## Orientation

- For gear wheels, evaluate tooth-root strength and flatness. Printing the wheel flat often gives a convenient gear plane, but the tooth load and layer orientation still need physical testing.
- For pawls and levers, orient the part so bending loads do not peel layers apart.
- Avoid thin vertical pins when a separate metal shaft or printed replaceable pin can be used.
- Add fillets at stress concentrations.

## Supports and assembly

Avoid support material on bearing bores, gear tooth flanks, and detent contact surfaces when possible. If support is unavoidable, design access for cleanup. Do not force-fit parts until the clearance coupon establishes a safe fit.

## Required print log

For each tested part, record:
- X2D configuration and nozzle;
- filament brand, type, and color;
- slicer profile and layer height;
- wall count, infill, and orientation;
- measured hole and pin dimensions;
- fit result;
- operating cycles and observed wear;
- photos or video of the test.

## Safety

Use eye protection for support removal and cutting. Keep hands clear of pinch points while testing. Test by hand at low speed; do not motorize an unvalidated mechanism.
