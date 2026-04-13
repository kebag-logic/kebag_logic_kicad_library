from pathlib import Path

class FileSaver:
    def __init__(self, path_to_file):
        self.path_to_file = Path(path_to_file).resolve()

    def save_markdown(self, md_table: str):
        with open(self.path_to_file, "w", encoding="utf-8") as f:
            f.write(md_table)
        print(f"Markdown table saved to {self.path_to_file}")