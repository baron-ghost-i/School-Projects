def Student_Record(filename, **data):
    with open(filename, "a+") as fob:
        name, address, roll_no = data.get("Name"), data.get("Address"), data.get("Roll_no")
        line = f"{name},{address},{roll_no}\n"
        fob.write(line)
    print("Added record!")

def Student_Readdata(filename):
    with open(filename) as fob:
        data = fob.readlines()
        for i in data:
            data[data.index(i)] = i.replace("\n", "")
    for i in data:
        record = i.split(",")
        print("Name: {}, Address: {}, Roll number: {}".format(record[0], record[1], record[2]))

def Student_Search(filename, rollno):
    with open(filename) as fob:
        data = fob.readlines()
        for i in data:
            data[data.index(i)] = i.replace("\n", "")
    for i in range(len(data)):
        data[i] = tuple(data[i].split(","))

    for i in data:
        if i[2] == rollno:
            out = f'''Name: {i[0]}
Address: {i[1]}'''
            print(out)
            break

while True:
    menu = input('''
----------------------------
Selection
----------------------------
1. Add new student record
2. Read the student records
----------------------------
0. Exit
----------------------------
Enter number of selection: ''')
    if menu == "0":
        raise SystemExit(0)
    elif menu == "1":
        name = input("Enter name: ")
        address = input("Enter address (do not use commas in address): ")
        roll_no = input("Enter roll no.: ")
        data = {"Name": name, "Address": "address", "Roll_no": roll_no}
        Student_Record("student.txt", **data)
    elif menu == "2":
        menu2 = input('''Selection
------------------------------------------
1. Read all records
2. Read the record for a specified student
------------------------------------------
0. Return
------------------------------------------
Enter number of selection: ''')
        if menu2 == "0":
            pass
        elif menu2 == "1":
            Student_Readdata("student.txt")
        elif menu2 == "2":
            roll_no = input("Enter roll number to be searched for: ")
            Student_Search("student.txt", roll_no)
        else:
            print("Incorrect selection provided!")
    else:
        print("Incorrect selection provided!")