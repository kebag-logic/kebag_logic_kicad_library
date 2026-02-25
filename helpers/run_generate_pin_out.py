import argparse
from core.kicad_project import KiCadProject
from core.kicad_netlist_parser import KiCadNetlistParser
from core.file_saver import FileSaver

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
    md_table = parser.generate_markdown_for_component(reference=args.component_name)

    filename = args.component_name+"_pin_out.md"
    saver = FileSaver(filename)
    saver.save_markdown(md_table)


if __name__ == "__main__":
    main()