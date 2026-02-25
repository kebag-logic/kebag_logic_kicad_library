from pathlib import Path
import sexpdata
from .base import KiCadBase

class KiCadProject(KiCadBase):
    def __init__(self, root_schematic: Path):
        self.root_schematic = Path(root_schematic).resolve()

        if not self.root_schematic.exists():
            raise FileNotFoundError(
                f"Root schematic not found: {self.root_schematic}"
            )

    def collect_sheets(self) -> list[Path]:
        """
        Recursively collect all schematic sheets starting from root.
        Returns a sorted list of absolute Path objects including the root sheet.
        """
        all_sheets: set[Path] = set()
        to_process = [self.root_schematic]

        while to_process:
            current = to_process.pop()

            if current in all_sheets:
                continue

            all_sheets.add(current)

            for sub_path in self._extract_subsheet_paths(current):
                if sub_path not in all_sheets:
                    to_process.append(sub_path)

        return sorted(all_sheets)

    def _extract_subsheet_paths(self, sch_path: Path) -> list[Path]:
        sexp = self.load_schematic(sch_path)

        subsheets = []

        def recurse(node):
            if not isinstance(node, list):
                return

            if (
                node
                and isinstance(node[0], sexpdata.Symbol)
                and str(node[0]) == "sheet"
            ):
                for item in node[1:]:
                    if (
                        isinstance(item, list)
                        and len(item) >= 3
                        and isinstance(item[0], sexpdata.Symbol)
                        and str(item[0]) == "property"
                        and str(item[1]) == "Sheetfile"
                    ):
                        filename = str(item[2])
                        subsheets.append(
                            (sch_path.parent / filename).resolve()
                        )
            else:
                for child in node:
                    recurse(child)

        recurse(sexp)
        return subsheets
