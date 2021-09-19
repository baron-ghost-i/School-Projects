import os
import re

datalist = []
for i in os.scandir(path = "14"):
    with open(f"14/{i.name}", "r") as fob:
        data = fob.read().replace("\n", " ").split()
        for i in range(len(data)):
            data[i] = re.sub(r"[.!,:,\?]", "", data[i])
        datalist.append(data)
wordlist = [i for words in datalist for i in words]
print(wordlist)
maxcount, word = 0, None
for i in wordlist:
    count = wordlist.count(i)
    if count > maxcount:
        word, maxcount = i, count

print("Most common word: \"{}\", found: {} times".format(word, maxcount))