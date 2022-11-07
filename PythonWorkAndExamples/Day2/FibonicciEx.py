"""n = input("Enter any number:- ")
j = int(n)

def fib(j):
    a, b = 0, 1
    while a < j:
        print(a, end=',')
        a, b = b, a+b
        # print()
fib(j)"""

"""def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        return result
f100 = fib2(100)
# f100"""


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # see below
        a, b = b, a + b
    return result


fib2(100)  # call it

