import unittest

from power_recursion import power_recursion

class TestPower(unittest.TestCase):

    def test_power_recursion(self):
        self.assertEquals(power_recursion(3,4), 81)

    def test_power_recursion_only_integers(self):
        self.assertEquals(power_recursion('s',4), "Please use intergers")
    
    def test_power_recursion_only_positive_power(self):
        self.assertEquals(power_recursion(3,-4), "The number to be powered shouldnot be negative")

if __name__ == "__main__":
    unittest.main()