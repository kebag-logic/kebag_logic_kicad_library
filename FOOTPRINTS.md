# Footprint Guideline

## Layer Names
- Silkscreen: F.Silkscreen (top), B.Silkscreen (bottom)
- Fabrication: F.Fab (top), B.Fab (bottom)
- Courtyard: F.Courtyard (top), B.Courtyard (bottom)

Use the top layer consistently. All markings, outlines, and courtyards must be placed on the corresponding layer to avoid ambiguity.

## Footprint Orientation
- All footprints should have the component facing upwards (pin 1 top-left when possible) for consistency in assembly drawings.
- The footprint should be centered around the origin (0,0).

## Fontsizes
| Layer         | Font       | Width | Height | Thickness | Position  |
|---------------|-----------|-------|--------|-----------|-----------|
| F.Silkscreen  | KiCad Font | 1mm   | 1mm    | 0.15mm    | centered  |
| F.Fab         | KiCad Font | 1mm   | 1mm    | 0.15mm    | centered  |

## Outlines

### F.Silkscreen
- Component outlines must be drawn on F.Silkscreen where applicable.
- Outlines must not overlap any pads.
- Minimum distance to copper: 0.1 mm
- Line width: 0.12 mm
- Line style: solid

### F.Fab
- The complete component outline must be drawn on F.Fab.
- This outline is allowed to overlap pads as it is not printed on the PCB.
- Line width: 0.1 mm
- Line style: solid

## Pin 1 Marking
- All polarized or directional components must have pin 1 clearly marked.
- Use a small triangle for the marking, which can be copied from existing footprints.
- Through-hole components must have a rectangular pad to indicate pin 1, e.g., pin headers.
- Ensure the marking is visible on the silkscreen and does not overlap pads or other critical areas.

## Pad Design

### SMD Pads
- SMD pads must be rounded rectangles.
- Corner size: 25%
- F.Paste and F.Mask layers must be included as part of the pad.

### Through Hole Pads
- Through-hole pads must have a rectangular pad to indicate pin 1.
- All other through-hole pads must be circular.

## Pad Numbering
- Ensure pad numbers follow the schematic symbol and datasheet convention.
- Verify that pin 1 is correctly aligned with the schematic symbol and pad numbering.

## Courtyard
- A courtyard must surround all components with a minimum clearance of 0.1 mm from the outermost pad or copper area.
- Line width: 0.05 mm
- Line style: solid

## Visible Parameters
- The component reference must always be present on F.Silkscreen and F.Fab.
- Silkscreen and fabrication layers must align consistently for all components.

## Invisible Parameters
- All other metadata (e.g., values, tolerances, internal references) must not appear on the footprint.

## 3D Models
- Each footprint must be assigned a corresponding 3D model.
- Place all 3D models in the `3dmodels/` folder.
- Subfolders containing STEP files must end with `.3dshapes`.
- If a 3D model is missing, it can be sourced from [SnapEDA](https://www.snapeda.com/). Ensure the license allows usage.