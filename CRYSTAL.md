# Crystal Symbol Properties

The naming scheme for all crystal is as follows:
```
Crystal_{Value}_{Frequency_Tolerance_in_ppm}_{Load_Capacitance_in_pF}_{Package_LxW_in_mm}
```
For a crystal with the following parameters
- Value: 25MHz
- Frequency Tolerance: 10ppm
- Load Capacitance: 32pF
- Package LxW in mm: 3.2mm x 2.5mm

This would result in
```
Crystal_25M_10ppm_32pF_3.2x2.5
```

## Crystal footprint and package rules

- Each crystal symbol uses the default Crystal symbol provided in the `KL_Crystal` library
- Each symbol must have a footprint assigned.
- The footprint must match the package size defined in the `Package_LxW_in_mm` field.
- The Crystal value is stored as frequency using SI prefix without ‘Hz’ (e.g. 25M, 32.768k)
- The kilo, mega, ... postfixes are written in capital letters.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `X` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **Frequency_Tolerance_in_ppm**: Typical frequency tolerance measured at 25°C.
- **Load_Capacitance_in_pF**: Load of the crystal in pF.
- **Package_LxW_in_mm**: The package dimensions in mm.
- **MPN**: Manufacturer Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **Farnell**: Order number of this component at Farnell.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## Crystal, full example
| Name                          | Value                                                                             | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                              |-                                                                                  |-      |-          |-          |-          |-          |-      |
| Reference                     | X                                                                                 | 1     | 0         | Center    | Center    | 0         | 0     |
| Value                         | 25M                                                                               | 1     | 0         | Center    | Center    | 0         | 0     |
| Footprint                     | KL_Footprints:VXM7                                                                | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet                     | https://ww1.microchip.com/downloads/en/DeviceDoc/VXM7-Website-April-2020.pdf      | 0     | 0         | Center    | Center    | 0         | 0     |
| Description                   | Crystal                                                                           | 0     | 0         | Center    | Center    | 0         | 0     |
| Frequency_Tolerance_in_ppm    | 10                                                                                | 0     | 0         | Center    | Center    | 0         | 0     |
| Load_Capacitance_in_pF        | 32                                                                                | 0     | 0         | Center    | Center    | 0         | 0     |
| Package_LxW_in_mm             | 3.2x2.5                                                                           | 0     | 0         | Center    | Center    | 0         | 0     |
| MPN                           | VXM7-9032-25M0000000                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser                        | 579-M7903225M0000000                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey                       | 150-VXM7-9032-25M0000000CT-ND                                                     | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC                          | C1517995                                                                          | 0     | 0         | Center    | Center    | 0         | 0     |