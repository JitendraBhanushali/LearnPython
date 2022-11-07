from functools import reduce

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 0
# ----------- first Way --------------------------
for i in list1:
    num = num + i
print(num)

# -------------- Second way -----------------------
# num = reduce(lambda x, y: x + y, list1)
# print(num)

