fname = input("Enter first name:")
lname = input("Enter last name:")

try:

    age = int(input("Enter user's age:"))
    if age < 0:
        print("Age cannot be negative")
    else:
        print("Full Name: " + fname + " " + lname)
        print("You will be", age, "next year")

except ValueError:
    print("Invalid age input")





