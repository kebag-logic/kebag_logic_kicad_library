# Data Connector Symbol Properties

The naming scheme for all data connectors is as follows:
```
{Type}_<component-name>
```
For a RJ45 connector with the component name 0826-1X4T-43-F, this would result in
```
RJ45_0826-1X4T-43-F
```

## Data Connector footprint and package rules

- Each data connector symbol uses an appropriate symbol that shows all pins in a single alignment. Multiple GND are not to be overlayed each other.
- Each symbol must have a footprint assigned.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `J` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---

- **MPN**: Manufacturer Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the Cut Tape CT number.
- **LCSC**: Order number of a component with identical specifications at LCSC (https://lcsc.com).

## Data Connector full example
| Name                          | Value                                                                             | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                              |-                                                                                  |-      |-          |-          |-          |-          |-      |
| Reference                     | J                                                                                 | 1     | 0         | Center    | Center    | 0         | 0     |
| Value                         | SMA                                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| Footprint                     | KL_Footprints:BEL_0826-1X4T-43-F                                                  | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet                     | https://www.belfuse.com/media/drawings/products/magjack%20ICMs/dr-mag-0826-1x4t-43-f.pdf        | 0     | 0         | Center    | Center    | 0         | 0     |
| Description                   | RJ45 Connector                                                           | 0     | 0         | Center    | Center    | 0         | 0     |
| MPN                           | 0826-1X4T-43-F                                                                      | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser                        | 530-0826-1X4T-43-F                                                                    | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey                       | 5923-0826-1X4T-43-F-ND                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC                          | C6776265                                                                         | 0     | 0         | Center    | Center    | 0         | 0     |