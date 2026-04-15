# Voltage Regulator Symbol Properties

The naming scheme for all voltage regulators is as follows:
```
<Voltage Regulator Name>
```
For a voltage regulator with the name `TPS564257DRLR`, this would result in
```
TPS564257DRLR
```

## Voltage regulator footprint and package rules

- Each voltage regulator symbol uses an appropriate symbol that shows all pins in a single alignment. Multiple GND are not to be overlayed each other.
- Each symbol must have a footprint assigned.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `U` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **VIN_MIN_V**: Min. input voltage that the voltage regulator can process in V.
- **VIN_MAX_V**: Max. input voltage that the voltage regulator can process in V.
- **I_OUT_A**: Max. output current the voltage regulator can provide in A.
- **I_VIN_A**: The current the voltage regulator consumes provided in A.
- **MPN**: Manufacturer Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **Farnell**: Order number of this component at Farnell.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## Voltage regulator, full example
| Name                          | Value                                                                             | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                              |-                                                                                  |-      |-          |-          |-          |-          |-      |
| Reference                     | U                                                                                 | 1     | 0         | Center    | Center    | 0         | 0     |
| Value                         | TPS564257DRLR                                                                     | 1     | 0         | Center    | Center    | 0         | 0     |
| Footprint                     | KL_Footprints:SOT-563                                                             | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet                     | https://www.ti.com/lit/gpn/tps564257                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| Description                   | Voltage Regulator                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| VIN_MIN_V                     | 3                                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| VIN_MAX_V                     | 17                                                                                | 0     | 0         | Center    | Center    | 0         | 0     |
| I_OUT_A                       | 4                                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| I_VIN_A                       | 0.000370                                                                          | 0     | 0         | Center    | Center    | 0         | 0     |
| MPN                           | TPS564257DRLR                                                                     | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser                        | 595-TPS564257DRLR                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey                       | 296-TPS564257DRLRCT-ND                                                            | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC                          | C19272233                                                                         | 0     | 0         | Center    | Center    | 0         | 0     |