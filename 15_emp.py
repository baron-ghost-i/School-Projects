def read(empno):
    with open("employees.csv") as file:
        data = []
        for i in file.readlines():
            data.append(tuple(i.split(",")))
    for i in data:
        if i[0] == empno:
            return i
        else:
            continue
    return None

def write(empno, name, sal):
    with open("employees.csv", "a") as file:
        file.write("{},{},{}\n".format(empno, name, sal))
        print(f"Added employee {name}, with empno {empno} and salary {sal}")

while True:
    menu = input('''
---------------------------
Selection
---------------------------
1. Add new employee details
2. Read employee details
---------------------------
0. Exit
---------------------------
Enter number of selection: ''')
    if menu == "0":
        raise SystemExit(0)

    elif menu == "1":
        empno = input("Enter empno: ")
        name = input("Enter name: ")
        sal = input("Enter salary: ")
        write(empno, name, sal)

    elif menu == "2":
        empno = input("Enter empno: ")
        data = read(empno)
        if data != None:
            print("Name: {}\nSalary: {}".format(data[1], data[2]))
        else:
            print("Employee! not found!")
    
    else:
        print("Invalid value provided")