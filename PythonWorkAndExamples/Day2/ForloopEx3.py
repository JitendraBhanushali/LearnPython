# for i in range(10):
#     print(i, end=" ")

'''list(range(5, 10))
print(list)

list(range(0, 15, 3))
print(list)

list(range(-10, -1000, -3))
print(list)

j = ["Jerry","Harry","Heet","Jeet"]
for i in range(len(j)):
    print(i, j[i])

sum(range(4))
print(sum)'''

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
                print(n,"Equals", x, '*', n//x)
                break
    else:
        print(n, "This is a prime number")