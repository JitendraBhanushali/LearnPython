""" ------------------------- Modules -------------------------"""

# n = int(input("Enter any number:- "))
#
#
# def fib(n):
#     a, b = 0, 1
#
#     while a < n:
#         print(a, end=" ")
#         a, b = b, a + b
#     print()
#
# print(fib(n))
#
# f = int(input("Enter any number:- "))
#
# def fib2(f):
#     result = []
#     a, b = 0, 1
#     while a < f :
#         result.append(a)
#         a, b  = b, a+b
#         return result
#
# print(fib(f))


import sys

a = sys.ps1

b = sys.ps2

sys.ps1 = 'C> '
print('Yuck!')
