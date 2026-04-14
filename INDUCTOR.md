# Inductor Symbol Properties
The naming scheme for all inductances is as follows:
```
L_{Value}_{I_max_in_A}_{Tolerance_in_pct}_{Package_LxW_in_mm}
```
For an inductor with the following parameters:
- Value: 3.3uH
- Max current: 8A
- Tolerance: 20%
- Package: 7.2mmx7.9mm

This would result in
```
L_3u3_8A_20pct_7.2x7.9
```

## Inductance footprint and package rules

- Each inductance symbol uses the default L symbol provided in the `KL_L` library
- Each symbol must have a footprint assigned.
- The footprint must match the package size defined in the `Package_LxW_in_mm` field.
- Preferred SMD size: 0603. Exceptions allowed if the required value is not available in 0603.
- Inductance values are without the SI Unit. All values have a postfix describing the nano, micro, ... range
- The nano, micro, ... postfixes are written in lowercase letters.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `L` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **I_max_in_A**: The current the inductor can handle before going into saturation.
- **Tolerance_in_pct**: Inductor value tolerance in %.
- **Package_LxW_in_mm**: The package size in mm.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## Inductor, complete example
| Name              | Value                                                                                                                                                                         | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                  |-                                                                                                                                                                              |-      |-          |-          |-          |-          |-      |
Reference           | L                                                                                                                                                                             | 1     | 0         | Center    | Center    | 0         | 0     |
Value               | 3u3                                                                                                                                                                           | 1     | 0         | Center    | Center    | 0         | 0     |
Footprint           | KL_Footprints:L_3u3_EXLA1V0603                                                                                                                                                | 0     | 0         | Center    | Center    | 0         | 0     |
Datasheet           | https://www.eaton.com/content/dam/eaton/products/electronic-components/resources/data-sheet/eaton-exla1v06-automotive-high-current-molded-inductor-data-sheet-elx1221-en.pdf  | 0     | 0         | Center    | Center    | 0         | 0     |
Description         | Inductor                                                                                                                                                                      | 0     | 0         | Center    | Center    | 0         | 0     |
I_max_in_A          | 8                                                                                                                                                                             | 0     | 0         | Center    | Center    | 0         | 0     |
Tolerance_in_pct    | 20                                                                                                                                                                            | 0     | 0         | Center    | Center    | 0         | 0     |
Package_LxW_in_mm   | 7.2x7.9                                                                                                                                                                       | 0     | 0         | Center    | Center    | 0         | 0     |
Digikey             | 704-EXLA1V0603-3R3-R                                                                                                                                                          | 0     | 0         | Center    | Center    | 0         | 0     |
Mouser              | 283-EXLA1V0603-3R3-RCT-ND                                                                                                                                                     | 0     | 0         | Center    | Center    | 0         | 0     |
LCSC                | C7189866                                                                                                                                                                      | 0     | 0         | Center    | Center    | 0         | 0     |
