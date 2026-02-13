#!/usr/bin/env python3
import argparse
from calculate_current_consumption import (
    extract_sheets,
    collect_all_components,
    generate_markdown_table,
    save_markdown_to_file
)

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
    all_sheets = extract_sheets(args.root_sch)

    # Collect all components with currents
    all_components = collect_all_components(all_sheets)

    # Generate markdown table
    md_table = generate_markdown_table(all_components)

    # Save to file
    save_markdown_to_file(md_text=md_table, file_path=args.output_md)
    print(f"Markdown table saved to {args.output_md}")

if __name__ == "__main__":
    main()
