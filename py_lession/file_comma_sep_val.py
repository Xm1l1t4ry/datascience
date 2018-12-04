file = open("data\info.txt")

data = file.read()
print(type(data))
print(data)

lines = data.splitlines()
print(lines)

keys = lines[0].split(',')
values = lines[1].split(',')

student = dict()

for i in range(len(keys)):
    student[keys[i]] = values[i]
print(student)

file.close()