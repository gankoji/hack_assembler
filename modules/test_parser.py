"""Unit tests for the Hack parser methods"""
import unittest
from parameterized import parameterized

from .parser import Parser, CommandToken

def compareTokens(a: CommandToken, b: CommandToken):
    if a.is_c != b.is_c:
        print("Different is_c.")
        return False
    if a.opcode != b.opcode:
        print("Different opcode.")
        return False
    if a.dest != b.dest:
        print("Different destination.")
        return False
    if a.jump != b.jump:
        print("Different jump.")
        return False
    return True

class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_find_opcode(self):
        # Arrange/Act
        code = self.parser.find_opcode("0")

        # Assert
        assert code == 0b0101010

    def test_lex_c_inst(self):
        # Arrange
        expected = CommandToken(True,0b0010101,"M","JNE")

        # Act
        res = self.parser.lex_c_inst("M=D|A;JNE")

        # Assert
        self.assertTrue(compareTokens(res,expected))

    # Arrange
    @parameterized.expand([
        (          "@17", CommandToken(False,        -1,   17, None,   None)),
        (       "(LOOP)", CommandToken(False,        -1, None, None, "LOOP")),
        ("    M=D|A;JNE", CommandToken( True, 0b0010101,  "M","JNE",   None)),
        (        "0;JMP", CommandToken( True, 0b0101010, None,"JMP",   None))
    ])
    def test_lex_line(self, line, expected):
        # Act
        res = self.parser.lex_line(line)

        # Assert
        if not compareTokens(res,expected):
            print("Compare tokens failed. res vs expected:")
            print(res)
            print(expected)
        self.assertTrue(compareTokens(res,expected))

    def test_parse_file(self):
        # Arrange
        expected = [
            CommandToken(False,       -1,     17, None,   None), # @17
            CommandToken( True,0b0110000,    "M", None,   None), # M=A
            CommandToken(False,       -1,   None, None, "LOOP"), # (LOOP)
            CommandToken( True,0b1110000,    "D", None,   None), # D=M
            CommandToken( True,0b0011111,   None, None,   None), # D+1
            CommandToken( True,0b0001100,    "M", None,   None), # M=D
            CommandToken(False,       -1, "LOOP", None,   None), # @LOOP
            CommandToken( True,0b0101010,   None,"JMP",   None), # 0;JMP
        ]


        # Act
        lines = []
        with open('modules/parser_test_file.txt','r') as f:
            for line in f:
                lines.append(line)

        res = self.parser.parse_file(lines)

        # Assert
        self.assertEqual(len(res), len(expected))
        for r,l in zip(res, expected):
            if not compareTokens(r,l):
                print(r)
                print(l)
            self.assertTrue(compareTokens(r,l))



if __name__ == "main":
    print("Hello World")
    t = TestParser()
    t.test_find_opcode()
