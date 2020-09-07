# Write the program that calculate total price with discount by the products.
#
# Use class Product(name, price, count) and class Cart. In class Cart you can add the products.
#
# Discount depends on count product:
#
# count	discount
# 2	    0%
# 5	    5%
# 7	    10%
# 10	20%
# 20	30%
# more than 20	50%
# Write unittest with class CartTest and test all methods with logic

import unittest
from parameterized import parameterized


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


    def discount_calc(self):
        if self.count <= 2:
            self.price_with_discount = self.price
        elif self.count <= 5:
            self.price_with_discount = round(self.price * 0.95, 2)
        elif self.count <= 7:
            self.price_with_discount = round(self.price * 0.9, 2)
        elif self.count <= 10:
            self.price_with_discount = round(self.price * 0.8, 2)
        elif self.count <= 20:
            self.price_with_discount = round(self.price * 0.7, 2)
        elif self.count > 20:
            self.price_with_discount = round(self.price * 0.5, 2)
        return self.price_with_discount


class Cart:
    def __init__(self):
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)

    def totalprice(self):
        self.totalprice = 0
        for product in self.product_list:
            self.totalprice += product.discount_calc()*product.count
        return self.totalprice



class CartTest(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("eggs", 12, 0)
        self.product2 = Product("bread", 24, 5)

    def test_discount(self):
        self.assertEqual(self.product1.discount_calc(), 12)
        self.assertEqual(self.product2.discount_calc(), 22.8)

    def tearDown(self):
        self.product1 = None
        self.product2 = None

# product1 = Product("eggs", 12, 0)
# product2 = Product("bread", 24, 5)
# product3 = Product("ice-cream", 45, 7)
# product4 = Product("каун", 45, 10)
# product5 = Product("батерейки", 45, 20)
# product6 = Product("гайки", 45, 30)
#
# zakaz = Cart()
# zakaz.add_product(product1)
# zakaz.add_product(product2)
# zakaz.add_product(product3)
# zakaz.add_product(product4)
# zakaz.add_product(product5)
# zakaz.add_product(product6)
# print(zakaz.totalprice())

productTestSuite = unittest.TestSuite()
productTestSuite.addTest(unittest.makeSuite(CartTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(productTestSuite)