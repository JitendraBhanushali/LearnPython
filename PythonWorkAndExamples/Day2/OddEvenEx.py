"""no = input("Enter a number to check its odd or even:- ")
a = int(no)
if a % 2 == 0:
    print("This is a Even number:- ", a)
else:
    print("This is a Odd number:- ", a)"""

for no in range(2, 10):
    if no % 2 == 0:
        print("This is a Even no:- ", no)
    else:
        print("This is a Odd no:- ", no)