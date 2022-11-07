"""
Question:
A website requires the users to input username and password to register. Write a program to check
the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""


pss = input("Enter the set of passwords :")
c_pss = []
c_pss = pss.split(',')
a = 0
A = 0
num = 0
sp = 0
for i in c_pss:
    a = len(i)
    if (a >= 6 and a <= 12):
        for x in i:
            if (x.isupper()):
                a = 1
            if (x.islower()):
                A = 1
            if (x.isdigit()):
                num = 1
            if (x in ('#', '$', '@')):
                # print(x)
                sp = 1
    if (a + A + num + sp == 4):
        print("Correct password:- ", i)
    else:
        print("Wrong password:- ", i)
