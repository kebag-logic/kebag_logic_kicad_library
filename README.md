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
        | `KL_L` | `${KL_LIB}/symbols/KL_L.kicad_sym` | Contains all inductances. |
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

The main principle of the Kebag Logic Libraries is: Each value (resistance, capacitance, ...) has a dedicated symbol with a dedicated footprint. This helps to select a component with a specific value, tolerance etc. With that approach creating BOMs and estimating price points is a simple next step.

Please follow these guidelines to add a component to the library:

- [Resistor Guidelines](RESISTOR.md)
- [Capacitor Guidelines](CAPACITOR.md)
- [Inductor Guidelines](INDUCTOR.md)
- [Footprint Guidelines](FOOTPRINTS.md)

## License

tbd