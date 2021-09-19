with open("file.txt", "r") as fob:
    data = fob.read()
data = data.replace(" ", "#").replace("\n", "#")
print(data)