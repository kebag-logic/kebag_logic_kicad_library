# Power Connector Symbol Properties

The naming scheme for all power connectors is as follows:
```
Con_{SigType}_{Shape}_{KeyParameters}
```
For a DC barrel connector with 5.5mm outer and 2.5mm inner diamert, this would result in
```
Con_{SigType}_{Shape}_{Outer_Diam_in_mm}x{Inner_Diam_in_mm}
Con_DC_Barrel_5.5mmx2.5mm
```

## Power Connector footprint and package rules

- Each power connector symbol uses an appropriate symbol that shows all pins in a single alignment. Multiple GND are not to be overlayed each other.
- Each symbol must have a footprint assigned.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `J` and must not be fixed in the symbol.

## Polarity rules

- The positive terminal must always be placed at the top of the symbol.
- The negative terminal (GND) must always be placed at the bottom.
- For barrel connectors:
  - Inner pin = positive (unless explicitly specified otherwise)
  - Outer sleeve = GND
- Any deviation must be clearly documented in the Description field.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **SigType**: The signal type for which the connector is rated. Usually DC or AC.
- **Shape**: The shape of the connector.
- **Outer_Diam_in_mm**: The outer diameter of the connector in mm.
- **Inner_Diam_in_mm**: The inner diameter of the connector in mm.
- **I_max_in_A**: The max. rated current in A.
- **V_max_in_V**: The max. rated voltage in V.
- **MPN**: Manufacturer Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **Farnell**: Order number of this component at Farnell.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## Power Connector full example
| Name                          | Value                                                                             | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                              |-                                                                                  |-      |-          |-          |-          |-          |-      |
| Reference                     | J                                                                                 | 1     | 0         | Center    | Center    | 0         | 0     |
| Value                         |                                                                                   | 0     | 0         | Center    | Center    | 0         | 0     |
| Footprint                     | KL_Footprints:DC-Jack_Wuerth_694108301002                                         | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet                     | https://www.we-online.com/components/products/datasheet/694108301002.pdf          | 0     | 0         | Center    | Center    | 0         | 0     |
| Description                   | Power Connector                                                                   | 0     | 0         | Center    | Center    | 0         | 0     |
| Outer_Diameter_in_mm          | 5.5                                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| Inner_Diameter_in_mm          | 2.5                                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| I_max_in_A                    | 5                                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| V_max_in_V                    | 30                                                                                | 0     | 0         | Center    | Center    | 0         | 0     |
| MPN                           | 694108301002                                                                      | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser                        | 710-694108301002                                                                  | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey                       | 732-5934-ND                                                                       | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC                          |                                                                                   | 0     | 0         | Center    | Center    | 0         | 0     |