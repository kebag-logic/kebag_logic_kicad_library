from pathlib import Path
import sexpdata
import subprocess
import platform
import shutil
from .base import KiCadBase

class KiCadProject(KiCadBase):
    def __init__(self, root_schematic: Path):
        self.root_schematic = Path(root_schematic).resolve()

        if not self.root_schematic.exists():
            raise FileNotFoundError(
                f"Root schematic not found: {self.root_schematic}"
            )
        self.path_to_kicad = None

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
        sexp = self.load_file(sch_path)

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

    def _resolve_kicad_cli(self, custom_path=None):
        """
        Determine correct kicad-cli executable path.
        Priority:
        1. User provided path
        2. Found in PATH
        3. OS-specific default location
        """

        if custom_path:
            return Path(custom_path)

        cli_in_path = shutil.which("kicad-cli")
        if cli_in_path:
            return Path(cli_in_path)

        system = platform.system()

        # macOS
        if system == "Darwin":
            default_path = Path(
                "/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli"
            )
        # Linux
        elif system == "Linux":
            default_path = Path("/usr/bin/kicad-cli")
        # Windows
        elif system == "Windows":
            default_path = Path(
                r"C:\\Program Files\\KiCad\\9.0\\bin\\kicad-cli.exe"
            )

        else:
            raise RuntimeError(f"Unsupported OS: {system}")

        if not default_path.exists():
            raise FileNotFoundError(
                "Could not find kicad-cli automatically. "
                "Please provide path_to_kicad."
            )

        return default_path

    def export_netlist(self, output_file=None, path_to_kicad=None):
        cli = self._resolve_kicad_cli(path_to_kicad)
        path_to_xml = Path(output_file) if output_file else Path("netlist.xml").resolve()

        print(f"Processing: {self.root_schematic}...")
        subprocess.run(
            [
                str(cli),
                "sch",
                "export",
                "netlist",
                str(self.root_schematic),
                "-o",
                str(path_to_xml),
            ],
            check=True,
        )
        print(f"Done. File in {path_to_xml}")
        return path_to_xml
