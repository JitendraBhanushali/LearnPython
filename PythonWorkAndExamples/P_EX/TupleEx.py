""" ------------------Tuples and Sequences--------------------------"""

t = 12345, 54321, 'hello!'
print(t[0])
print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
t[0] = 88888
print(t)