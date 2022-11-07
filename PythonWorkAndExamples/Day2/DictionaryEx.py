# Dictionary is nothing but it's a key value pair

d1 = {"Jerry":"Sabji,Roti","Himu":"Sabji,Chaval","Nikhil":"Chaval,Dal"}
print(d1)   # This line is print the all Dictionary keys and values
print("This line is print the selected key value:- ",d1["Jerry"])  # This line is print only Selected key and value
d1["Tarun"] = "Sabji,Roti"
print(d1)   # This line is print the all Dictionary keys and values and new added key value
d1["Parth"] = "Fast Food"
print(d1)   # This line is print the all Dictionary keys and values and new added key value
# d1["Nikunj","Harry"] = "Fast Food","Junk food"
d1.update({'Niku': 'v', 'b':'v'})
#print(d1)   # This line is print the all Dictionary keys and values and new added key values
#del d1["Nikunj","Harry"]
print(d1)
d2 = d1 # This line is copy the all dictionary but it's not good
print("This is Copy of D1:- ",d2)
del d2["Parth"]
print("This is print after Deleting some key in D2:- ",d1)
print("This is a sorted list keys:- ",sorted(d1))
print("This is check the key in dict or not:- ","Jerry" in d1)
print("This is check the key in dict or not:- ", "Harry" not in d1)
print("This is check the key in dict or not:- ", "Jerry" not in d1)
