from pathlib import Path
import re
from decimal import Decimal
import sexpdata

class KiCadSchematicParser:
    def __init__(self, root_schematic, field_prefix="I_", filter_prefix="L"):
        self.root_schematic = root_schematic
        self.field_prefix = field_prefix
        self.filter_prefix = filter_prefix

        self.all_sheets = None
        self.all_components = None
        self.md_table = None

    def extract_sheets(self):
        """
        Recursively collect all schematic sheets starting from root.
        Returns a set of absolute Path objects including the root sheet.
        """

        root_path = Path(self.root_schematic).resolve()
        all_sheets = set()
        to_process = [root_path]

        while to_process:
            current = to_process.pop()

            if current in all_sheets:
                continue

            if not current.exists():
                print(f"Warning: Sheet not found: {current}")
                continue

            all_sheets.add(current)

            # Extract subsheets
            subsheets = self.extract_subsheet_files(current)

            for sub in subsheets:
                sub_path = (current.parent / sub).resolve()
                if sub_path not in all_sheets:
                    to_process.append(sub_path)

        self.all_sheets = sorted(all_sheets)

    def extract_subsheet_files(self, sch_path: Path):
        """
        Extract direct subsheet file names from a KiCad 6/7/8/9 schematic.
        Returns relative filenames as stored in the schematic.
        """
        pattern = re.compile(r'\(property\s+"Sheetfile"\s+"([^"]+)"')

        with open(sch_path, "r", encoding="utf-8") as f:
            content = f.read()

        return pattern.findall(content)

    def collect_all_components(self):
        """
        Extracts all components from the given list of KiCad schematic files,
        merges duplicates by reference, retrieves their 'Value' property, and
        returns a sorted list of tuples (ref, value, currents_dict).

        Parameters:
            all_sheets: list of KiCad schematic file paths
            field_prefix: prefix to identify current properties (default 'I_')

        Returns:
            List of tuples: (Reference, Value, Currents dict), sorted by reference
        """
        all_components_dict = {}  # Key: reference, Value: dict with 'value' and currents
        ref_pattern = re.compile(r"^[A-Z]+\d+$")  # Only accept refs like U1, L2, R3, etc.

        for sheet in self.all_sheets:
            # Extract symbols with currents
            sheet_components = self.extract_symbols_from_file(sheet)

            for ref, currents in sheet_components.items():
                # Skip symbols without proper numbered references
                if not ref_pattern.match(ref):
                    continue

                # Use a dict to hold the Value property
                value_holder = {'value': None}

                # Parse schematic again to find the Value property for this reference
                path = Path(sheet).resolve()
                sexp = self.parse_kicad_sch(path)

                def _find_value(node):
                    if not isinstance(node, list) or len(node) == 0:
                        return
                    head = node[0]
                    if isinstance(head, sexpdata.Symbol) and str(head) == "symbol":
                        ref_candidate = None
                        for item in node[1:]:
                            if isinstance(item, list) and len(item) >= 3:
                                if isinstance(item[0], sexpdata.Symbol) and str(item[0]) == "property":
                                    prop_name = str(item[1])
                                    prop_value = str(item[2])
                                    if prop_name == "Reference":
                                        ref_candidate = prop_value
                                    elif prop_name == "Value" and ref_candidate == ref:
                                        value_holder['value'] = prop_value
                    else:
                        for child in node:
                            _find_value(child)

                _find_value(sexp)

                # Merge into master dict
                if ref in all_components_dict:
                    all_components_dict[ref]['currents'].update(currents)
                else:
                    all_components_dict[ref] = {'value': value_holder['value'], 'currents': currents}

        # Convert to list of tuples and sort by reference
        all_components = sorted(
            [(ref, info['value'], info['currents']) for ref, info in all_components_dict.items()],
            key=lambda x: x[0]
        )

        self.all_components = all_components

    def extract_symbols_from_file(self, sch_path: str):
        path = Path(sch_path).resolve()
        sexp = self.parse_kicad_sch(path)
        return self.extract_symbols(sexp)

    def extract_symbols(self, sexp):
        results_dict = {}

        def _recurse(node):
            if not isinstance(node, list) or len(node) == 0:
                return

            head = node[0]
            if isinstance(head, sexpdata.Symbol) and str(head) == "symbol":
                ref = None
                currents = {}
                for item in node[1:]:
                    if isinstance(item, list) and len(item) >= 3:
                        if isinstance(item[0], sexpdata.Symbol) and str(item[0]) == "property":
                            prop_name = str(item[1])
                            prop_value = str(item[2])
                            if prop_name == "Reference":
                                ref = prop_value
                            elif prop_name.startswith(self.field_prefix):
                                try:
                                    currents[prop_name] = float(prop_value)
                                except ValueError:
                                    print(f"Warning: could not parse {prop_value} for {ref}")
                if ref and currents:
                    if ref in results_dict:
                        results_dict[ref].update(currents)
                    else:
                        results_dict[ref] = currents
            else:
                for child in node:
                    _recurse(child)

        _recurse(sexp)
        return results_dict

    def parse_kicad_sch(self, path: Path):
        """Parse a KiCad schematic file into an S-expression tree."""
        print(f"Reading: {path}")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return sexpdata.loads(content)

    def generate_markdown_table(self):
        """
        Generate a markdown table from a list of components.

        all_components: List of tuples (ref, value, currents_dict)
        Components with reference starting with 'L' are ignored.
        """
        # Filter out 'L' components
        filtered_components = [(ref, value, currents) for ref, value, currents in self.all_components if not ref.startswith("L")]

        # 1. Collect all current property names
        current_fields = set()
        for _, _, currents in filtered_components:
            current_fields.update(currents.keys())
        current_fields = sorted(current_fields)  # sort alphabetically

        # 2. Header row
        header = ["Identifier", "Name"] + current_fields
        md_lines = ["| " + " | ".join(header) + " |"]
        md_lines.append("|" + "---|" * len(header))  # separator

        # 3. Component rows
        for ref, value, currents in filtered_components:
            row = [ref, value if value else ""]
            for field in current_fields:
                # Round to 6 decimals for clean display
                val = currents.get(field, "")
                if isinstance(val, float):
                    val = round(val, 6)
                row.append(str(val))
            md_lines.append("| " + " | ".join(row) + " |")

        # 4. Sum row for numeric values
        sum_row = ["Sum", ""]
        for field in current_fields:
            total = sum(Decimal(str(currents.get(field, 0))) for _, _, currents in filtered_components)
            # Round for display
            total = round(float(total), 6) if total else ""
            sum_row.append(str(total) if total else "")
        md_lines.append("| " + " | ".join(sum_row) + " |")

        self.md_table = "\n".join(md_lines)

    def save_markdown_to_file(self, file_path="power_budget.md"):
        """
        Save a markdown string to a file.

        md_text: The markdown text to save
        file_path: Path to the .md file
        """
        path = Path(file_path).resolve()
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.md_table)
        print(f"Markdown table saved to {path}")