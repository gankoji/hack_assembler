"""Instruction encoder for the Hack assembly language.

Takes as input a list of instruction tokens and returns a list of
encoded instructions.
"""

from hack_assembler.modules.parser import CommandToken
from hack_assembler.modules.opcodes.opcode import dest_dict, jump_dict

class Encoder():

    def encode_a_inst(self, tokens: CommandToken) -> str:
        bits = ["0"]
        dest_addr = int(tokens.dest)
        bin_str = f'{dest_addr:>015b}'
        bits.append(bin_str)
        return "".join(bits)

    def encode_c_inst(self, tokens: CommandToken) -> str:

        # Check for None
        dest = dest_dict[tokens.dest] if tokens.dest else 0
        jump = jump_dict[tokens.jump] if tokens.jump else 0

        # Convert to bit strings
        instr = f"111{tokens.opcode:>07b}{dest:>03b}{jump:>03b}"
        return instr



if __name__ == "__main__":
    enc = Encoder()
    out = enc.encode_a_inst(CommandToken(False,-1,"17",None))
    print(out)

    out = enc.encode_c_inst(CommandToken(True,0b0101010,"MD","JNE"))
    print(out)
