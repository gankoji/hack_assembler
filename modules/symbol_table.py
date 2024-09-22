"""Module for handling symbols/labels in Hack

Label | RAM address | (hexa)
    SP             0  0x0000
   LCL             1  0x0001
   ARG             2  0x0002
  THIS             3  0x0003
  THAT             4  0x0004
R0-R15          0-15  0x0000-f
SCREEN         16384  0x4000
   KBD         24576  0x6000
"""

class SymbolTable():
    """Stores and manipulates the symbol table for a Hack assembly program."""

    def __init__(self):
        # Initialize the symbol table with the predefined labels
        self.symbol_table = {
            "    SP":     0,
            "   LCL":     1,
            "   ARG":     2,
            "  THIS":     3,
            "  THAT":     4,
            "    R0":     0,
            "    R1":     1,
            "    R2":     2,
            "    R3":     3,
            "    R4":     4,
            "    R5":     5,
            "    R6":     6,
            "    R7":     7,
            "    R8":     8,
            "    R9":     9,
            "   R10":    10,
            "   R11":    11,
            "   R12":    12,
            "   R13":    13,
            "   R14":    14,
            "   R15":    15,
            "SCREEN": 16384,
            "   KBD": 24576,
        }

    def add_entry(self, label: str, addr: int):
        if self.contains(label):
            print(f"Error, label {label} already exists.")
            return

        self.symbol_table[label] = addr

    def contains(self, label):
        return (label in self.symbol_table.keys())

    def get_address(self, label):
        if not self.contains(label):
            print(f"Error, symbol {label} not in table.")

        return self.symbol_table[label]
