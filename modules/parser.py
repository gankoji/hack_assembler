"""Parser for the Hack Assembler."""

from .opcodes.opcode import opcode_dict

class CommandToken:
    def __init__(self, is_c: bool, opcode: int, dest: str, jump: str):
        self.is_c: bool = is_c
        self.opcode: int = opcode
        self.dest: str = dest
        self.jump: str = jump

def lex_line(line: str) -> CommandToken:
    """Return a list of tokens from the given line of Hack assembly code.

        Args:
            line: The line of code to parse.

        Returns:
            A list of tokens extracted from the line. Format is (is_c, opcode, dest, jump)
    """
    line = line.lstrip() # Remove beginning whitespace
    line = line.rstrip() # And the end, too
    if line[0] == "@":
        # We have an A instruction
        return CommandToken(False, -1, int(line[1:]),_)
    elif line[0] == "(":
        # We have a label definition
        line = line.rstrip(")")
        line = line.lstrip("(")
        return CommandToken(False, -1, line, _)
    else:
        # We have some type of C instruction
        return lex_c_inst(line)

def lex_c_inst(line: str) -> CommandToken:
    """Tokenify a C instruction. C instruction format is
       dest=comp;jump. Either dest or jump can be empty. If dest is empty,
       the '=' is omitted. If jump is empty, ';' is omitted.

        Args:
            line: The line of code to parse.

        Returns:
            A CommandToken containing the fields of the command.
    """
    # First, we split on the two separators to see what we have
    ls = line.split("=")
    if ls[0] == "":
        # dest is empty
        dest = ""
    else:
        dest = ls[0]
    rs = ls.split(";")
    if rs[1] == "":
        # jump is empty
        jump = None
    else:
        jump = rs[1]

    c = rs[0]
    comp = find_opcode(c)

    return CommandToken(True, comp, dest, jump)

def find_opcode(c: str) -> int:
    return opcode_dict[c]

if __name__ == "main":
    print("hello world")
