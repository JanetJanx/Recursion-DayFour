import unittest

from power_recursion import power_recursion

class TestPower(unittest.TestCase):
    """The tests below compare the result of the user built power function 
    power_recursion() with the results of the inbuilt power function pow()"""

    def test_power_recursion(self):
        self.assertEqual(power_recursion(3,4), pow(3,4))

    def test_power_recursion_only_integers(self):
        self.assertEqual(power_recursion('s',4), "Please use intergers")
    
    def test_power_recursion_with_negative_power(self):
        self.assertEqual(power_recursion(3,-4), pow(3,-4))

    def test_power_recursion_with_base_zero(self):
        self.assertEqual(power_recursion(0,4), pow(0,4))
    
    def test_power_recursion_with_power_zero(self):
        self.assertEqual(power_recursion(5,0), pow(5,0))

    def test_power_recursion_with_base_one(self):
        self.assertEqual(power_recursion(1,4), pow(1,4))
    
    def test_power_recursion_with_power_one(self):
        self.assertEqual(power_recursion(5,1), pow(5,1))

if __name__ == "__main__":
    unittest.main()