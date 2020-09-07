# You have function divide
#
# Please, write the code with unit tests for the function "divide":
# minimum 3 tests
# must chek all flows
# all test must be pass
# no failures
# no skip

import unittest


def divide(num1, num2):
    return float(num1)/num2


class DivideTest(unittest.TestCase):
    def test_positive_divide(self):
        self.assertEqual(divide(10,2), 5)

    def test_positive2_divide(self):
        self.assertEqual(divide(2, 10), 0.2)

    def test_negative_divide(self):
        self.assertEqual(divide(-12, 2), -6)

    def test_almost_positive_divide(self):
        self.assertAlmostEqual(divide(1, 3), 0.333333, 6)

    def test_zero_divide(self):
        self.assertRaises(Exception, divide, 5, 0)

divideTestSuite = unittest.TestSuite()
divideTestSuite.addTest(unittest.makeSuite(DivideTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(divideTestSuite)