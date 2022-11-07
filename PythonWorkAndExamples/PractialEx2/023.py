"""
Question:
    Write a method which can calculate square value of number

Hints:
    Using the ** operator

"""
n = int(input("Enter any number:- "))


def square(n):
    sqr = n ** 2

    print("Square of number is:- ", sqr)


square(n)
