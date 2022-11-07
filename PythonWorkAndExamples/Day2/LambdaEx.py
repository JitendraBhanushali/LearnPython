"""print("This is a Lamda Exaple")
j = input("Enter any number i will give you next 2 number:- ")
a = int(j)
def make_increment(n):
    return lambda x: x + n


f = make_increment(a)
print("This number is you given:- ", f(0))
print("This number is given by System:- ", f(1))
print("This number is given by System:- ",f(2))
"""

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
