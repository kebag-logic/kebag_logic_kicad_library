import re
from .symbol_name_parameters import symbol_name_parameters, PASS, FAIL


class SymbolValidator:

    def __init__(self, symbol_type):
        self.symbol_type = symbol_type

        type_config = symbol_name_parameters['symbol_type'][symbol_type]

        self.expected_params = {
            k: v for k, v in type_config.items() if k != "VALIDATION_RULES"
        }

        self.validation_rules = type_config.get("VALIDATION_RULES", {})

    def validate(self, properties, reference_entry):
        results = {}

        for name, prop_dict in properties.items():
            if reference_entry[0] in name:
                continue

            val1 = self.parse_symbol_name(name)
            val2 = prop_dict

            results.setdefault(name, {})

            # --- 1. Compare name-derived parameters ---
            for param, cast_type in self.expected_params.items():
                # print(f"param: {param}")
                v1 = val1[param]
                v2 = val2.get(param)

                if cast_type == "float":
                    v1 = float(v1)
                    v2 = float(v2)
                elif cast_type == "str":
                    v1 = str(v1)
                    v2 = str(v2)

                verdict = PASS if v1 == v2 else FAIL

                results[name][param] = {
                    "verdict": verdict,
                    "expected": v1,
                    "actual": v2
                }

            # --- 2. Additional property validation ---
            for field, rule in self.validation_rules.items():
                # print(f"field: {field}, rule: {rule}")
                value = val2.get(field, "")

                verdict = PASS
                expected = None

                if rule["type"] == "equals":
                    expected = rule["value"]
                    if value != expected:
                        verdict = FAIL

                elif rule["type"] == "not_empty":
                    expected = "non-empty"
                    if not value or str(value).strip() in ["", "~"]:
                        verdict = FAIL

                elif rule["type"] == "contains_package":
                    try:
                        expected = val1["Package_in_inch"]
                    except KeyError:
                        expected = val1["Package_LxW_in_mm"]
                    if expected not in str(value):
                        verdict = FAIL

                results[name][field] = {
                    "verdict": verdict,
                    "expected": expected,
                    "actual": value
                }

        # --- reporting (ONLY FAILURES) ---
        print("\n=== VALIDATION RESULTS ===")

        for name, params in results.items():
            failures = {k: v for k, v in params.items() if v["verdict"] == FAIL}

            if not failures:
                continue

            print(f"\n❌ {name}")
            for param, data in failures.items():
                print(f"   {param}: expected {data['expected']} | actual {data['actual']}")

        total = len(results)
        failed = sum(1 for p in results.values() if any(v["verdict"] == FAIL for v in p.values()))

        print("\n=== SUMMARY ===")
        print(f"Total symbols checked: {total}")
        print(f"Symbols with errors: {failed}")
        print(f"Symbols OK: {total - failed}")

        return results

    def parse_symbol_name(self, symbol_name):
        param_names = list(self.expected_params.keys())

        if not symbol_name.startswith(self.symbol_type + "_"):
            raise ValueError(f"{symbol_name} does not match symbol type {self.symbol_type}")

        parts = symbol_name[len(self.symbol_type) + 1:].split("_")

        result = {}

        for name, val in zip(param_names, parts):
            expected_type = self.expected_params[name]

            if expected_type == "float":
                val = float(re.sub(r"[^\d.]+", "", val))
            elif expected_type == "int":
                val = int(val)
            else:
                val = str(val)

            result[name] = val

        return result
