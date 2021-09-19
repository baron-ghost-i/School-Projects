import pickle

with open("data2.txt", "wb") as fob:
    fob.write(pickle.dumps([
        {"name": "Ayan Sinha", "roll": 1, "marks": 95},
        {"name": "Tiasa Mahanty", "roll": 2, "marks": 94},
        {"name": "Subhrodeep Bandopadhyay", "roll": 3, "marks": 100},
        {"name": "Arka Sinha", "roll": 4, "marks": 95},
        {"name": "Saptadipa Roy", "roll": 5, "marks": 93},
        {"name": "Asha Basu Mallik", "roll": 6, "marks": 97}
    ]))

with open("data2.txt", "rb") as fob:
    data = pickle.loads(fob.read())
roll = input("Enter roll number: ")
try:
    roll = int(roll)
except ValueError:
    print("Invalid roll number provided")
except:
    raise
else:
    for i in data:
        if i["roll"] == roll:
            index = data.index(i)
            break
    try:
        marks = int(input("Enter updated marks: "))
    except ValueError:
        print("Invalid value for marks provided")
    else:
        data[index]["marks"] = marks
        with open("data2.txt", "wb") as fob:
            fob.write(pickle.dumps(data))