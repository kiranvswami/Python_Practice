name=input("What's your name?")

if len(name) <= 3:
    print("Name must be greater than 3 characters.")
elif len(name)>10:
    print("Name should not exceed beyond 10 charaters")
else:
    print("Your name looks good!!")