# Create function with name outer(name). This function should return inner function with name inner.
# This inner function prints message Hello, <name>!
# For example
# tom = outer("tom")
# tom() -> Hello, tom!

def outer(name):
    def inner():
        print(f"Hello, {name}!")
    return inner


if ('outer' in locals()):
 print('function "outer" is present')
else:
 print('function "outer" is absent')

outer("Tom")()

alice = outer("Alice")
alice()