# Transistor Symbol Properties

The naming scheme for all transistors (FETs and BJTs) is as follows:
```
<Transistor Name>
```
For a transistor with the name `BSS138LT1G`, this would result in
```
BSS138LT1G
```

## Transistor footprint and package rules

- Each transistor symbol uses an appropriate symbol that shows all pins in a single alignment.
- Each symbol must have a footprint assigned.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `Q` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **Type**: Transistor type, e.g. `N-Channel MOSFET`, `P-Channel MOSFET`, `NPN`, `PNP`.
- **V_DS_in_V**: Max. drain-source (or collector-emitter) voltage in V.
- **I_D_in_A**: Max. continuous drain (or collector) current in A.
- **R_DS_on_in_Ohm**: On-resistance in Ohm at the datasheet reference V_GS (FETs only).
- **MPN**: Manufacturer Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## Transistor, full example
| Name              | Value                                              | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                  |-                                                   |-      |-          |-          |-          |-          |-      |
| Reference         | Q                                                  | 1     | 0         | Center    | Center    | 0         | 0     |
| Value             | BSS138LT1G                                         | 1     | 0         | Center    | Center    | 0         | 0     |
| Footprint         | KL_Footprints:SOT-23                               | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet         | https://www.onsemi.com/pdf/datasheet/bss138lt1-d.pdf | 0   | 0         | Center    | Center    | 0         | 0     |
| Description       | N-Channel MOSFET                                   | 0     | 0         | Center    | Center    | 0         | 0     |
| Type              | N-Channel MOSFET                                   | 0     | 0         | Center    | Center    | 0         | 0     |
| V_DS_in_V         | 50                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| I_D_in_A          | 0.22                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| R_DS_on_in_Ohm    | 3.5                                                | 0     | 0         | Center    | Center    | 0         | 0     |
| MPN               | BSS138LT1G                                         | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser            | 863-BSS138LT1G                                     | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey           | TBD                                                | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC              | TBD                                                | 0     | 0         | Center    | Center    | 0         | 0     |
