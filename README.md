# Kebag Logic KiCad Library

This library contains all components used in Kebag Logic Hardware Projects. The Library has been created using KiCad 9.

## Installation

1. Clone the repository. Clone this library to a location of your choice.
In the following steps we assume the library is located at: `~/kebag_logic_kicad_library/`

2. Configure the KiCad path variable
    1. Open **Preferences → Configure Paths...**
    2. Click the **+** button to add a new entry
    3. Set:
        - **Name:** `KL_LIB`
        - **Path:** `~/kebag_logic_kicad_library`

    This path variable is used by all libraries listed below.
3. Add the symbol libraries
    1. Open **Preferences → Manage Symbol Libraries...**
    2. Select **Global Libraries** (recommended) or **Project Specific Libraries**
    3. Click **Add existing library**
    4. Add the following symbol libraries:

        | Library name | Path | Description |
        |--------------|------|-|
        | `KL_R` | `${KL_LIB}/symbols/KL_R.kicad_sym` | Contains all resistors. |
        | `KL_C` | `${KL_LIB}/symbols/KL_C.kicad_sym` | Contains all capacitors. |
        | `KL_MCU` | `${KL_LIB}/symbols/KL_MCU.kicad_sym` | Contains all microcontrollers. |
        | `KL_Voltage_Regulators` | `${KL_LIB}/symbols/KL_Voltage_Regulators.kicad_sym` | Contains all voltage regulators. |
        | `KL_TP` | `${KL_LIB}/symbols/KL_TP.kicad_sym` | Contains all test points. |
    5. Confirm with **OK**
    6. The libraries are now available in the Symbol Chooser.

4. Add the footprint libraries

    1. Open **Preferences → Manage Footprint Libraries...**
    2. Select **Global Libraries** (recommended) or **Project Specific Libraries**
    3. Click **Add existing library**
    4. Add the following footprint library:

        | Library name | Path | Description |
        |--------------|------|-|
        | `KL_Footprints` | `${KL_LIB}/footprints/KL_Footprints.pretty` | Contains all footprints
    5. Confirm with **OK**
    6. The footprint library is now available in the Footprint Chooser.

## Adding components to a library

The main principle of the Kebag Logic Libraries is: Each value (resistance, capacitance, ...) has a dedicated symbol. This helps to select a component with a specific value, tolerance etc. With that approach creating BOMs and estimating price points is a simple next step.

## Resistor Symbol Properties

The naming scheme for all resistors is as follows:
```
R_{Value}_{Power_in_W}_{Tolerance_in_pct}_{Package_in_inch}
```

### Footprint and package rules

- Each symbol must have a footprint assigned.
- The footprint must match the package size defined in the `Package_in_inch` field.
- Preferred SMD size: 0603. Exceptions allowed if the required value is not available in 0603.
- Resistor values are without the SI Unit. Values <= 0 are entered with an R as postfix. E.g. `0R`.
- The kilo, mega, ... postfixes are written in capital letters.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `R` and must not be fixed in the symbol.

### Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **Power_in_W**: The power the resistor can handle in Watts.
- **Tolerance_in_pct**: Resistor value tolerance in %.
- **Package_in_inch**: The package size in inch.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **Farnell**: Order number of this component at Farnell.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

### Resistor, full example
| Name              | Value                                                                             | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                  |-                                                                                  |-      |-          |-          |-          |-          |-      |
| Reference         | R                                                                                 | 1     | 0         | Center    | Center    | 0         | 0     |
| Value             | 10K                                                                               | 1     | 0         | Center    | Center    | 0         | 0     |
| Footprint         | KL_Footprints:R_0603                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet         | https://www.yageogroup.com/content/datasheet/asset/file/PYU-RC_GROUP_51_ROHS_L    | 0     | 0         | Center    | Center    | 0         | 0     |
| Description       | Resistor                                                                          | 0     | 0         | Center    | Center    | 0         | 0     |
| Power_in_W        | 0.1                                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| Tolerance_in_pct  | 1                                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| Package_in_inch   | 0603                                                                              | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser            | 603-RC0603FR-0710KL                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey           | 311-10.0KHRCT-ND                                                                  | 0     | 0         | Center    | Center    | 0         | 0     |
| Farnell           | 2421850                                                                           | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC              | C98220                                                                            | 0     | 0         | Center    | Center    | 0         | 0     |

## Capacitor Symbol Properties

The naming scheme for all resistors is as follows:
```
C_{Value}_{Voltage_in_V}_{Tolerance_in_pct}_{Dielectric}_{Package_in_inch}
```

### Footprint and package rules

- Each symbol must have a footprint assigned.
- The footprint must match the package size defined in the `Package_in_inch` field.
- Preferred SMD size: 0603. Exceptions allowed if the required value is not available in 0603.
- Resistor values are without the SI Unit. All values have a postfix describing the nano, micro, ... range
- The nano, micro, ... postfixes are written in lowercase letters.
- Links to datasheets only from the manufacturer. No supplier datasheets.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `C` and must not be fixed in the symbol.

### Custom fields

- Field names are fixed and must not be changed.
- Units are encoded in the field name to allow automated BOM processing.
---
- **Voltage_in_V**: The voltage the capacitor can handle in Volts.
- **Tolerance_in_pct**: Capacitor value tolerance in %.
- **Dielectric**: Dielectric parameter.
- **Package_in_inch**: The package size in inch.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey. Make sure to provide the **Cut Tape (CT)** number.
- **Farnell**: Order number of this component at Farnell.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

### Capacitor, full example
| Name              | Value                                                                                 | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                  |-                                                                                      |-      |-          |-          |-          |-          |-      |
| Reference         | C                                                                                     | 1     | 0         | Left      | Center    | 0         | 0     |
| Value             | 100n                                                                                  | 1     | 0         | Left      | Center    | 0         | 0     |
| Footprint         | KL_Footprints:C_0603                                                                  | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet         | https://weblib.samsungsem.com/mlcc/mlcc-ec-data-sheet.do?partNumber=CL10B104KB8NNN    | 0     | 0         | Center    | Center    | 0         | 0     |
| Description       | Unpolarized capacitor                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |
| Voltage_in_V      | 10                                                                                    | 0     | 0         | Center    | Center    | 0         | 0     |
| Tolerance_in_pct  | 10                                                                                    | 0     | 0         | Center    | Center    | 0         | 0     |
| Dielectric        | X7R                                                                                   | 0     | 0         | Center    | Center    | 0         | 0     |
| Package_in_inch   | 0603                                                                                  | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser            | 187-CL10B104KB8NNNC                                                                   | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey           | 1276-1000-1-ND                                                                        | 0     | 0         | Center    | Center    | 0         | 0     |
| Farnell           | 4539043                                                                               | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC              | C1591                                                                                 | 0     | 0         | Center    | Center    | 0         | 0     |

## License

tbd