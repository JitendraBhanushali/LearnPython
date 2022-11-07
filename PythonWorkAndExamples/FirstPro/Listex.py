print("List Example")
print ("This is a mix list")
product = ["Mobile","leptop","Airpods","Bottel",25]
print(product)

print("\nThis is a numeric list")
numbers = [22,25,1,23,25,22]
print(numbers)

print("\nThis is a sorted numeric list")
numbers = [22,25,1,23,25,22]
numbers.sort()
print(numbers)

print("\nThis is a revers numeric list")
numbers = [22,25,1,23,25,22,20,34]
numbers.reverse()
print(numbers)

print("\nslice numeric list")
numbers = [22,25,1,23,25,22,20,34]
print(numbers[1:5])
print(numbers[:8])
print(numbers[::])
print(numbers[::-1])
print(numbers[::-2])

print("\nmin numer , Max number, length of number")
numbers = [22,25,1,23,25,22,20,34]
print(numbers)
print(min(numbers))
print(max(numbers))
print(len(numbers))
numbers.append(35)
print(numbers)
numbers.insert(2,35)
print("\nNew number inserted list",numbers)

numbers.remove(35)
print("\n Removed number list",numbers)

numbers.pop()
print("Last number Removed by pop",numbers)