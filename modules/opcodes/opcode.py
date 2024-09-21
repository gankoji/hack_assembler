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
