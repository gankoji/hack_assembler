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
        self.symbol_table = {}
