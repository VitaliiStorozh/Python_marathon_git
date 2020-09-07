# Write the function quadratic_equation with arguments a, b ,c that solution to quadratic equation
# without complex solution.
#
# Write unit tests for this function with QuadraticEquationTest class
#
# Minimum 3 tests: discriminant < 0, discriminant > 0, discriminant = 0

def quadratic_equation(a, b, c):
    discr = b ** 2 - 4 * a * c
    if a == 0:
        raise ValueError("error")
    elif discr > 0:
        import math
        x1 = round((-b + math.sqrt(discr)) / (2 * a), 2)
        x2 = round((-b - math.sqrt(discr)) / (2 * a), 2)
        return x1, x2
    elif discr == 0 and a != 0:
        x = -b / (2 * a)
        return x



import unittest


class QuadraticEquationTest(unittest.TestCase):
    def test_discriminant_less_zero(self):
        self.assertEqual(quadratic_equation(8,4,2), None)
    def test_discriminant_equal_zero(self):
        self.assertEqual(quadratic_equation(4,8,4), -1)
    def test_discriminant_more_zero(self):
        self.assertEqual(quadratic_equation(12,7,1), (-0.25, -0.33))
    def test_valid_arguments(self):
        self.assertRaises(Exception, quadratic_equation, 0,0,0)

# print(quadratic_equation(0,0,0))

quadraticTestSuite = unittest.TestSuite()
quadraticTestSuite.addTest(unittest.makeSuite(QuadraticEquationTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(quadraticTestSuite)