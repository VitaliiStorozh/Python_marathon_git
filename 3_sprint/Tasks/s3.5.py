# Create decorator logger. The decorator should print to the console information
# about function's name and all its arguments separated with ',' for the function decorated with logger.
#
# Create function concat with any numbers of any arguments which concatenates arguments
# and apply logger decorator for this function.


def logger(func):
    def wrapper(*args, **kwargs):
        string = ""
        for arg in args:
            string += str(arg) + ", "
        for _, kwarg in kwargs.items():
            string += str(kwarg) + ", "
        result = func(*args, **kwargs)
        print(f"Executing of function {func.__name__} with arguments {string[:-2]}...")
        return result
    return wrapper

@logger
def concat(a='', *args, **kwargs):
    s = str(a)
    for item in args:
        s += str(item)
    for value in kwargs.values():
        s += str(value)
    return s

@logger
def sum(a, b):
    return a + b

@logger
def print_arg(arg):
    print(arg)



print(concat(1))
print(concat('first string', second = 2, third = 'second string'))
print(concat('first string', {'first kwarg': 0, 'second kwarg': 'second kwarg'}))
print(sum(2,3))
dict_args={'first kwarg' :0, 'second kwarg': 'second kwarg'}
concat(**dict_args)
print_arg(2)
