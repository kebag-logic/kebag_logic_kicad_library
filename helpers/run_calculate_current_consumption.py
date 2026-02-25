#!/usr/bin/env python3
import argparse
from core.kicad_project import KiCadProject
from core.kicad_schematic_parser import KiCadSchematicParser
from core.current_analyzer import CurrentAnalyzer
from core.file_saver import FileSaver

def main():
    parser = argparse.ArgumentParser(
        description="Calculate current consumption from KiCad schematics and save to a markdown file."
    )
    parser.add_argument(
        "root_sch",
        type=str,
        help="Path to the root KiCad schematic file (e.g., ../../shish-lan.kicad_sch)"
    )
    parser.add_argument(
        "output_md",
        nargs="?",  # optional positional argument
        default="current_consumption.md",
        type=str,
        help="Path to the output markdown file (default: current_consumption.md)"
    )
    args = parser.parse_args()

    # Extract sheets from root schematic
    project = KiCadProject(args.root_sch)
    all_sheets = project.collect_sheets()
    if not all_sheets:
        raise TypeError("Could not extract sheets.")

    # Collect all components with currents
    parser = KiCadSchematicParser()
    all_symbols = []

    for sheet in all_sheets:
        all_symbols.extend(parser.parse_file(sheet))
    if not all_symbols:
        raise TypeError("Could not extract symbols.")

    # Generate markdown table
    analyzer = CurrentAnalyzer()
    components = analyzer.extract_currents(all_symbols)
    components_per_rail = []
    for component in components:
        print(f"{component.reference}: {component.currents}")
        if "U" in component.reference:
            components_per_rail.append(component)
    if not components_per_rail:
        raise TypeError("Could not extract any components.")
    current_per_rail = analyzer.summarize_by_rail(components_per_rail)
    md_current_per_rail=analyzer.generate_markdown_table(current_per_rail)

    # Save to file
    file_saver = FileSaver(path_to_file=args.output_md)
    file_saver.save_markdown(md_current_per_rail)

if __name__ == "__main__":
    main()
