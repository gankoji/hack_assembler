"""Parser for the Hack Assembler."""

from .opcodes.opcode import opcode_dict

class CommandToken:
    def __init__(
            self,
            is_c:    bool,
            opcode:  int | None,
            dest:    str | int | None,
            jump:    str | None,
            label:   str | None = None
    ):
        self.is_c = is_c
        self.is_l = label is not None
        self.opcode = opcode
        self.dest = dest
        self.jump = jump
        self.label = label


    def __str__(self):
        return f'{self.is_c},{self.opcode},Dest:{self.dest},Jump:{self.jump},Label:{self.label},IsLabel:{self.is_l}'

class Parser():
    def remove_comments(self, line: str) -> str:
        comment_start = line.find("//")
        if comment_start == -1:
            return line
        elif comment_start == 0:
            return ""
        else:
            return line[0:comment_start]

    def lex_line(self, line: str) -> CommandToken:
        """Return a list of tokens from the given line of Hack assembly code.

            Args:
                line: The line of code to parse.

            Returns:
                A list of tokens extracted from the line. Format is (is_c, opcode, dest, jump)
        """

        # Preprocess the line
        line = self.remove_comments(line) # Get rid of comments
        line = line.lstrip() # Remove beginning whitespace
        line = line.rstrip() # And the end, too

        # Don't process if there's nothing left
        if len(line) == 0:
            return None

        if line[0] == "@":
            # We have an A instruction
            dest = None
            try:
                dest = int(line[1:])
            except ValueError:
                dest = line[1:]

            return CommandToken(False, -1, dest, None)
        elif line[0] == "(":
            # We have a label definition
            line = line.rstrip(")")
            line = line.lstrip("(")
            return CommandToken(False, -1, None, None, line)
        else:
            # We have some type of C instruction
            return self.lex_c_inst(line)

    def lex_c_inst(self, line: str) -> CommandToken:
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
        if len(ls) == 1:
            # dest is empty
            dest = None
            rest = 0
        else:
            dest = ls[0]
            rest = 1

        rs = ls[rest].split(";")
        if len(rs) == 1:
            # jump is empty
            jump = None
        else:
            jump = rs[1]

        c = rs[0]
        comp = self.find_opcode(c)

        return CommandToken(True, comp, dest, jump)

    def find_opcode(self, c: str) -> int:
        return opcode_dict[c]

    def parse_file(self, file: [str]) -> [CommandToken]:
        out = []
        for line in file:
            lexed = self.lex_line(line)
            if lexed:
                out.append(lexed)

        return out
if __name__ == "main":
    print("hello world")
