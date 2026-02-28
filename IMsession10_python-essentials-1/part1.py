try:
    x = int(input("Enter first number:"))   
    y = int(input("Enter second number:"))

    if y == 0:
        print("Cannot divide by zero")
    else:
        print("Sum is ",x+y)
        print("Division Quotient is ", x/y)

except ValueError:
    print("Invalid Input")
