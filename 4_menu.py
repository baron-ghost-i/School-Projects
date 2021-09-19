import math
from datetime import datetime, timezone, timedelta
from typing import Union

menudict = {
    "1": ("circle", "area"),
    "2": ("circle", "circumference"),
    "3": ("rectangle", "area"),
    "4": ("rectangle", "perimeter"),
    "5": "date",
    "6": "time",
    "0": "exit"
}

def geometry(**kwargs) -> Union[float, None]:
    shape, type, dimension1, dimension2 = kwargs.get("shape"), kwargs.get("type"), kwargs.get("dimension1"), kwargs.get("dimension2")
    def circle(type, dimension1):
        if type == "area":
            return round(math.pi*(dimension1**2), 2)
        elif type == "circumference":
            return round(2*math.pi*dimension1, 2)
        else:
            return None
    
    def rectangle(type, dimension1, dimension2):
        if type == "area":
            return round(dimension1*dimension2, 2)
        elif type == "perimeter":
            return round(2*(dimension2+dimension1), 2)
        else:
            return None
    
    if shape == "rectangle":
        return rectangle(type, dimension1, dimension2)
    elif shape == "circle":
        return circle(type, dimension1)
    else:
        raise RuntimeError("Invalid selection provided")

def timedate(type: str):
    tz = timezone(timedelta(hours = 5, minutes = 30))
    time_ = datetime.now(tz)
    if type == "date":
        return time_.strftime("Current date: %Y, %B %d, %A")
    elif type == "time":
        return time_.strftime("Current time: %H:%M:%S, %d/%m/%y")

while True:
    menu = input('''
------------------------------------
Selection
------------------------------------
1. Area of circle
2. Circumference of circle
3. Area of rectangle
4. Perimeter of rectangle
5. Current year, month and day
6. Current date and time
------------------------------------
0. Exit
------------------------------------
Enter number of selection: ''')

    option = menudict.get(menu)

    if isinstance(option, tuple):
        shape, type = option
        options = {"shape": shape, "type": type}
        if shape == "circle":
            d1 = input("Enter the radius (value only): ")
            options.update({"dimension1": float(d1)})
        else:
            d1 = input("Enter length (value only): ")
            d2 = input("Enter breadth (value only): ")
            options.update({"dimension1": float(d1), "dimension2": float(d2)})
        output = geometry(**options)
        print(f"{type.title()} of {shape}: {output}")

    elif isinstance(option, str):
        if option != "exit":
            print(timedate(option))
        else:
            raise SystemExit(0)
    else:
        print("Invalid input!")