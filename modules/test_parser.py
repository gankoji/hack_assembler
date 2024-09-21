"""Unit tests for the Hack parser methods"""
import parser

class TestParser:
    def test_find_opcode(self):
        code = parser.find_opcode("0")
        assert code == 0b101010

if __name__ == "main":
    print("Hello World")
    t = TestParser()
    t.test_find_opcode()
