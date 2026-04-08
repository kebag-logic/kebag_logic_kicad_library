import copy

def make_validation_rules(reference):
    rules = copy.deepcopy(VALIDATION_RULES_GENERAL)
    rules["Reference"]["value"] = reference
    return rules

PASS = 0
FAIL = 1

VALIDATION_RULES_GENERAL = {
    "Reference": {"type": "equals", "value": "R"},
    "Footprint": {"type": "contains_package"},
    "Datasheet": {"type": "not_empty"},
    "Mouser": {"type": "not_empty"},
    "Digikey": {"type": "not_empty"},
    "LCSC": {"type": "not_empty"},
}

symbol_name_parameters = {
    "symbol_type":
    {
        "R":
        {
            "Value": "str",
            "Power_in_W": "float",
            "Tolerance_in_pct": "float",
            "Package_in_inch": "str",
            "VALIDATION_RULES" : make_validation_rules("R")
        },
        "C":
        {
            "Value": "str",
            "Voltage_in_V": "float",
            "Tolerance_in_pct": "float",
            "Dielectric": "str",
            "Package_in_inch": "str",
            "VALIDATION_RULES" : make_validation_rules("C")
        }
    }
}