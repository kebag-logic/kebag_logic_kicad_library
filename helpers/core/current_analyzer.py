from decimal import Decimal
from .symbol import Symbol
from .components import CurrentComponent

class CurrentAnalyzer:
    def __init__(self, field_prefix="I_"):
        self.field_prefix = field_prefix

    def extract_currents(self, symbols: list[Symbol]) -> list[CurrentComponent]:

        components: dict[str, CurrentComponent] = {}

        for sym in symbols:
            currents = {
                k: Decimal(v)
                for k, v in sym.properties.items()
                if k.startswith(self.field_prefix)
            }

            if not currents:
                continue

            if sym.reference not in components:
                components[sym.reference] = CurrentComponent(
                    reference=sym.reference,
                    value=sym.value,
                    currents={}
                )

            components[sym.reference].currents.update(currents)

        return list(components.values())

    def summarize_by_rail(
        self, components: list[CurrentComponent]
    ) -> dict[str, Decimal]:

        totals: dict[str, Decimal] = {}

        for comp in components:
            for rail, current in comp.currents.items():
                totals.setdefault(rail, Decimal(0))
                totals[rail] += current

        return totals

    def generate_markdown_table(self, current_per_rail: dict[str, Decimal], md_table = None) -> str:
        if not md_table:
            md_table = "| Rail | Current in A |\n|-|-|\n"
        for rail in sorted(current_per_rail):
            value = current_per_rail[rail]
            md_table += f"| {rail} | {value} |\n"
        return md_table