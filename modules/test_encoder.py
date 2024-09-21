import unittest
from parameterized import parameterized

from hack_assembler.modules.encoder import Encoder
from hack_assembler.modules.parser import CommandToken

class TestEncoder(unittest.TestCase):
    def setUp(self):
        self.encoder = Encoder()

    def test_a_inst(self):
        expected = "0000000000010001"
        res = self.encoder.encode_a_inst(CommandToken(False,-1,"17",None))

        self.assertEqual(res, expected)

    def test_c_inst(self):
        expected = "1110101010011101"
        res = self.encoder.encode_c_inst(CommandToken(True,0b0101010,"MD","JNE"))

        self.assertEqual(res, expected)
