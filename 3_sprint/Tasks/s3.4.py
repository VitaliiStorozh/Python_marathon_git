# Create function-generator divisor that should return all divisors of the positive number.
# If there are no divisors left function should return None.
# three = divisor(3)
# next(three) => 1
# next(three) => 3
# next(three) => None


def divisor(n):
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            yield i
    yield n
    while True:
        yield None

var = divisor(10)
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))