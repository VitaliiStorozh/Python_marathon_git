class Goods:

    def __init__(self, price, discount_strategy=None):
        self.discount_strategy = discount_strategy
        self.price = price

    def price_after_discount(self):
        if self.discount_strategy is not None :
            return self.discount_strategy(self.price)
        else:
            return self.price
    def __str__(self):
        return (f"Price: {self.price}, price after discount: {self.price_after_discount()}")


twenty_percent_discount = lambda price: price * 0.8
on_sale_discount = lambda price: price * 0.5

print(Goods(20000))

print(Goods(20000, discount_strategy=twenty_percent_discount))

print(Goods(20000, discount_strategy=on_sale_discount))
