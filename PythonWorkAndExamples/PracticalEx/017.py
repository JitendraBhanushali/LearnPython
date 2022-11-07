"""
Question:
Write a program that computes the net amount of a bank account based a transaction
log from console input. The transaction log format is shown as following:
D 100
W 200
¡­
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""
net_amount = 0

while True:
    a = int(input("Select 1 for deposite 2 for withdrawal and 3 for Exit:-  "))

    if a == 1:
        d = int(input("how much money deposite :-"))
        net_amount += d
        print(f"D :- ", d)
        print("Account balence is :- ", net_amount)

    elif a == 2:
        w = int(input("how much money withdrawal :-"))
        net_amount -= w
        print(f"W :- ", w)
        print("Account balence is :- ", net_amount)

    elif a == 3:
        print("Thank you")
        print("Your Account Balence is:- ", net_amount)
        break
