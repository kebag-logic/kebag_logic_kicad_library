# Network Switch Symbol Properties

The naming scheme for all Network Switches is as follows:
```
<NetworkSwitchName>
```
For a MCU with the name `LAN96455F`, this would result in
```
LAN96455F
```

## Network Switch footprint and package rules

- Each Network Switch symbol uses an appropriate symbol that shows all pins in a single alignment. Multiple GND are not to be overlayed each other.
- Each symbol must have a footprint assigned.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `U` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **`I_<rail-name>_A`**: The typical max. current consumption per rail in A. Do not use the value from the absolute maximum ratings as this value does not represent normal operating conditions. Decimal voltage rails are indicated as follows: `3.3V` is written as `3V3`.
- **MPN**: Manufacturer Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **Farnell**: Order number of this component at Farnell.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## Network Switch, full example
| Name                          | Value                                                                             | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                              |-                                                                                  |-      |-          |-          |-          |-          |-      |
| Reference                     | U                                                                                 | 1     | 0         | Center    | Center    | 0         | 0     |
| Value                         | LAN96455F-I/8MW                                                                   | 1     | 0         | Center    | Center    | 0         | 0     |
| Footprint                     | KL_Footprints:TQFP-128_14x14mm_P0.4mm                                             | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet                     | https://ww1.microchip.com/downloads/aemDocuments/documents/NCS/ProductDocuments/DataSheets/LAN9645xF_Data_Sheet_DS00006065.pdf                          | 0     | 0         | Center    | Center    | 0         | 0     |
| Description                   | Network Switch                                                                    | 0     | 0         | Center    | Center    | 0         | 0     |
| I_DD_1V15_max_A               | 0.935                                                                             | 0     | 0         | Center    | Center    | 0         | 0     |
| I_DD_AL_1V15_max_A            | 0.400                                                                             | 0     | 0         | Center    | Center    | 0         | 0     |
| I_DD_ALSx_1V15_max_A          | 0.025                                                                             | 0     | 0         | Center    | Center    | 0         | 0     |
| I_DD_AH25_2V5_max_A           | 0.475                                                                             | 0     | 0         | Center    | Center    | 0         | 0     |
| I_DD_AH33_3V3_max_A           | 0.505                                                                             | 0     | 0         | Center    | Center    | 0         | 0     |
| I_DD_IO25_2V5_max_A           | 0.045                                                                             | 0     | 0         | Center    | Center    | 0         | 0     |
| I_DD_IO33_3V3_max_A           | 0.075                                                                             | 0     | 0         | Center    | Center    | 0         | 0     |
| I_DD_IOD                      | 0.005                                                                             | 0     | 0         | Center    | Center    | 0         | 0     |
| MPN                           | LAN96455F-I/8MW                                                                   | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser                        | 579-LAN96455FI8MW                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey                       | 150-LAN96455F-I/8MW-ND                                                            | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC                          | C730175                                                                           | 0     | 0         | Center    | Center    | 0         | 0     |