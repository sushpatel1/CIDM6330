from numToroman import NumeralsToRoman
import unittest

class NumToRomanTest(unittest.TestCase):
   def test_working(self):
       pass


   def NumToRomanTest(self):
       numeral1 = NumeralsToRoman(105)
       Expected_Val1 = "CV"
       Actual_val1 = numeral1.NumToRoman()

       numeral2 = NumeralsToRoman(0)
       Expected_Val2 = "not a valid Number"
       Actual_val2 = numeral2.NumToRoman()
       
       self.assertEqual(Expected_Val1, Actual_val1)
       self.assertNotEqual(Expected_Val2, Actual_val1)