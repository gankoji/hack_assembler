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
        print("First pass over input to generate symbol table")
        for i,token_tuple in enumerate(parsed):
            if token_tuple.is_l:
                self.st.add_entry(token_tuple.label, i+1)

        print("Symbol table generated.")
        free_addr = 16 # Could be dynamic, this is just after the last of our predefined symbols in RAM

        # Second pass
        print("Second pass over input to generate machine code with addresses")
        for i,token_tuple in enumerate(parsed):
            if self.st.contains(token_tuple.dest):
                token_tuple.dest = self.st.get_address(token_tuple.dest)

            if token_tuple.is_c:
                # Standard path, generate an instruction
                inst = self.encoder.encode_c_inst(token_tuple)
            elif token_tuple.is_l:
                # We have a label instruction, don't generate any code
                continue
            else:
                # We have an A instruction
                # First, check if we're declaring a variable
                if isinstance(token_tuple.dest, str):
                    # Put it in the symbol table too
                    self.st.add_entry(token_tuple.dest, free_addr)
                    # Replace it in the instruction...
                    token_tuple.dest = free_addr
                    # and increment our pointer
                    free_addr += 1

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
