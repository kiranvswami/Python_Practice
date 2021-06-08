temp=int(input("Enter Tempearature: "))
unit=input ("C or F: ")

if unit.upper() == 'C':
    convert=temp*1.8+32
    print(f"Tempearature in Fahreniet is: {convert} F")
else:
    convert=(temp-32)/1.8
    print(convert)