#!/usr/bin/env python3

"""Top level module for the Hack Assembler.

Hack is the assembly and machine language for the Hack CPU designed and
implemented in the Nand2Tetris course. See
https://drive.google.com/open?id=1CITliwTJzq19ibBF5EeuNBZ3MJ01dKoI&authuser=schocken%40gmail.com&usp=drive_fs
for details.
"""

from modules import parser

if __name__ == "__main__":
    print("Hello world!")
    print(parser.find_opcode("D|A"))
