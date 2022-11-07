# Functions
# Use "def" for creating a new function
# print("Define a function and return the value")
# def add(x, y):
#     print("x is {} and y is {}".format(x, y))
#     return x + y
# add(1, 10)  # This is a normally call a function
# add(y=6, x=5)   # Key word argument can arrive in any order.
# print("")   # This print is gives new line

# print("Define a function and return the value")
# def var_args(*args):
#     print("args is ", args)
#     return args
# var_args(1,2,3)
# print("")   # This print is gives new line

# Define a function to take a variable numbers of key word and arguments
# print("Numbers of keywords and arguments")
# def keyword_args(**kwargs):
#     print("Keyword Argument is ", kwargs)
#     return kwargs
# keyword_args(hello="Friends", myNameIs="Jerry")
# print("")   # This print is gives new line

# print("All the args and kwargs values")
# def all_the_args(*args, **kwargs):
    # print(args)
    # print(kwargs)

# all_the_args(1,2,3,4, a=21, b=32113, c=123123)
# print("")   # This print is gives new line

# when calling function, you can do the opposite of args/kwargs!
# Use * to extend tuples and use ** to exten kwargs.
# print("All the args and kwargs values separately")
# def all_the_args(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# args = (1, 2, 3, 4)
# kwargs = {'a': 21, 'c': 123123, 'b': 32113}
# all_the_args(*args)
# all_the_args(**kwargs)
# all_the_args(*args, **kwargs)
# print("")   # This print is gives new line

# Returning multiple values (with tuple assignments)
# def swap(x, y):
#     return y, x
# x = 1
# y = 2
# x, y = swap(x, y)
# print(swap(3, 4))

# global scope
# x = 5

# local scope begins here
# local variable x is not same as global variable x
# def set_x(num):
#     x = num     # => 34
#     print(x)    # => 34

# global indicates that particular var lives in th global
# def set_global_x(num):
#     global x
#     print(x)    # => 5
#     x = num     # => global variable x is set to 6
#     print(x)    # => 7
# set_x(34)
# set_global_x(7)

# Python has first class functions
# def create_add(x):
#     def add(y):
#         return x + y
#     return add
# add_20 = create_add(20)
# a = add_20(2)
# print(a)

# There are also anonymous function
# print((lambda x: x > 2)(3))   #=> True
# print((lambda x, y: x ** 2 + y ** 2)(2, 1))     # => 5

# There are buil-in higher order functions
# print(list(map(add_20, [1, 2, 3]))) # => [21, 22, 23]
# print(list(map(max, [1, 2, 3], [4, 2, 1]))) # => [4, 2, 3]

# print(list(filter(lambda x: x > 5, [1, 2, 7, 44, 3, 4, 6, 5]))) # => [7, 44, 6]

# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list which can itself be a nested list
# print([add_20(i) for i in [2, 3, 4]]) # => [22, 23, 24]
# print([x for x in [3, 4, 5, 6, 7] if x > 5])  # => [6, 7]

# You can construct set and dict comprehension as well
# print({x for x in "asdadsadweqdasdasddad" if x not in "sadasda"})   # =>{'e', 'q', 'w'}
# print({x: x**2 for x in range(8)}) # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

# a = {x: x**2 for x in range(8)}
# print(a)    # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

