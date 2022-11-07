"""def ask_ok(prompt, retries=2, reminder="Please try again!"):
    while True:
        ok = input("Enter Yes or No:- ")
        if ok in ('y', 'yes', 'ya'):
            return True
        if ok in ('n', 'no', 'na', 'nop'):
            return False
        retries = retries - 1
        if retries < 0:
            raise Exception("invalid user responds")
        print(reminder)


print(ask_ok("Enter Yes or No"))
"""


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("--- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 30)
    for kw in keywords:
        print(kw, ":", keywords[kw])


print(cheeseshop("paneer", "it's not available in shop sir", shopkeeper="Devid", client="karlos", sketch="Cheeseshop"))
