# MCU Symbol Properties

The naming scheme for all MCUs is as follows:
```
<MCU Name>
```
For a MCU with the name `STM32H742VGT6`, this would result in
```
STM32H742VGT6
```

## MCU footprint and package rules

- Each MCU symbol uses an appropriate symbol that shows all pins in a single alignment. Multiple GND are not to be overlayed each other.
- Each symbol must have a footprint assigned.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `U` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **VIN_MAX_V**: Max. input voltage that the MCU can operate on in V.
- **`I_<rail-name>A`**: The typical max. current consumption per rail in A. Do not use the value from the absolute maximum ratings as this value does not represent normal operating conditions.
- **MPN**: Manufacturer Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **Farnell**: Order number of this component at Farnell.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## MCU, full example
| Name                          | Value                                                                             | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                              |-                                                                                  |-      |-          |-          |-          |-          |-      |
| Reference                     | U                                                                                 | 1     | 0         | Center    | Center    | 0         | 0     |
| Value                         | STM32H742VGT6                                                                     | 1     | 0         | Center    | Center    | 0         | 0     |
| Footprint                     | KL_Footprints:LQFP-100_14x14mm_P0.5mm                                             | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet                     | https://www.st.com/resource/en/datasheet/stm32h742vg.pdf                          | 0     | 0         | Center    | Center    | 0         | 0     |
| Description                   | MCU                                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| VIN_MAX_V                     | 4                                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| I_DD_max_A                    | 0.544                                                                             | 0     | 0         | Center    | Center    | 0         | 0     |
| MPN                           | STM32H742VGT6                                                                     | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser                        | 511-STM32H742VGT6                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey                       | 497-STM32H742VGT6-ND                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC                          | C730175                                                                           | 0     | 0         | Center    | Center    | 0         | 0     |