"""
Question:
Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield

"""
nm = int(input("Enter any number:- "))

""" ---------- This is used for divide any value by 7 ---------------"""

div7 = [i for i in range(0, nm) if (i % 7 == 0)]
print(div7)

