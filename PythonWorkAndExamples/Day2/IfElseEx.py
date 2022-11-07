age = int(input("Enter your age for your driving license:- "))

if age != 7:
    print("Your age is not valid please enter valid age")
elif age < 18:
    print("You are not eligible")
elif age == 18:
    print("Please come to RTO")
elif age > 50:
    print("Your license is expired please renew it")

else:
    print("You are eligible Please come to RTO")