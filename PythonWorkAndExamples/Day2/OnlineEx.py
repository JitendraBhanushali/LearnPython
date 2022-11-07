"""x = int(input("Enter Any Number:- "))
print(x)
if x < 0:
    x = 0
    print("Nagativ Changed to Zero:- ", x)
elif x == 0:
    print("This is Zero")
elif x == 1:
    print("This is one")
else:
    print("This is Positive number")
"""

# while True:
#     pass

"""def error (status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 418:
            return "I am Robot"
        case _:
            return "Something want to wrong with the internet"""

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"