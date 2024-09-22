import unittest
from parameterized import parameterized

from hack_assembler import hack

class testHack(unittest.TestCase):
    def setUp(self):
        self.hack = hack.Hack()

    def test_no_symbols(self):
        # Arrange
        expected = """0000000000001010
1110110000001000
1110110000010000
1110101010010000
0000000000000001
1110001100001000
0000000000000001
1111110111001000
1111110000010000
0000000000001010
1111000111010000
0000000000000010
1110101010000010"""

        # Act
        res = self.hack.assemble_file("assembler_test_no_symbols.asm")

        # Assert
        print(res)
        self.assertEqual(len(res), len(expected))

    @parameterized.expand([
        (  "tests/add.asm",  "tests/add.hack"),
        ( "tests/maxL.asm", "tests/maxL.hack"),
        ("tests/pongL.asm","tests/pongL.hack"),
        ("tests/rectL.asm","tests/rectL.hack"),
    ])
    def test_golden_inputs(self, input_file, expected_file):
        expected = ""
        with open(expected_file, 'r') as f:
            expected = f.read()

        res = self.hack.assemble_file(input_file)
        if res != expected:
            print(f"Failed to match for input {input_file}.")
            print(res)
            print("\n" + expected)

        self.assertEqual(res, expected)
