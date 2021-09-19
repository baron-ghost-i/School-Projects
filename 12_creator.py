with open("file.txt", "r") as file:
    data = file.readlines()
    data2 = []
    l = []
    for line in data:
        for i in line:
            if i.lower() == "a":
                data2.append(line)
                break

for i in data2:
    data.remove(i)

with open("file.txt", "w") as file:
    file.writelines(data)

with open("file2.txt", "w") as file:
    file.writelines(data2)