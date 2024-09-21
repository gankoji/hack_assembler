"""Utility module for the Hack ISA.

Translates input strings to numeric opcode outputs that correspond to the
machine instruction, i.e. (a c1 c2 c3 c4 c5 c6)

"""

#    comp                          comp
# (when a==0) c1 c2 c3 c4 c5 c6 (when a==1)
#     0        1  0  1  0  1  0      _
#     1        1  1  1  1  1  1      _
#    -1        1  1  1  0  1  0      _
#     D        0  0  1  1  0  0      _
#     A        1  1  0  0  0  0      M
#    !D        0  0  1  1  0  1
#    !A        1  1  0  0  0  1      !M
#    -D        0  0  1  1  1  1
#    -A        1  1  0  0  1  1      -M
#    D+1       0  1  1  1  1  1
#    A+1       1  1  0  1  1  1      M+1
#    D-1       0  0  1  1  1  0
#    A-1       1  1  0  0  1  0      M-1
#    D+A       0  0  0  0  1  0      D+M
#    D-A       0  1  0  0  1  1      D-M
#    A-D       0  0  0  1  1  1      M-D
#    D&A       0  0  0  0  0  0      D&M
#    D|A       0  1  0  1  0  1      D|M

opcode_dict = {}

opcode_dict[ "0"] = 0b0101010
opcode_dict[ "1"] = 0b0111111
opcode_dict["-1"] = 0b0111010

opcode_dict["D"] = 0b0001100
opcode_dict["A"] = 0b0110000
opcode_dict["M"] = 0b1110000

opcode_dict["!D"] = 0b0001101
opcode_dict["!A"] = 0b0110001
opcode_dict["!M"] = 0b1110001

opcode_dict["-D"] = 0b0001111
opcode_dict["-A"] = 0b0110011
opcode_dict["-M"] = 0b1110011

opcode_dict["D+1"] = 0b0011111
opcode_dict["A+1"] = 0b0110111
opcode_dict["M+1"] = 0b1110111

opcode_dict["D-1"] = 0b0001110
opcode_dict["A-1"] = 0b0110010
opcode_dict["M-1"] = 0b1110010

opcode_dict["D+A"] = 0b0000010
opcode_dict["D+M"] = 0b1000010

opcode_dict["D-A"] = 0b0010011
opcode_dict["D-M"] = 0b1010011

opcode_dict["A-D"] = 0b0000111
opcode_dict["M-D"] = 0b1000111

opcode_dict["D&A"] = 0b0000000
opcode_dict["D&M"] = 0b1000000

opcode_dict["D|A"] = 0b0010101
opcode_dict["D|M"] = 0b1010101


# Dest Table
# dest d1 d2 d3 jump j1 j2 j3
# null 0  0  0  null  0  0  0
# M    0  0  1  JGT   0  0  1
# D    0  1  0  JEQ   0  1  0
# MD   0  1  1  JGE   0  1  1
# A    1  0  0  JLT   1  0  0
# AM   1  0  1  JNE   1  0  1
# AD   1  1  0  JLE   1  1  0
# AMD  1  1  1  JMP   1  1  1

jump_dict = {}
jump_dict["JGT"] = 0b001
jump_dict["JEQ"] = 0b010
jump_dict["JGE"] = 0b011
jump_dict["JLT"] = 0b100
jump_dict["JNE"] = 0b101
jump_dict["JLE"] = 0b110
jump_dict["JMP"] = 0b111

dest_dict = {}
dest_dict[  "M"] = 0b001
dest_dict[  "D"] = 0b010
dest_dict[ "MD"] = 0b011
dest_dict[  "A"] = 0b100
dest_dict[ "AM"] = 0b101
dest_dict[ "AD"] = 0b110
dest_dict["AMD"] = 0b111
