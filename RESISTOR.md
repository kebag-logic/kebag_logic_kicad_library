# Resistor Symbol Properties

The naming scheme for all resistors is as follows:
```
R_{Value}_{Power_in_W}_{Tolerance_in_pct}_{Package_in_inch}
```
For a resistor with the following parameters
- Value: 10 kilo Ohms
- Power: 100mW
- Tolerance: 1%
- Package: 0603

This would result in
```
R_10K_0W1_1pct_0603
```

## Resistor footprint and package rules

- Each resistor symbol uses the default R symbol provided in the `KL_R` library
- Each symbol must have a footprint assigned.
- The footprint must match the package size defined in the `Package_in_inch` field.
- Preferred SMD size: 0603. Exceptions allowed if the required value is not available in 0603.
- Resistor values are without the SI Unit. Values <= 0 are entered with an R as postfix. E.g. `0R`.
- The kilo, mega, ... postfixes are written in capital letters.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `R` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **Power_in_W**: The power the resistor can handle in Watts.
- **Tolerance_in_pct**: Resistor value tolerance in %.
- **Package_in_inch**: The package size in inch.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **Farnell**: Order number of this component at Farnell.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## Resistor, full example
| Name              | Value                                                                             | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                  |-                                                                                  |-      |-          |-          |-          |-          |-      |
| Reference         | R                                                                                 | 1     | 0         | Center    | Center    | 0         | 0     |
| Value             | 10K                                                                               | 1     | 0         | Center    | Center    | 0         | 0     |
| Footprint         | KL_Footprints:R_0603                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet         | https://www.yageogroup.com/content/datasheet/asset/file/PYU-RC_GROUP_51_ROHS_L    | 0     | 0         | Center    | Center    | 0         | 0     |
| Description       | Resistor                                                                          | 0     | 0         | Center    | Center    | 0         | 0     |
| Power_in_W        | 0.1                                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| Tolerance_in_pct  | 1                                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| Package_in_inch   | 0603                                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser            | 603-RC0603FR-0710KL                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey           | 311-10.0KHRCT-ND                                                                  | 0     | 0         | Center    | Center    | 0         | 0     |
| Farnell           | 2421850                                                                           | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC              | C98220                                                                            | 0     | 0         | Center    | Center    | 0         | 0     |