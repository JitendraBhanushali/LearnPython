def sqr(s):
    return s * s


def cube(c):
    return c * c * c


def mod(m):
    return m % 2


fun = [sqr, cube, mod]
print("Suare, Cube, Module")
for i in range(5):
    val = list(map(lambda x: x(i), fun))
    print(val)
