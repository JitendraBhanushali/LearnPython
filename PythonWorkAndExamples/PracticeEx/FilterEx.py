""" --------------------- Filter Ex ----------------------------"""

lst = [1, 2, 3, 44, 3, 4, 53, 24, 22, 455, 3112, 53]


def is_greater_5(num):
    return num > 5


gr = list(filter(is_greater_5, lst))
print(gr)
