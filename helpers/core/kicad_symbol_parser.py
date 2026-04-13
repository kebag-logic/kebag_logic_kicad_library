import re
from pathlib import Path
from sexpdata import Symbol
from .base import KiCadBase


class KiCadSymbolParser(KiCadBase):

    def __init__(self, symbol_lib):
        self.symbol_lib = Path(symbol_lib).resolve()

        if not self.symbol_lib.exists():
            raise FileNotFoundError(
                f"Root symbol lib not found: {self.symbol_lib}"
            )

        self.data = self.load_library()
        self.symbols = self.extract_symbols()
        self.properties = self.extract_all_properties()
        self.reference_entry = self.extract_reference_entry()
        self.symbol_type = self.extract_symbol_type()

    def load_library(self):
        print(f"Reading: {self.symbol_lib}")
        return self.load_file(self.symbol_lib)

    def extract_symbols(self):
        symbols = []

        for item in self.data:
            if self._is_symbol(item, "symbol"):
                symbol_name = item[1]
                symbols.append((symbol_name, item))
        if not symbols:
            raise AttributeError("Could not extract any symbols")

        print(f"Found {len(symbols)} symbols.")
        return symbols

    def extract_all_properties(self):
        print("Extracting properties.")
        properties = {}

        for name, sym in self.symbols:
            properties[name] = self.extract_properties(sym)

        return properties

    def extract_reference_entry(self):
        for name, sym_expr in self.properties.items():
            if '{' in name and '}' in name:
                print(f"Found reference: {name}")
                return name, sym_expr
        raise KeyError("Could not find reference symbol")

    def extract_symbol_type(self):
        return self.reference_entry[0][0]

    def extract_properties(self, symbol_expr):
        props = {}

        for item in symbol_expr:
            if not self._is_symbol(item, "property"):
                continue

            key = item[1]
            value = item[2]

            if isinstance(value, Symbol):
                value = value.value()
            elif isinstance(value, list):
                value = str(value)

            props[key] = value

        return props

    def _is_symbol(self, expr, name):
        return isinstance(expr, list) and isinstance(expr[0], Symbol) and expr[0].value() == name
