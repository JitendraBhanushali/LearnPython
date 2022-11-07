"""
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

nm = input("Enter string and number:- ")

def countnumlet(nm):
    lcount = ncount = 0

    for i in nm:
        if i.isdigit():
            ncount += 1
        elif i.isalpha():
            lcount += 1
    return lcount, ncount


latters, digits = countnumlet(nm)

print("Latters :- ", latters)
print("Digits :- ", digits)
