x = input("Enter the list (separate each value with a whitespace): ")

x = x.split(" ")
print(f"Before swapping: {x}")

element = x.pop(len(x)-1)
x.insert(0, element)

print(f"After swapping: {x}")
