# Create a collection
Humans = {"jerry": "Active", "ravi": "Inactive", "Raj": "Active", "hitesh": "Inactive"}

for user, status in Humans.copy().items():
    if status == "Inactive":
        del Humans[user]
        print(Humans)
print("\n")
active_user = {}
for user, status in Humans.items():
    if status == "Active":
        active_user[user] = status
        print(active_user)
