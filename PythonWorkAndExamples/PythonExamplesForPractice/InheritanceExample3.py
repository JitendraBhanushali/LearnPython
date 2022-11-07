# Import Two files and use methosd of class

from InheritanceExample import Superhero
from InheritanceExample2 import Bat

class Batman(Superhero, Bat):
    def __init__(self, *args, **kwargs):
        # Typically to inherit attributes you have to call super:
        # super(Batman, self).__init__(*args, **kwargs)
        # However we are dealing with multiple inheritance here, and super()
        # only works with the next base class in the MRO list.
        # So instead we explicitly call __init__ for all ancestors.
        # The use of *args and **kwargs allows for a clean way to pass arguments,
        # with each parent "peeling a layer of the onion".
        Superhero.__init__(self, 'anonymous', movie=True, superpowers=["Wealthy"], *args, **kwargs)

        Bat.__init__(self, *args, can_fly=False, **kwargs)

        # override the value for the name attribute
        self.name = "SuperMan"

    def sing(self):
        return "Lalalalalaalaalalalaaalaaa"
if __name__ == "__main__":
    supHero = Batman()
    # Get the method resolution search order used by both getattr() and super()
    # This attribute is dynamic and can be updated

    print(Batman.__mro__)   # => (<class '__main__.Batman'>,
                            # => <class 'InheritanceExample.Superhero'>,
                            # => <class 'ClassesExample.human'>,
                            # => <class 'InheritanceExample2.Bat'>, <class 'object'>)
    # This method is override
    print(supHero.get_species())    # => Superhuman

    # This method is override
    print(supHero.sing())   # => Superhuman

    # Call method that exists only in 2nd ancestor (forefather)
    print(supHero.sonar())  # => }}} Dhantanaaaaa {{{

    # Inherited class attribute
    supHero.age = 150
    print(supHero.age)      # => 150

    # Inherited attribute from and ancestor (forefather) whose defualt value is override
    print("Can I fly? " + str(supHero.fly)) # => Can I fly? False