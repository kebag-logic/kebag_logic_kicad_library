# RF Connector Symbol Properties

The naming scheme for all RF connectors is as follows:
```
Conn-RF_{Shape}_{Gender}_{Orientation}_{Impedance_in_Ohm}_{Freq_rating_in_GHz}
```
For a SMA connector, this would result in
```
Conn-RF_SMA_Female_RightAngle_50Ohm_6GHz
```

## RF Connector footprint and package rules

- Each RF connector symbol uses an appropriate symbol that shows all pins in a single alignment. Multiple GND are not to be overlayed each other.
- Each symbol must have a footprint assigned.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `J` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---

- **Shape**: Mechanical interface type of the RF connector (e.g. SMA, SMB, MCX, BNC, N_Type).
- **Gender**: Defines the connector gender and polarity:
  - `Male`: Center pin present
  - `Female`: Center receptacle
  - `RP_Male`: Reverse polarity male
  - `RP_Female`: Reverse polarity female

- **Orientation**: Mounting direction of the connector relative to the PCB:
  - `Straight`: Vertical or top entry
  - `RightAngle`: 90 degree orientation

- **Impedance_in_Ohm**: Nominal characteristic impedance in Ohm (typically 50 or 75).
- **Freq_Rating_in_GHz**: Maximum specified operating frequency in GHz.
- **MPN**: Manufacturer Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the Cut Tape CT number.
- **LCSC**: Order number of a component with identical specifications at LCSC (https://lcsc.com).

## RF Connector full example
| Name                          | Value                                                                             | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                              |-                                                                                  |-      |-          |-          |-          |-          |-      |
| Reference                     | J                                                                                 | 1     | 0         | Center    | Center    | 0         | 0     |
| Value                         | SMA                                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| Footprint                     | KL_Footprints:SMA_Right_Angle                                                     | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet                     | https://gct.co/pdfjs/web/viewer.html?file=/files/drawings/RFPC-SMA27-F.pdf        | 0     | 0         | Center    | Center    | 0         | 0     |
| Description                   | small coaxial connector                                                           | 0     | 0         | Center    | Center    | 0         | 0     |
| Shape                         | SMA                                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| Gender                        | Female                                                                            | 0     | 0         | Center    | Center    | 0         | 0     |
| Orientation                   | RightAngle                                                                        | 0     | 0         | Center    | Center    | 0         | 0     |
| Impedance_in_Ohm              | 50                                                                                | 0     | 0         | Center    | Center    | 0         | 0     |
| Freq_rating_in_GHz            | 6                                                                        | 0     | 0         | Center    | Center    | 0         | 0     |
| MPN                           | RFPC-SMA27-F                                                                      | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser                        | 640-RFPCSMA27F                                                                    | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey                       | 2073-RFPC-SMA27-F-ND                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC                          | C49253491                                                                         | 0     | 0         | Center    | Center    | 0         | 0     |