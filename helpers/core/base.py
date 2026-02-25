from pathlib import Path
import sexpdata

class KiCadBase:
    @staticmethod
    def load_schematic(path: Path):
        """Load schematic and return S-expression."""
        with open(path, "r", encoding="utf-8") as f:
            return sexpdata.loads(f.read())
