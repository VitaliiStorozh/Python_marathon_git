# Create class Worker with fields name and salary. If salary negative raise ValueError
#
# Create a method get_tax_value() that calculate tax from salary .
# Tax must be calculate like "progressive tax" with next step:
#
# less then 1000 - 0%
# 1001 - 3000 - 10%
# 3001 - 5000 - 15%
# 5001 - 10000 - 21%
# 10001 - 20000 - 30%
# 20001 - 50000 - 40%
# more than 50000 - 47%
# Please create WorkerTest class with unitest to the class Worker. Try to use setUp and tearDown methods.
# Don`t use assertRaises in tests.

import unittest


class Worker:
    def __init__(self, name="Gabriel", salary=0):
        self.name = name
        self.salary = salary

    def get_tax_value(self, salary):
        try:
            if salary < 0:
                raise ValueError
            elif salary <= 1000:
                self.tax = 0
            elif salary <= 3000:
                self.tax = (salary - 1000) * 0.1
            elif salary <= 5000:
                self.tax = (2000 * 0.1) + ((salary - 3000) * 0.15)
            elif salary <= 10000:
                self.tax = (2000 * 0.1) + (2000 * 0.15) + ((salary - 5000) * 0.21)
            elif salary <= 20000:
                self.tax = (2000 * 0.1) + (2000 * 0.15) + (5000 * 0.21) + ((salary - 10000) * 0.3)
            elif salary <= 50000:
                self.tax = (2000 * 0.1) + (2000 * 0.15) + (5000 * 0.21) + (10000 * 0.3) + ((salary - 20000) * 0.4)
            elif salary > 50000:
                self.tax = (2000 * 0.1) + (2000 * 0.15) + (5000 * 0.21) + (10000 * 0.3) + (30000 * 0.4) + (
                        (salary - 50000) * 0.47)
        except ValueError:
            print("Nobody has salary such less Zero")
        return self.tax


class WorkerTest(unittest.TestCase):

    def setUp(self):
        self.worker = Worker()

    @unittest.expectedFailure
    def test_get_tax_minus(self):
        self.assertEqual(self.worker.get_tax_value(-1000), 0)

    def test_get_tax_zero(self):
        self.assertEqual(self.worker.get_tax_value(0), 0)

    def test_get_tax_1(self):
        self.assertEqual(self.worker.get_tax_value(1000), 0)

    def test_get_tax_3(self):
        self.assertEqual(self.worker.get_tax_value(3000), 200.0)

    def test_get_tax_5(self):
        self.assertEqual(self.worker.get_tax_value(5000), 500.0)

    def test_get_tax_10(self):
        self.assertEqual(self.worker.get_tax_value(10000), 1550.0)

    def test_get_tax_20(self):
        self.assertEqual(self.worker.get_tax_value(20000), 4550.0)

    def test_get_tax_50(self):
        self.assertEqual(self.worker.get_tax_value(50000), 16550.0)

    def test_get_tax_100(self):
        self.assertEqual(self.worker.get_tax_value(100000), 40050.0)

    def tearDown(self):
        self.worker = None


# worker1 = Worker()
# print(worker1.get_tax_value(3000))


workerTestSuite = unittest.TestSuite()
workerTestSuite.addTest(unittest.makeSuite(WorkerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(workerTestSuite)
