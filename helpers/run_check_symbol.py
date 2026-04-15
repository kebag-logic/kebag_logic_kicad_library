import argparse
from core.kicad_symbol_parser import KiCadSymbolParser
from core.symbol_validator import SymbolValidator


def main():

    parser = argparse.ArgumentParser(
        description="Check a library for consistency"
    )
    parser.add_argument(
        "symbol_lib",
        type=str,
        help="Path to the symbol lib"
    )

    args = parser.parse_args()

    # --- parse ---
    lib = KiCadSymbolParser(symbol_lib=args.symbol_lib)

    # --- validate ---
    validator = SymbolValidator(symbol_type=lib.symbol_type)

    _ = validator.validate(
        properties=lib.properties,
        reference_entry=lib.reference_entry
    )


if __name__ == "__main__":
    main()
