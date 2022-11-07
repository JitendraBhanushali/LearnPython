# # We use the "class" statement to create a class
class human:
    species = "H. sapiens"
    # print(species)  # => "H. sapiens"

    def __init__(self, name):
        # Asign the argument to the instanxe's name attribute
        self.name = name
        # print("Your Name is -", {name})

        # Initialize property
        self._age = 0
    def say(self,msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    def sing(self):
        return 'yo...yo... one two... one twoo', self.name
    # A class method is shared among all instance
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species
    # A Static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "Give a return value to the computer for further function use "

    # A property is just like a getter.
    # It turns the method age() into a read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age
    # This allows the propert to be deleted
    @age.deleter
    def age(self):
        del self._age

# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this
# module is the main program.
if __name__ == '__main__':
    # Instantiate a class
    name = human(name="Jitendra")
    name.say("Hello Himanshu")   # => Jitendra: Hello Himanshu
    name1 = human(name="Himanshu")
    name1.say("Hello Jitendra")     # => Himanshu: Hello Jitendra
    # name and name1 are instance of type human,
    # or in other words: they are Human objects

    # Call our class methods
    name.say(name.get_species())    # => Jitendra: H. sapiens
    name1.say(name1.get_species())  # => Himanshu: I am a Human

    # Update The human species
    human.species = "I am a Human"  # => Change the human species value
    name.say(name.get_species())    # => new species is Jitendra: I am a Human
    name1.say(name1.get_species())  # => new species is Himanshu: I am a Human

    # Call the static methods
    print(human.grunt())    # => Give the function return value

    # Static method can be called by instance too
    print(name.grunt())     # => Give the function return value by object
    print(name1.grunt())    # => Give the function return value by object

    # Update the property of instance
    name.age = 22


    # Get the property
    name.say(name.age)      # Jitendra: 22
    name1.say(name1.age)    # Himanshu: 0 defualt age is 0
    # Update age of name 1
    name1.age = 21.9
    name1.say(name1.age)    # Updated age is Himanshu: 21.9

    # Deleted the property
    # del name.age            # Delete the age atribute of name
    # name.say(name.age)      # AttributeError: 'human' object has no attribute '_age'
    # name1.say(name1.age)    # This is a print the age










# This is for my prectice
# object = human("Jitendra")  # => Creating class object and use methods of class
# say = object.say("Dudu")  # => give a value of function & # => Create a valriable and print the return value of function
# print(say)
# sing = object.sing()    # => Create a valriable and print the return value of function
# print(sing)
# object.get_species()    # => return the value for computer
# grunt = object.grunt()     # => Create a valriable and print the return value of function
# print(grunt)
# # object.age()


# declare our own string class
# class String:
#
#     # magic method to initiate object
#     def __init__(self, string):
#         self.string = string
#
#
# # Driver Code
# if __name__ == '__main__':
#     # object creation
#     string1 = String('Hello')
#
#     # print object location
#     print(string1)  # => Print the string object loction <__main__.String object at 0x7fd6bbd58df0>

# Diffrence between print and return
# def function_that_prints():
#     print("I printed")
#
# def function_that_returns():
#     return "I returned"
#
# f1 = function_that_prints()
# f2 = function_that_returns()
# print("Now let us see what the values of f1 and f2 are")
# print(f1)   # This is a print and return a none
# print(f2)   # This is a return a given string