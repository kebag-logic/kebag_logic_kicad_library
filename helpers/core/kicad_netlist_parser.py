import sexpdata
from pathlib import Path
from .base import KiCadBase


class KiCadNetlistParser(KiCadBase):

    def __init__(self, netlist_file: str):
        self.netlist_file = Path(netlist_file).resolve()
        self.sexp = self.load_file(self.netlist_file)

    def extract_nets(self):
        nets = {}

        def recurse(node):
            if not isinstance(node, list):
                return

            if node and str(node[0]) == "net":
                net_name = None
                connections = []

                for item in node[1:]:
                    if not isinstance(item, list):
                        continue

                    head = str(item[0])

                    if head == "name":
                        net_name = str(item[1])

                    elif head == "node":
                        ref = None
                        pin = None

                        for sub in item[1:]:
                            if not isinstance(sub, list):
                                continue

                            if str(sub[0]) == "ref":
                                ref = str(sub[1])
                            elif str(sub[0]) == "pin":
                                pin = str(sub[1])

                        if ref and pin:
                            connections.append((ref, pin))

                if net_name:
                    nets[net_name] = connections

            else:
                for child in node:
                    recurse(child)

        recurse(self.sexp)
        return nets

    def _filter_nets_by_prefix(self, prefix: str):
        nets = self.extract_nets()
        filtered = {}

        for net_name, nodes in nets.items():
            relevant = [n for n in nodes if n[0].startswith(prefix)]

            if relevant:
                filtered[net_name] = relevant

        return filtered

    def _build_pin_to_net_map(self, prefix: str) -> dict[str, str]:
        nets = self._filter_nets_by_prefix(prefix)
        pin_map = {}

        for net_name, nodes in nets.items():
            for ref, pin in nodes:
                pin_map[pin] = net_name

        return pin_map

    def _get_component_info(self, reference: str) -> dict:
        """
        Extract component metadata (ref + value) from netlist.
        """
        component_info = {}

        def recurse(node):
            if not isinstance(node, list):
                return

            # Look for (comp ...)
            if node and str(node[0]) == "comp":
                ref = None
                value = None

                for item in node[1:]:
                    if not isinstance(item, list):
                        continue

                    head = str(item[0])

                    if head == "ref":
                        ref = str(item[1])
                    elif head == "value":
                        value = str(item[1])

                if ref == reference:
                    component_info["ref"] = ref
                    component_info["value"] = value
                    return

            else:
                for child in node:
                    recurse(child)

        recurse(self.sexp)
        return component_info

    def _get_libsource_for_component(self, reference: str):
        lib_name = None
        part_name = None

        def recurse(node):
            nonlocal lib_name, part_name

            if not isinstance(node, list):
                return

            if node and str(node[0]) == "comp":
                ref = None
                for item in node[1:]:
                    if isinstance(item, list) and str(item[0]) == "ref":
                        ref = str(item[1])

                if ref == reference:
                    for item in node[1:]:
                        if isinstance(item, list) and str(item[0]) == "libsource":
                            for sub in item[1:]:
                                if isinstance(sub, list):
                                    if str(sub[0]) == "lib":
                                        lib_name = str(sub[1])
                                    elif str(sub[0]) == "part":
                                        part_name = str(sub[1])
                    return

            for child in node:
                recurse(child)

        recurse(self.sexp)
        return lib_name, part_name

    def _get_pin_names_from_libpart(self, lib_name: str, part_name: str):
        pin_map = {}

        def recurse(node):
            if not isinstance(node, list):
                return

            if node and str(node[0]) == "libpart":
                current_lib = None
                current_part = None
                pins_section = None

                for item in node[1:]:
                    if isinstance(item, list):
                        if str(item[0]) == "lib":
                            current_lib = str(item[1])
                        elif str(item[0]) == "part":
                            current_part = str(item[1])
                        elif str(item[0]) == "pins":
                            pins_section = item

                if current_lib == lib_name and current_part == part_name:
                    if pins_section:
                        for pin in pins_section[1:]:
                            if isinstance(pin, list) and str(pin[0]) == "pin":
                                num = None
                                name = None

                                for sub in pin[1:]:
                                    if isinstance(sub, list):
                                        if str(sub[0]) == "num":
                                            num = str(sub[1])
                                        elif str(sub[0]) == "name":
                                            name = str(sub[1])

                                if num:
                                    pin_map[num] = name if name else ""

                    return

            for child in node:
                recurse(child)

        recurse(self.sexp)
        return pin_map

    def generate_markdown_for_component(self, reference: str) -> str:
        component = self._get_component_info(reference)

        if not component:
            raise ValueError(f"Component {reference} not found in netlist.")

        pin_to_net = self._build_pin_to_net_map(reference)

        lib_name, part_name = self._get_libsource_for_component(reference)
        pin_names = {}

        if lib_name and part_name:
            pin_names = self._get_pin_names_from_libpart(lib_name, part_name)

        def pin_sort_key(p):
            """
            Sort pins: numeric pins first, then alphanumeric pins (e.g., EPAD).
            """
            if p.isdigit():
                # numeric pins
                return (0, int(p))
            # non-numeric pins
            return (1, p)

        def clean_net_name(net_name: str) -> str:
            # Replace unnamed and not connected nets with nice names
            if net_name.startswith("Net-(") and "{" in net_name:
                return "<unnamed>"
            elif net_name.startswith("unconnected-("):
                return "n.c."
            return net_name

        sorted_pins = sorted(pin_to_net.keys(), key=pin_sort_key)

        lines = []
        lines.append(f"# {component['ref']}: {component.get('value', '')}")
        lines.append("")
        lines.append("| Pin No | Pin Name | Connected to net |")
        lines.append("| - | - | - |")

        for pin in sorted_pins:
            pin_name = pin_names.get(pin, "")
            net = clean_net_name(pin_to_net[pin])
            lines.append(f"| {pin} | {pin_name} | {net} |")

        md_table = "\n".join(lines)

        return md_table, component
