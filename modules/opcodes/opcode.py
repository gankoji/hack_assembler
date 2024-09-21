"""Utility module for the Hack ISA. Translates input strings to numeric opcode
outputs."""

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

opcode_dict[ "0"] = 0b101010
opcode_dict[ "1"] = 0b111111
opcode_dict["-1"] = 0b111010

opcode_dict["D"] = 0b001100
opcode_dict["A"] = 0b110000
opcode_dict["M"] = 0b110000

opcode_dict["!D"] = 0b001101
opcode_dict["!A"] = 0b110001
opcode_dict["!M"] = 0b110001

opcode_dict["-D"] = 0b001111
opcode_dict["-A"] = 0b110011
opcode_dict["-M"] = 0b110011

opcode_dict["D+1"] = 0b011111
opcode_dict["A+1"] = 0b110111
opcode_dict["M+1"] = 0b110111

opcode_dict["D-1"] = 0b001110
opcode_dict["A-1"] = 0b110010
opcode_dict["M-1"] = 0b110010

opcode_dict["D+A"] = 0b000010
opcode_dict["D+M"] = 0b000010

opcode_dict["D-A"] = 0b010011
opcode_dict["D-M"] = 0b010011

opcode_dict["A-D"] = 0b000111
opcode_dict["M-D"] = 0b000111

opcode_dict["D&A"] = 0b000000
opcode_dict["D&M"] = 0b000000

opcode_dict["D|A"] = 0b010101
opcode_dict["D|M"] = 0b010101
