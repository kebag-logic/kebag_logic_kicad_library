# Kebag Logic Helper Scripts

A collection of helper scripts to make live easier.

## Usage

### run_calculate_current_consumption.py

A script that collects current consumption on the rails defined in each component.
- Run with `python run_calculate_current_consumption.py <root-schematic> <output-file>`
- Run with `python run_calculate_current_consumption.py --help` to see command line options.

### run_generate_pin_out.py

**Important:** Requires a KiCAD 9.x installation.

A script that generates the pin out for a specified component.
- Run with `python run_generate_pin_out.py <root-schematic> <output-file>`
- Run with `python run_generater_pin_out.py --help` to see command line options.

### run_check_symbol.py

A script that validates consistent parameter entries in the respective symbol.

- Run with `python run_check_symbol.py <symbols/symbol.kicad_sym>`.
- Run with `python run_check_symbol.py --help` to see command line options.