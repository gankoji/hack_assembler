import unittest
from parameterized import parameterized

from hack_assembler.modules.symbol_table import SymbolTable

class testSymbolTable(unittest.TestCase):
    def setUp(self):
        self.st = SymbolTable()

    def testPredefinedLabels(self):
        self.assertEqual(self.st.get_address(    "SP"),     0)
        self.assertEqual(self.st.get_address(   "LCL"),     1)
        self.assertEqual(self.st.get_address(   "ARG"),     2)
        self.assertEqual(self.st.get_address(  "THIS"),     3)
        self.assertEqual(self.st.get_address(  "THAT"),     4)

        self.assertEqual(self.st.get_address(    "R0"),     0)
        self.assertEqual(self.st.get_address(    "R1"),     1)
        self.assertEqual(self.st.get_address(    "R2"),     2)
        self.assertEqual(self.st.get_address(    "R3"),     3)
        self.assertEqual(self.st.get_address(    "R4"),     4)
        self.assertEqual(self.st.get_address(    "R5"),     5)
        self.assertEqual(self.st.get_address(    "R6"),     6)
        self.assertEqual(self.st.get_address(    "R7"),     7)
        self.assertEqual(self.st.get_address(    "R8"),     8)
        self.assertEqual(self.st.get_address(    "R9"),     9)
        self.assertEqual(self.st.get_address(   "R10"),    10)
        self.assertEqual(self.st.get_address(   "R11"),    11)
        self.assertEqual(self.st.get_address(   "R12"),    12)
        self.assertEqual(self.st.get_address(   "R13"),    13)
        self.assertEqual(self.st.get_address(   "R14"),    14)
        self.assertEqual(self.st.get_address(   "R15"),    15)

        self.assertEqual(self.st.get_address("SCREEN"), 16384)
        self.assertEqual(self.st.get_address(   "KBD"), 24576)

    def testContains(self):
        self.assertTrue(self.st.contains("SCREEN"))

    def testAddEntry(self):
        self.st.add_entry("LOOP", 16)
        self.assertTrue(self.st.contains("LOOP"))

    def testGetAddress(self):
        self.st.add_entry("LOOP", 16)
        self.assertEqual(self.st.get_address("LOOP"), 16)
