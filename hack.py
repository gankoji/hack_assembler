#!/usr/bin/env python3

"""Top level module for the Hack Assembler.

Hack is the assembly and machine language for the Hack CPU designed and
implemented in the Nand2Tetris course. See
https://drive.google.com/open?id=1CITliwTJzq19ibBF5EeuNBZ3MJ01dKoI&authuser=schocken%40gmail.com&usp=drive_fs
for details.
"""

from hack_assembler.modules.parser import Parser, CommandToken
from hack_assembler.modules.encoder import Encoder
from hack_assembler.modules.symbol_table import SymbolTable

class Hack():
    def __init__(self):
        self.parser = Parser()
        self.encoder = Encoder()
        self.st = SymbolTable()

    def assemble_file(self, filename: str) -> str:
        lines = []
        with open(filename,'r') as f:
            for line in f:
                lines.append(line)

        parsed = self.parser.parse_file(lines)

        # First pass
        for i,token_tuple in enumerate(parsed):
            if token_tuple.is_l:
                self.st.add_entry(token_tuple.dest, i+1)

        # Second pass
        for i,token_tuple in enumerate(parsed):
            if self.st.contains(token_tuple.dest):
                token_tuple.dest = self.st.get_address(token_tuple.dest)

            if token_tuple.is_c:
                inst = self.encoder.encode_c_inst(token_tuple)
            else:
                inst = self.encoder.encode_a_inst(token_tuple)

            if i == 0:
                output = inst
            else:
                output = output + "\n" + inst

        return output

if __name__ == "__main__":
    parser = Parser()
    print("Hello world!")
    print(parser.find_opcode("D|A"))
