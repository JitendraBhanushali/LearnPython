"""
Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later


"""


class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello", self.name)


p = Person("Jit")
p.say_hello()
