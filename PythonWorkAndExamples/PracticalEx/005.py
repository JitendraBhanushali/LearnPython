"""" Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters"""
class stringEx():
    def __int__(self):
        self.s1 = ""

    def get_string(self):
        self.s1 = input("Enter your string here:- ")

    def prin_string(self):
        print("Your string is now capitl:- ", self.s1.upper())


s1 = stringEx()
s1.get_string()
s1.prin_string()
