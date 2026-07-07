# Module Symbol Properties

Modules are complete boards or sub-assemblies (host boards, SoMs, plug-on modules)
that appear as a single component in a schematic.

The naming scheme for all modules is as follows:
```
<Module Name>
```
For a module with the name `PocketBeagle2`, this would result in
```
PocketBeagle2
```

## Module footprint and package rules

- The symbol shows every header/interface pin of the module. Pin numbering must
  follow the module documentation (for header modules: P1.x = 1..36, P2.x = 37..72).
- Each symbol must have a footprint assigned that matches the mating header/land pattern.
- Links to documentation only from the module vendor. No supplier documentation.
- Only the Reference field and the Value field are visible by default.
- The reference designator prefix must remain `U` and must not be fixed in the symbol.

## Custom fields

- Field names are fixed and must not be changed.
---
- **MPN**: Manufacturer/vendor Part Number.
- **Mouser**: Order number of this component at Mouser.
- **Digikey**: Order number of this component at Digikey.
- **LCSC**: Order number of a component with exact same characteristics at LCSC (https://lcsc.com).

## Module, full example
| Name              | Value                                       | Show  | Show Name | H Align   | V Align   | Italic    | Bold  |
|-                  |-                                            |-      |-          |-          |-          |-          |-      |
| Reference         | U                                           | 1     | 0         | Center    | Center    | 0         | 0     |
| Value             | PocketBeagle2                               | 1     | 0         | Center    | Center    | 0         | 0     |
| Footprint         | KL_Footprints:BeagleBoard_PocketBeagle      | 0     | 0         | Center    | Center    | 0         | 0     |
| Datasheet         | https://docs.beagleboard.org/boards/pocketbeagle-2/ | 0 | 0    | Center    | Center    | 0         | 0     |
| Description       | BeagleBoard.org PocketBeagle 2 host board (AM62x) | 0 | 0      | Center    | Center    | 0         | 0     |
| MPN               | PocketBeagle 2                              | 0     | 0         | Center    | Center    | 0         | 0     |
| Mouser            | TBD                                         | 0     | 0         | Center    | Center    | 0         | 0     |
| Digikey           | TBD                                         | 0     | 0         | Center    | Center    | 0         | 0     |
| LCSC              | TBD                                         | 0     | 0         | Center    | Center    | 0         | 0     |
