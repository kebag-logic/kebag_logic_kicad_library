# Header Symbol Properties

The naming scheme for all headers is as follows:
```
Header_{No_of_Pins}x{No_of_Rows}_{Pitch_pin_in_mm}_{Pitch_row_in_mm}_{Orientation}
```
For a 10x2 pin header this would result in
```
Header_10x2_2.54mm_2.54mm_Straight
```

## Header footprint and package rules

- Each header symbol uses an appropriate symbol that shows all pins in a single alignment. Multiple GND are not to be overlayed each other.
- Each symbol must have a footprint assigned.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `J` and must not be fixed in the symbol.

## Pin 1 identification

- Pin 1 is marked with a rectangular pad
- All other pins have a circular pad

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **No_of_pins**: The number of pins per row.
- **No_of_rows**: The number of rows.
- **Pitch_pin_in_mm**: The pitch between pins in mm.
- **Pitch_row_in_mm**: The pitch between rows in mm.
- **Orientation**: The orientation of the header. Straight or RightAngle.
- **MPN**: Manufacturer Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## Header full example
| Name                          | Value                                                                             | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                              |-                                                                                  |-      |-          |-          |-          |-          |-      |
| Reference                     | J                                                                                 | 1     | 0         | Center    | Center    | 0         | 0     |
| Value                         |                                                                                   | 0     | 0         | Center    | Center    | 0         | 0     |
| Footprint                     | KL_Footprints:10x02_2.54mm_Header                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet                     | https://app.adam-tech.com/products/download/data_sheet/203218/bhr-xx-vua-data-sheet.pdf          | 0     | 0         | Center    | Center    | 0         | 0     |
| Description                   | Pin Header                                                                        | 0     | 0         | Center    | Center    | 0         | 0     |
| No_of_pins                    | 10                                                                                | 0     | 0         | Center    | Center    | 0         | 0     |
| No_of_rows                    | 2                                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| Pitch_pin_in_mm               | 2.54                                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| Pitch_row_in_mm               | 2.54                                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| Orientation                   | Straight                                                                          | 0     | 0         | Center    | Center    | 0         | 0     |
| MPN                           | BHR-20-VUA                                                                        | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser                        | 737-BHR-20-VUA                                                                    | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey                       | 2057-BHR-20-VUA-ND                                                                | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC                          | C598987                                                                           | 0     | 0         | Center    | Center    | 0         | 0     |