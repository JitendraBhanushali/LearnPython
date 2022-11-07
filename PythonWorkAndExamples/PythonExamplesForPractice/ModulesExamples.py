# You can import modules
import math
# a = math.sqrt(16)
# print(a)    # => 4.0

# You can get a specific function from a module.
# from math import ceil, floor
# print(ceil(3.0))    # => 3
# print(ceil(3.01))    # => 4
# print(floor(3.2))   # => 3
# print(floor(3.99))   # => 3


# You can import all functions from module.
# Warning: this is not recommended
from math import *

# You can shorten module names
# import math as m
# a = math.sqrt(16) == m.sqrt(16)
# print(a)    # => Trues

# Python modules are just ordinary Python files.
# You can write your own and import then.
# The name of the module is same as the name of the file.

# print(dir(math))

# If you have a Python script named mathe.py in the same folder as your current script,
# the file math.py will be loaded insted of the built-in Python module.
# This happens because the local folder has priority over Python's built-in libraries.

