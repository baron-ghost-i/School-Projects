x = input("Enter the list (separate each value with a whitespace): ")

x = x.split(" ")
for i in range(len(x)):
    x[i] = int(x[i])
print(f"Before swapping: {x}")

element = x.pop(len(x)-1)
x.insert(0, element)

print(f"After swapping: {x}")