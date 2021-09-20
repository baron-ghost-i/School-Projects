def roman_num(func, n: str, value: int = None) -> int:
    def read(n):
        with open("roman.txt", "r") as foo:
            data = foo.read()
            data = eval(data)
        val = data.get(n)
        if val != None:
            print(f"{n} = {val}")
        else:
            print("Value not found")
    
    def write(n, value):
        with open("roman.txt", "r") as foo:
            data = foo.read()
            if data == "" or data == "{}":
                data = dict()
            else:
                data = eval(data)

        data.update({n: value})
        with open("roman.txt", "w") as foo:
            foo.write(str(data))
        print("Data saved!")

    if func == "read":
        read(n)
    elif func == "write":
        write(n, value)
    else:
        print("Incorrect mode provided!")

mode = input("Enter the function to be carried out (read/write): ")

n = input("Enter Roman numeral: ")

if mode == "write":
    value = input("Enter value: ")
else:
    value = None

roman_num(func = mode, n = n, value = value)
