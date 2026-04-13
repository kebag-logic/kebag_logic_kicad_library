from dataclasses import dataclass
from decimal import Decimal

@dataclass
class CurrentComponent:
    reference: str
    value: str
    currents: dict[str, Decimal]