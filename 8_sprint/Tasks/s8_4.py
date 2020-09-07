 # Create class Triangle with method get_area() that calculate area of triangle. As input you will have list of 3 sides size.
# Example:
# triangle = Triangle([3, 3, 3])
#
# Use classes TriangleNotValidArgumentException and TriangleNotExistException
#
# Create class TriangleTest with parametrized unittest for class Triangle


import unittest


class TriangleNotValidArgumentException(Exception):
    pass


class TriangleNotExistException(Exception):
    pass


class Triangle:

    def __init__(self, data):
        try:
            if not self.data_valid(data):
                raise TriangleNotValidArgumentException("TriangleNotValidArgumentException")
            elif max(data) >= sum(data) - max(data):
                raise TriangleNotExistException("TriangleNotExistException")
            elif max(data) < sum(data) - max(data):
                self.side_a = data[0]
                self.side_b = data[1]
                self.side_c = data[2]
        except TriangleNotExistException as e:
            print(e)
        except TriangleNotValidArgumentException as e:
            print(e)

    def data_valid(self, data):
        try:
            if len(data) != 3:
                return False
            for i in data:
                if not isinstance(i, int):
                    return False
        except Exception as a:
            return False
        return True

    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        from math import sqrt
        s = int(sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) * 100) / 100
        return s


class TriangleTest(unittest.TestCase):
    valid_test_data = [
        ((3, 4, 5), 6.0),
        ((10, 10, 10), 43.30),
        ((6, 7, 8), 20.33),
        ((7, 7, 7), 21.21),
        ((50, 50, 75), 1240.19),
        ((37, 43, 22), 406.99),
        ((26, 25, 3), 36.0),
        ((30, 29, 5), 72.0),
        ((87, 55, 34), 396.0),
        ((120, 109, 13), 396.0),
        ((123, 122, 5), 300.0)
    ]
    not_valid_triangle = [
        (1, 2, 3),
        (1, 1, 2),
        (7, 7, 15),
        (100, 7, 90),
        (17, 18, 35),
        (127, 17, 33),
        (145, 166, 700),
        (1000, 2000, 1),
        (717, 17, 7),
        (0, 7, 7),
        (-7, 7, 7)
    ]
    not_valid_arguments = [
        ('3', 4, 5),
        ('a', 2, 3),
        (7, "str", 7),
        ('1', '1', '1'),
        'string',
        (7, 2),
        (7, 7, 7, 7),
        'str',
        10,
        ('a', 'str', 7)
    ]

    def test_valid_triangle(self):
        for data in TriangleTest.valid_test_data:
            triangle = Triangle(data[0])
            with self.subTest():
                self.assertEqual(triangle.get_area(), data[1])

    def test_invalid_triangle(self):
        for data in TriangleTest.not_valid_arguments:
            triangle = Triangle(data)
            with self.subTest():
                self.assertRaises(TriangleNotValidArgumentException)

    def test_not_exist_data(self):
        for data in TriangleTest.not_valid_triangle:
            triangle = Triangle(data)
            with self.subTest():
                self.assertRaises(TriangleNotExistException)



triangleTestSuite = unittest.TestSuite()
triangleTestSuite.addTest(unittest.makeSuite(TriangleTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(triangleTestSuite)
