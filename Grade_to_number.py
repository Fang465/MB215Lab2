from ast import Break


Grade = 0
print("This will retrieve a letter grade equivalent to a given number between 0 and 100")
Grade = int(input("Enter grade as a number (between 0 and 100 only. No decimals): "))
bad_input = True
while bad_input == True:
    if Grade > 100:
        print ("Please enter a grade between 0 and 100, no decimals")
        Grade = int(input("Enter grade as a number (between 0 and 100 only. No decimals): "))
    elif Grade >= 90:
        print("This grade will result in an A")
        bad_input = False
        break
    elif Grade >= 80:
        print("This grade will result in a B")
        bad_input = False
        break
    elif Grade >= 70:
        print("This grade will result in a C")
        bad_input = False
        break
    elif Grade >= 60:
        print("This grade will result in a D")
        bad_input = False
        break
    else:
        print("This grade will result in a fail")
        bad_input = False
        break