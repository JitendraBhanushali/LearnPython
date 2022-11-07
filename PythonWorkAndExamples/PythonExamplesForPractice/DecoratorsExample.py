# Decorators
# In this example `beg` wraps `say`. if say_please is True then it
# will change the returned message.

# This file is imported
from functools import wraps
def beg(trg_fun):
    @wraps(trg_fun)
    def wrapper(*args, **kwargs):
        msg, say_please = trg_fun(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please, I am poor :(")
        return msg
    return wrapper
@beg
def say(say_please=False):
    msg = "Can you buy me a Limbupani?"
    return msg, say_please
print(say())    # => Can you buy me a Limbupani?
print(say(say_please = True))   # => Can you buy me a Limbupani? Please, I am poor :(