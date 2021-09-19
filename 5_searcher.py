import re

def find(query: str, target: str):
    data = target.split()
    for i in data:
        if i == query:
            return data.index(i)
        elif query in i:
            for j in i.replace(query, ""):
                if j.isalpha():
                    return None
            return data.index(i)
        else:
            continue
    return None

target = input("Enter string to be checked: ")
query = input("Enter the word to be searched for: ")

index = find(query = query, target = target)
if index != None:
    print(f"Word found at position {index+1}")
else:
    print("The word was not found!")