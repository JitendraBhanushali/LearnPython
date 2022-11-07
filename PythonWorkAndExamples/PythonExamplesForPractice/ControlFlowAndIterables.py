# crecting a variable
some_var = 5
print(some_var)
print("")   # This print for new line

# if statement
# use for spaces not for tabs
print("This for loop for check the condition")
if some_var > 10:
    print("Some_var is totally bigger than 10.")
elif some_var < 10:
    print("some_var is smaller than 10.")
else:
    print("Some_var is indeed 10.")
print("")   # This print for new line

"""
for loops iterate over lists
    print:
        dog is a hero
        cat is a hero
        mouse is a hero
"""
print("This for loop for iterate the list and give value")
for animal in ["dog", "cat", "mouse"]:
    print("{} is a hero".format(animal))
print("")   # This print for new line
"""
"range(number)" return an iterable of numbers
from zero to given number of range
"""
print("This is a forloop for range")
for i in range(4):
    print(i)
print("")   # This print for new line

"""
range(lower,upper) return iterable of numbers
for lower range to upper range
"""
print("This forloop for lower range and upper range")
for i in range(2, 8):
    print(i)
print("")   # This print for new line

"""
range(lower,upper,step) returns an iterable of numbers from the 
lower number to the upper number, while by incrementing by steps
step is not given the default value is 1.
"""
print("This forloop for incrementing steps")
for i in range(2, 7, 2):
    print(i)
print("")   # This print for new line

"""
To loop over a list and retrive the  index and value
"""
print("This forLoop for give index and value")
animal = ["dog", "cat", "cow", "mouse"]
for i, value in enumerate(animal):
    print(i, value)
print("")   # This print for new line

"""
while loop
Go until a condition is no longer met.
"""
print("While loop")
x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x+1
print("")   # This print for new line

# try catch block
print("try catch block")
try:
    # use raise to raise an error
    raise IndexError("This is an index Error")
except IndexError as e:
    pass    # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass     # Multiple exceptions can be handled together, if required.
else:        # Optional clause to the try/except block. Must follow all except blocks
    print("All good")   # Runs only if the code in try raises no exceptions
finally:     #Execute under all circumstances
    print("We can clean up resource here")
print("")   # This print for new line

# python offers a fundamental abstraction called the Iterable
# An iterable is an object that can be treated as a sequence.
# The object returned by the rang function, is an iterable.
print("Print the filled iterable key in new iterable")
filled_dict = {"One": 1, "Two": 2, "Three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)  # => dict_keys(['one', 'two', 'three']). This is an object that implements our Iterable interface.
print("")  # This print for new line

# we can loop over it.
print("This forLoop for get keys from new abstract iterable")
for i in our_iterable:
    print(i)
print("")  # This print for new line

# we cannot address element by index.
# our_iterable[1]  # Riased a TypeError
# print("")   # This print for new line

print("Get Iterable data in iterator")
# An iterable is an object that knows how to create an iterator.
our_iterator = iter(our_iterable)
# Our iterator is an object that can remember the state as we traverse through it.
# We get the next object with "next()".
print(next(our_iterator))   # This is a print a the first key
print(next(our_iterator))   # It's maintain the states
print(next(our_iterator))   # It's maintain the states
# print(next(our_iterator))   # Raises the Error StopIteration
print("")

# We can also loop over it, in fact, "for" does this implicitly!
print("Get iterator kes from froLoop")
our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i)
print("")

# All the iterable or iterator elements in list()
print("Print iterable or iterator data in list")
print("Iterable is ", list(our_iterable))   # Print the iterable data ['One', 'Two', 'Three']
print("Iterator is ", list(our_iterator))   # print the iterator data [] because state is saved
