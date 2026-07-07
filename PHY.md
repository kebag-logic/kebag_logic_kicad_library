# Ethernet PHY Symbol Properties

The naming scheme for all Ethernet PHYs is as follows:
```
<PHY Name>
```
For a PHY with the name `DP83867IRPAPR`, this would result in
```
DP83867IRPAPR
```

## PHY footprint and package rules

- Each PHY symbol uses an appropriate symbol that shows all pins in a single alignment. Multiple GND are not to be overlayed each other.
- Each symbol must have a footprint assigned.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `U` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **Interface**: MAC-side interface(s), e.g. `RGMII/SGMII`.
- **Speed**: Supported link speeds, e.g. `10/100/1000Base-T`.
- **I_VDD_A**: Typical total supply current in A.
- **MPN**: Manufacturer Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## PHY, full example
| Name              | Value                                     | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                  |-                                          |-      |-          |-          |-          |-          |-      |
| Reference         | U                                         | 1     | 0         | Center    | Center    | 0         | 0     |
| Value             | DP83867IRPAPR                             | 1     | 0         | Center    | Center    | 0         | 0     |
| Footprint         | KL_Footprints:HTQFP-64_10x10mm_P0.5mm     | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet         | https://www.ti.com/lit/gpn/dp83867ir      | 0     | 0         | Center    | Center    | 0         | 0     |
| Description       | Ethernet PHY                              | 0     | 0         | Center    | Center    | 0         | 0     |
| Interface         | RGMII/SGMII                               | 0     | 0         | Center    | Center    | 0         | 0     |
| Speed             | 10/100/1000Base-T                         | 0     | 0         | Center    | Center    | 0         | 0     |
| I_VDD_A           | TBD                                       | 0     | 0         | Center    | Center    | 0         | 0     |
| MPN               | DP83867IRPAPR                             | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser            | 595-DP83867IRPAPR                         | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey           | TBD                                       | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC              | TBD                                       | 0     | 0         | Center    | Center    | 0         | 0     |
