# Capacitor Symbol Properties

The naming scheme for all capacitors is as follows:
```
C_{Value}_{Voltage_in_V}_{Tolerance_in_pct}_{Dielectric}_{Package_in_inch}
```
For a capacitor with the following parameters
- Value: 100nF
- Voltage: 10V
- Tolerance: 10%
- Dielectric: X7R
- Package: 0603

This would result in
```
C_100n_10V_10pct_X7R_0603
```

## Capacitor footprint and package rules

- Each capacitor symbol uses the default R symbol provided in the `KL_C` library
- Each symbol must have a footprint assigned.
- The footprint must match the package size defined in the `Package_in_inch` field.
- Preferred SMD size: 0603. Exceptions allowed if the required value is not available in 0603.
- Capacitor values are without the SI Unit. All values have a postfix describing the nano, micro, ... range
- The nano, micro, ... postfixes are written in lowercase letters.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `C` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **Voltage_in_V**: The voltage the capacitor can handle in Volts.
- **Tolerance_in_pct**: Capacitor value tolerance in %.
- **Dielectric**: Dielectric parameter.
- **Package_in_inch**: The package size in inch.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **Farnell**: Order number of this component at Farnell.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## Capacitor, full example
| Name              | Value                                                                                 | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                  |-                                                                                      |-      |-          |-          |-          |-          |-      |
| Reference         | C                                                                                     | 1     | 0         | Left      | Center    | 0         | 0     |
| Value             | 100n                                                                                  | 1     | 0         | Left      | Center    | 0         | 0     |
| Footprint         | KL_Footprints:C_0603                                                                  | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet         | https://weblib.samsungsem.com/mlcc/mlcc-ec-data-sheet.do?partNumber=CL10B104KB8NNN    | 0     | 0         | Center    | Center    | 0         | 0     |
| Description       | Unpolarized capacitor                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| Voltage_in_V      | 10                                                                                    | 0     | 0         | Center    | Center    | 0         | 0     |
| Tolerance_in_pct  | 10                                                                                    | 0     | 0         | Center    | Center    | 0         | 0     |
| Dielectric        | X7R                                                                                   | 0     | 0         | Center    | Center    | 0         | 0     |
| Package_in_inch   | 0603                                                                                  | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser            | 187-CL10B104KB8NNNC                                                                   | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey           | 1276-1000-1-ND                                                                        | 0     | 0         | Center    | Center    | 0         | 0     |
| Farnell           | 4539043                                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC              | C1591                                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
