weight=int(input("Enter your weight:"))
unit=input("(L)bs or (K)g:")


if unit.upper()=="L":
    convert=weight*0.45
    print(f"your weight is {convert} KG")
else:
    convert=weight*2.20
    print(f"Your weight is {convert} LBS")
    