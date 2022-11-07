# ------------- Store function value in other function ---------

# def function1():
#     print("Hello Friends")
#
#
# # function1()
#
# fun2 = function1
# del function1
# fun2()

# ------------  Return Functions -----------

# def functionret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
# a = functionret(1)
# print(a)

# ---------- function as a function argument --------------
#
# def executer (fun):
#     fun("This is a function as a function argument ")
#
# executer(print)

# ------------ Decoration function used -------------

def dec1(func1):
    def nowexe():
        print("Executing start")
        func1()
        print("Executed")

    return nowexe

@dec1      """ this is a decoreted function used """
def who_is_jitu():
    print("Jitu is a good boy")


# who_is_jitu()

# who_is_jitu = dec1(who_is_jitu)
who_is_jitu()
