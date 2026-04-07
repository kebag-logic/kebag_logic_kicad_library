PASS = 0
FAIL = 1

symbol_name_parameters = {
    "symbol_type":
    {
        "R":
        {
            "Value": "str",
            "Power_in_W": "float",
            "Tolerance_in_pct": "float",
            "Package_in_inch": "str",
            "VALIDATION_RULES" : {
                "Reference": {"type": "equals", "value": "R"},
                "Footprint": {"type": "contains_package"},
                "Datasheet": {"type": "not_empty"},
                "Mouser": {"type": "not_empty"},
                "Digikey": {"type": "not_empty"},
                "LCSC": {"type": "not_empty"},
            },
        },
        "C":
        {
            "Value": "str",
            "Tolerance_in_pct": "float"
        }
    }
}