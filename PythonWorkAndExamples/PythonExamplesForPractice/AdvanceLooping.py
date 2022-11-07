# Generators help you to make lazy code.
# def double_number(iterable):
#     for i in iterable:
#         yield i + i     # => 1+1 = 2, 2+2 = 4, .......6+6 = 12

# Generators are memory-efficient because they only load the data needed to
# process the next value in the iterable. This allows them to perform
# operations on otherwise prohibitively large value ranges.
# NOTE: `range` replaces `xrange` in Python 3.

# for i in double_number(range(1,123123213)):
#     print(i)
#     if i >= 11:       # => Print the number 2,4,6,8,10,12
#         break

# Just as you can create a list comprehension, you can create generator
# comprehensions as well
# values = (-x for x in [10, 20, 30, 40, 50])
# for x in values:
#     print(x)        # => Print -10, -20, -30, -40, -50

# You can also cast a generator comprehension directly to a list
values = (-x for x in [1, 2, 3, 4, 5])
generate_list = list(values)
print(generate_list)  # => Creating a list and print [-1, -2, -3, -4, -5]
