# Writting a file
import json

print("Open a text file")
with open("myfile.txt")as f:
    for line in f:
        print(line)
print("")

# Writing in a opened file
print("Write in myfile.txt")
contents = {"a": 1, "b": 2, "c": 3}
with open("myfile.txt", "w+") as file:
    file.write(str(contents))   # writes a string to a file
print("")

# Open another txt file
print("")
with open("myfile2.txt", "w+") as file:
    file.write(json.dumps(contents))
print("")

# Reading file
print("Reading myfile.txt")
with open("myfile.txt", "r+") as file:
    contents = file.read()
print(contents)
print("")

# Reading file
print("Reading myfile2.txt")
with open("myfile2.txt", "r+") as file:
    contents = file.read()
print(contents)