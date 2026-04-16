# Ferrite Bead Symbol Properties

The naming scheme for all ferrite beads is as follows:
```
FB_{Value}_{Max_current_in_A}
```
For a ferrite bead with the following parameters
- Value: 33 Ohms
- Max. Current: 3A

This would result in
```
FB_33R_3A
```

## Ferrite Bead footprint and package rules

- Each ferrite bead must be derived from the `FB_{Value}_{Max_current_in_A}` template.
- Preferred SMD size (in inch): 0603. Exceptions allowed if the required value is not available in 0603.
- Ferrite bead values are written without the SI Unit. Values <= 1K are entered with an R as postfix. E.g. `0R`.
- The kilo, mega, ... postfixes are written in capital letters.
- Links to datasheets must link directly to the manufacturer. Supplier datasheets are to be avoided where possible.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `FB` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **Value**: The impedance of the component at 100MHz.
- **Max_current_in_A**: Max. current rating of this component.
- **MPN**: Manufacturer Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## Ferrite Bead, full example
| Name              | Value                                                                             | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                  |-                                                                                  |-      |-          |-          |-          |-          |-      |
| Reference         | FB                                                                                | 1     | 0         | Center    | Center    | 0         | 0     |
| Value             | 33R                                                                               | 1     | 0         | Center    | Center    | 0         | 0     |
| Footprint         | KL_Footprints:BLM18P                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet         | https://pim.murata.com/asset/pim4/ferriteBeadInductortypefilter/ENFA0003_PDF_FERRITEBEADINDUCTORTYPEFILTER?lastModifiedDatetime=20250707190934    | 0     | 0         | Center    | Center    | 0         | 0     |
| Description       | Ferrite Bead                                                                      | 0     | 0         | Center    | Center    | 0         | 0     |
| Max_current_in_A  | 3                                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| MPN               | BLM18PG330SN1D                                                                    | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser            | 81-BLM18PG330SN1D                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey           | 490-5220-1-ND                                                                  | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC              | C88984                                                                            | 0     | 0         | Center    | Center    | 0         | 0     |

## Validation

Run the validation script `run_check_symbol.py` in the helper folder.