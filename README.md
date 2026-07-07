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

        | Library name            | Path                                              | Description |
        |-------------------------|---------------------------------------------------|-------------|
        | KL_R                    | {$KL_LIB}/symbols/KL_R.kicad_sym                  | Contains all resistors |
        | KL_C                    | {$KL_LIB}/symbols/KL_C.kicad_sym                  | Contains all capacitors |
        | KL_Ferrites             | {$KL_LIB}/symbols/KL_Ferrites.kicad_sym           | Contains all ferrite beads |
        | KL_Passive_ICs          | {$KL_LIB}/symbols/KL_Passive_ICs.kicad_sym        | Contains all passive ICs |
        | KL_L                    | {$KL_LIB}/symbols/KL_L.kicad_sym                  | Contains all inductors |
        | KL_IC_LAN9645xF         | {$KL_LIB}/symbols/KL_IC_LAN9645xF.kicad_sym       | Contains the LAN9645xF |
        | KL_Connectors_RJ45      | {$KL_LIB}/symbols/KL_Connectors_RJ45.kicad_sym    | Contains all RJ45 connectors |
        | KL_Voltage_Regulators   | {$KL_LIB}/symbols/KL_Voltage_Regulators.kicad_sym | Contains all voltage regulators |
        | KL_TP                   | {$KL_LIB}/symbols/KL_TP.kicad_sym                 | Contains all test points |
        | KL_Headers              | {$KL_LIB}/symbols/KL_Headers.kicad_sym            | Contains all pin headers |
        | KL_Flags                | {$KL_LIB}/symbols/KL_Flags.kicad_sym              | Contains all flags |
        | KL_MCU                  | {$KL_LIB}/symbols/KL_MCU.kicad_sym                | Contains all MCUs |
        | KL_Connector            | {$KL_LIB}/symbols/KL_Connector.kicad_sym          | Conntains all connectors |
        | KL_LED                  | {$KL_LIB}/symbols/KL_LED.kicad_sym                | Contains all LEDs |
        | KL_Transistor           | {$KL_LIB}/symbols/KL_Transistor.kicad_sym         | Contains all transistors |
        | KL_Oscillator           | {$KL_LIB}/symbols/KL_Oscillator.kicad_sym         | Contains all active oscillators |
        | KL_PHY                  | {$KL_LIB}/symbols/KL_PHY.kicad_sym                | Contains all Ethernet PHYs |
        | KL_Module               | {$KL_LIB}/symbols/KL_Module.kicad_sym             | Contains all board modules |

    5. Confirm with **OK**
    6. The libraries are now available in the Symbol Chooser.

4. Add the footprint libraries

    1. Open **Preferences → Manage Footprint Libraries...**
    2. Select **Global Libraries** (recommended) or **Project Specific Libraries**
    3. Click **Add existing library**
    4. Add the following footprint library:

        | Library name | Path | Description |
        |--------------|------|-|
        | `KL_Footprints` | `${KL_LIB}/footprints/KL_Footprints.pretty` | Contains all footprints |
    5. Confirm with **OK**
    6. The footprint library is now available in the Footprint Chooser.

## Adding components to a library

The main principle of the Kebag Logic Libraries is: Each value (resistance, capacitance, ...) has a dedicated symbol with a dedicated footprint. This helps to select a component with a specific value, tolerance etc. With that approach creating BOMs and estimating price points is a simple next step.

Please follow these guidelines to add a component to the library:

- [Resistor Guidelines](RESISTOR.md)
- [Capacitor Guidelines](CAPACITOR.md)
- [Inductor Guidelines](INDUCTOR.md)
- [Crystal Guidelines](CRYSTAL.md)
- [Footprint Guidelines](FOOTPRINTS.md)

## Kebag Logic Signal Naming Scheme

Please follow the guidelines in [Signal Naming Convention](SIGNAL_NAMING_CONVENTION.md).

## Kebag Logic Bus Pull-up and Pull-down Resistor Placement

All pull-up and pull-down resistors that define the idle or default level of a shared communication bus (for example I2C SDA and SCL) shall be placed exclusively in the root schematic sheet.

These resistors must not be placed inside hierarchical sub-sheets, regardless of how often the sub-sheet is instantiated. This rule ensures that bus biasing is always visible at top level and prevents accidental duplication or omission.

## License

tbd