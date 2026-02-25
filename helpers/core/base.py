from pathlib import Path
import sexpdata

class KiCadBase:
    @staticmethod
    def load_file(path: Path):
        """Load file and return S-expression."""
        with open(path, "r", encoding="utf-8") as f:
            return sexpdata.loads(f.read())
