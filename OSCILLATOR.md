# Oscillator Symbol Properties

The naming scheme for all active oscillators is as follows:
```
Oscillator_{Value}_{Frequency_Stability_in_ppm}_{Output}_{Package_LxW_in_mm}
```
For an oscillator with the following parameters
- Value: 25MHz
- Frequency Stability: 25ppm
- Output type: HCMOS
- Package LxW in mm: 2.5mm x 2.0mm

This would result in
```
Oscillator_25M_25ppm_HCMOS_2.5x2.0
```

## Oscillator footprint and package rules

- Each oscillator is derived from the `Oscillator_{Value}_{Frequency_Stability_in_ppm}_{Output}_{Package_LxW_in_mm}` template.
- Each symbol must have a footprint assigned.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `Y` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **Frequency_Stability_in_ppm**: Overall frequency stability in ppm.
- **Output**: Output logic type, e.g. `HCMOS`.
- **Voltage_in_V**: Supply voltage or supply voltage range in V.
- **MPN**: Manufacturer Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## Oscillator, full example
| Name                        | Value                                     | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                            |-                                          |-      |-          |-          |-          |-          |-      |
| Reference                   | Y                                         | 1     | 0         | Center    | Center    | 0         | 0     |
| Value                       | 25M                                       | 1     | 0         | Center    | Center    | 0         | 0     |
| Footprint                   | KL_Footprints:ECS-2520MV                  | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet                   | https://ecsxtal.com/store/pdf/ECS-2520MV.pdf | 0  | 0         | Center    | Center    | 0         | 0     |
| Description                 | Oscillator                                | 0     | 0         | Center    | Center    | 0         | 0     |
| Frequency_Stability_in_ppm  | 25                                        | 0     | 0         | Center    | Center    | 0         | 0     |
| Output                      | HCMOS                                     | 0     | 0         | Center    | Center    | 0         | 0     |
| Voltage_in_V                | 1.6-3.6                                   | 0     | 0         | Center    | Center    | 0         | 0     |
| MPN                         | ECS-2520MV-250-CN-TR                      | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser                      | TBD                                       | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey                     | TBD                                       | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC                        | C405464                                   | 0     | 0         | Center    | Center    | 0         | 0     |
