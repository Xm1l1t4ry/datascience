import os
import os.path

answer = os.path.exists("numbers.txt")
a = os.path.isfile("numbers.txt")
b = os.path.isdir("data")
print(answer)
print(a, b)

file = open("data/name.txt")
data_in_file = file.read()
print(data_in_file)
lines = file.readlines()
print(lines)
file.close()