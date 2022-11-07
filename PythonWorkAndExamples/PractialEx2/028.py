"""
Question:
Define a function that can receive two integral numbers in string form and
compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.

"""

a = input("Enter any number:- ")
b = input("Enter any number:- ")

""" ---------- String to int and sum of two numbers --------------"""


def con_int():
    c = int(a)
    d = int(b)
    e = c + d

    print("Sum of given number:- ", e)


con_int()
