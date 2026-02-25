import re
import argparse
from core.kicad_project import KiCadProject
from core.kicad_netlist_parser import KiCadNetlistParser
from core.file_saver import FileSaver

def sanitize_filename(name: str) -> str:
    # Replace any character not a-z, A-Z, 0-9, dash, underscore, or dot with underscore
    return re.sub(r"[^a-zA-Z0-9._-]", "_", name)

def main():
    parser = argparse.ArgumentParser(
        description="Generate pin out file for components in the schematic"
    )
    parser.add_argument(
        "root_sch",
        type=str,
        help="Path to the root KiCad schematic file (e.g., shish-lan.kicad_sch)"
    )
    parser.add_argument(
        "component_name",
        type=str,
        help="Name of the component (e.g., U4)"
    )
    parser.add_argument(
        "output_md",
        nargs="?",  # optional positional argument
        default="pin_out.md",
        type=str,
        help="Path to the output markdown file (default: <component>_pin_out.md)"
    )
    args = parser.parse_args()

    project = KiCadProject(root_schematic=args.root_sch)
    xml = project.export_netlist()

    parser = KiCadNetlistParser(xml)
    md_table, cmp_name = parser.generate_markdown_for_component(reference=args.component_name)

    # Determine output filename
    if args.output_md and args.output_md != "pin_out.md":
        # User specified a filename
        filename = args.output_md
    else:
        # Default filename based on component
        filename = "documentation/" + sanitize_filename(f"{cmp_name['ref']}-{cmp_name['value']}_pin_out.md")
    saver = FileSaver(filename)
    saver.save_markdown(md_table)


if __name__ == "__main__":
    main()