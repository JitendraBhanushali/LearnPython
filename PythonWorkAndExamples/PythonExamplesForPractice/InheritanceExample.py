# Inheritance allows new child classes to be defined that
# inherit methods and variable from their class.

# To import functions from other files use the following format
# from "filename-without-extension" import "function-or-class"

from ClassesExample import human

# Specify the parent class(es) as parameters to the class definition
class Superhero(human):
    # If the child class should inherit all of the parent's definitions without
    # any modifications, you can just use the "pass" keyword (and nothing else)
    # but in this case it is commented out to allow for a unique child class:
    # pass

    # Child classes can override their parents' attributes
    species = "Superhuman"

    def __init__(self, name, movie=False, superpowers = ["Super Strength", "Bulletproofing"]):

        self.fictional = True
        self.movie = movie

        self.superpowers = superpowers


        super().__init__(name)

    def sing(self):
        return "Aee Haloooooo"

    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}".format(pow=power))
if __name__ == "__main__":
    supHero = Superhero(name="Hanuman")

    # Instance type checks
    if isinstance(supHero, human):
        print("I am Human")
    if type(supHero) is Superhero:
        print("I am a SuperHero")

    # Get the method resolution search order used by both gettatte() and super()
    # This attribute is dynamic and can be updated
    print(Superhero.__mro__)    # => (<class '__main__.Superhero'>,
                                # <class 'ClassesExample.human'>, <class 'object'>)

    # Calling parent method but uses its own class attribute
    print(supHero.get_species())    # => Superhuman

    # Class overridden method
    print(supHero.sing())   # => Aee Haloooooo

    # Class method from human
    supHero.say("Have a Gada")  # => Hanuman: Have a Gada

    # Call method that exists only in Superhero
    supHero.boast()     # => I wield the power of Super Strength
                        # => I wield the power of Bulletproofing

    supHero.age = 23    # => Inherited class attribute
    print(supHero.age)  # => Print the age 23

    # This Attribute that only exists within Superhero
    print("Am I Oscar eligable?" + str(supHero.movie))