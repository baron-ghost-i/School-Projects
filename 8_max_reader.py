import re

with open("file.txt", "r") as fob:
    lines = fob.readlines()
    words = [word for i in lines for word in i.split()]
for i in words:
    words[words.index(i)] = re.sub(r"[\?\.,:;\n]", "", i)

word = ""

for i in words:
    if len(i) > len(word):
        word = i


print(f"Longest word: {word}")
print(f"Longest line: {max(lines)}")