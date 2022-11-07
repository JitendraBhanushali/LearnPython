# def function_print_name(a,b,c,d):
#     print(a, b, c, d)
#
# function_print_name("jerry", "a", "dcd", "zcc")

def funargs(normal, *args, **kwargs):
    # print(args[0])
    print(normal)
    """This function is used to get all of values and print on the display"""
    for item in args:
        print(item)
    print("\nNow this is a kwargs value")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


pr = ["jitu", "hitu", "jay", "himu", "deep", "het"]
normal = "This is a normal arg"
kw = {"hello":"hello","jerry":"good programer","Himu":"Java developer"}
funargs(normal, *pr, **kw)
