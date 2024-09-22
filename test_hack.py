import unittest
from parameterized import parameterized

from hack_assembler import hack

def compareBinaryOutputs(a, b):
    ar = a.split("\n")
    br = b.split("\n")

    success = True
    for al, bl in zip(ar,br):
        if al != bl:
            print(f"Diff found:\n{al}\n{bl}")
            success = False

    return success

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


        self.assertTrue(compareBinaryOutputs(res, expected))
