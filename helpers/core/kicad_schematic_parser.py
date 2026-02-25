from pathlib import Path
import sexpdata
from .symbol import Symbol
from .base import KiCadBase


class KiCadSchematicParser(KiCadBase):

    def parse_file(self, path: Path) -> list[Symbol]:
        sexp = self.load_schematic(path)
        return self._extract_symbols(sexp)

    def _extract_symbols(self, sexp) -> list[Symbol]:
        symbols = []

        def recurse(node):
            if not isinstance(node, list):
                return

            if node and isinstance(node[0], sexpdata.Symbol) and str(node[0]) == "symbol":
                properties = {}
                reference = None
                value = None

                for item in node[1:]:
                    if not isinstance(item, list):
                        continue

                    head = item[0]

                    # --- Properties ---
                    if isinstance(head, sexpdata.Symbol) and str(head) == "property":
                        name = str(item[1])
                        val = str(item[2])
                        properties[name] = val

                        if name == "Value":
                            value = val

                    # --- Instances (real reference) ---
                    elif isinstance(head, sexpdata.Symbol) and str(head) == "instances":
                        for inst in item[1:]:
                            if isinstance(inst, list):
                                for sub in inst:
                                    if (
                                        isinstance(sub, list)
                                        and sub
                                        and str(sub[0]) == "path"
                                    ):
                                        for p in sub:
                                            if (
                                                isinstance(p, list)
                                                and p
                                                and str(p[0]) == "reference"
                                            ):
                                                reference = str(p[1])

                if reference:
                    symbols.append(Symbol(reference, value, properties))

            else:
                for child in node:
                    recurse(child)

        recurse(sexp)
        return symbols