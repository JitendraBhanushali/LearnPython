# Create another class for inherit
class Bat:

    species = "Hero"

    def __init__(self, can_fly=True):
        self.fly = can_fly

    def say(self, msg):
        msg = "Hello dudududududu"
        return msg

    def sonar(self):
        return "}}} Dhantanaaaaa {{{"

if __name__ == "__main__":
    b = Bat()
    print(b.say("Hello"))
    print(b.fly)    # => AttributeError: 'Bat' object has no attribute 'fly'
