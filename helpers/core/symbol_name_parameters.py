import copy

def make_validation_rules(reference, remove=None):
    rules = copy.deepcopy(VALIDATION_RULES_GENERAL)
    rules["Reference"]["value"] = reference
    if remove:
        for parameter in remove:
            del rules[parameter]

    return rules

PASS = 0
FAIL = 1

VALIDATION_RULES_GENERAL = {
    "Reference": {"type": "equals", "value": "R"},
    "Footprint": {"type": "contains_package"},
    "Datasheet": {"type": "not_empty"},
    "MPN": {"type": "not_empty"},
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
        },
        "L":
        {
            "Value": "str",
            "I_max_in_A": "float",
            "Tolerance_in_pct": "float",
            "Package_LxW_in_mm": "str",
            "VALIDATION_RULES" : make_validation_rules("L", remove=["Footprint"])
        },
        "Crystal":
        {
            "Value": "str",
            "Frequency_Tolerance_in_ppm": "float",
            "Load_Capacitance_in_pF": "float",
            "Package_LxW_in_mm": "str",
            "VALIDATION_RULES" : make_validation_rules("X", remove=["Footprint"])
        },
        "VoltageRegulator":
        {
            "USE_NAME_PARSING": False,
            "Value": "str",
            "VIN_MIN_V": "float",
            "VIN_MAX_V": "float",
            "I_OUT_A": "float",
            "I_VIN_A": "float",
            "VALIDATION_RULES" : make_validation_rules("U", remove=["Footprint"])
        },
        "MCU":
        {
            "USE_NAME_PARSING": False,
            "Value": "str",
            "V_DD_MAX_V": "float",
            "I_DD_MAX_A": "float",
            "VALIDATION_RULES" : make_validation_rules("U", remove=["Footprint"])
        }
    }
}