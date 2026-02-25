from dataclasses import dataclass

@dataclass
class Symbol:
    reference: str
    value: str | None
    properties: dict[str, str]