username = input("Enter name:")
try: 
    age = int(input("Enter age:"))
    print("Hello " + username)
    if age < 0:
        print("Age cannot be negative")
    elif age < 18:
        if age < 13:
            print("You are a Child")
        else:
            print("You are a Teenager")
        print("You are not eligible to vote")
    else:
        if age >= 18 and age < 60:
            print("You are an Adult")
        else:
            print("You are a Senior Citizen")
        print("You are eligible to vote")
except ValueError:
    print("Invalid age input")