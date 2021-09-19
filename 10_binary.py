import pickle

'''
with open("data.txt", "wb") as fob:
    fob.write(pickle.dumps({
        1: "Ayan Sinha",
        2: "Tiasa Mahanty",
        3: "Subhrodeep Bandopadhyay",
        4: "Arka Sinha",
        5: "Saptadipa Roy",
        6: "Asha Basu Mallik"
    }))
'''

with open("data.txt", "rb") as fob:
    data = pickle.loads(fob.read())

roll = input("Enter roll number: ")
try:
    roll = int(roll)
except ValueError:
    print("Invalid roll number provided")
except:
    raise
else:
    print(data.get(roll, "Roll number not found"))