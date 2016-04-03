
def decor(func):
    def wrap():
        print('============')
        func()
        print('============')
    return wrap

def print_text():
    print('Hello World!')

decorated = decor(print_text)
decorated()


# Recursion

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))


# Sets

num_set = {1, 2, 3, 4, 5}
word_set = set(['spam', 'eggs', 'sausage'])

print(3 in num_set)
print('spam' not in word_set)


nums = {1, 2, 3, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)


first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

