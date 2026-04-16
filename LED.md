# LED Symbol Properties

The naming scheme for all LEDs is as follows:
```
LED_{color}_{U_F_in_V}_{I_F_in_A}_{Package_in_inch}
```
For a LED with the following parameters
- color: Red
- U_F: 2V
- I_F: 0.03A
- Package: 0603

This would result in
```
LED_red_2V_0.03A_0603
```

## LED footprint and package rules

- Each LED must be derived from the `LED_{color}_{U_F_in_V}_{I_F_in_A}_{Package_in_inch}` template.
- The footprint must match the package size defined in the `Package_in_inch` field.
- Preferred SMD size (in inch): 0603. Exceptions allowed if the required value is not available in 0603.
- Links to datasheets must link directly to the manufacturer. Supplier datasheets are to be avoided where possible.
- Only the Label field is visible by default.
- The reference designator prefix must remain `D` and must not be fixed in the symbol.
- The LABEL field is used to create the actual reference designator. Please do not overwrite it.

# Cathode identification
- Pin 1 is always the cathode
- Pin 2 is always the anode
- Footprint: The cathode of the LED shall be enclosed by a rectangle on the silk screen.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **U_F_in_V**: Forward voltage in V.
- **I_F_in_A**: Max. forward current in A.
- **lambda_d_in_nm**: The wavelength of the diode in nm.
- **Package_in_inch**: The package in inch.
- **MPN**: Manufacturer Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## LED, full example
| Name              | Value                                                                             | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                  |-                                                                                  |-      |-          |-          |-          |-          |-      |
| Reference         | D                                                                                 | 1     | 0         | Center    | Center    | 0         | 0     |
| Value             | LED                                                                               | 1     | 0         | Center    | Center    | 0         | 0     |
| Footprint         | KL_Footprints:LED_0603                                                            | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet         | https://www.mouser.de/datasheet/3/281/1/LTST_C194KRKT.pdf                         | 0     | 0         | Center    | Center    | 0         | 0     |
| Description       | Light emitting diode                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| U_F_in_V          | 2                                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| I_F_in_A          | 0.03                                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| lambda_d_in_nm    | 639                                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| Color             | Red                                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| Package_in_inch   | 0603                                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| MPN               | LTST-C194KRKT                                                                     | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser            | 859-LTST-C194KRKT                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey           | 160-1835-1-ND                                                                     | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC              | C913101                                                                           | 0     | 0         | Center    | Center    | 0         | 0     |

## Validation

Run the validation script `run_check_symbol.py` in the helper folder.