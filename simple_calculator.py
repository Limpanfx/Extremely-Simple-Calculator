number = int(input("Choose your first number: "))
secondnumber = int(input("Choose your second number: "))
number2 = "random value"

def PrintingBorder():
    print("---------------------------------")

def PrintSpace():
    print(" ")

print("Selected numbers = ", number, "and", secondnumber)
PrintingBorder()
print("- Quick Checks:")
PrintSpace()

if number == 0:
    print("- your first number is equal to zero!")
    number2 = 2
else:
    print("- your first number isn't equal to zero!")
    number2 = 1

if secondnumber == 0:
    print("- your second number is equal to zero!")
    number2 = 2
else:
    print("- your second number isn't equal to zero!")
    number2 = 1

if number % 2 == 1:
    print("-", number, "is odd!")
elif number == 0:
    print("- your first number is: 0, not even not odd, it's zero!")
else:
    print("-", number, "is even!")

if secondnumber % 2 == 1:
    print("-", secondnumber, "is odd!")
elif secondnumber == 0:
    print("- your second number is: 0, not even not odd, it's zero!")
else:
    print("-", secondnumber, "is even!")

PrintSpace()
print("- Calculations")
PrintSpace()        

#addition
additionnumber = number + secondnumber
print("- addition =", number, "+", secondnumber, "=", additionnumber)

#subtraction
subtractionnumber = number - secondnumber
print("- subtraction =", number, "-", secondnumber, "=", subtractionnumber)

#multiplication
multiplicationnumber = number * secondnumber
print("- multiplication =", number, "*", secondnumber, "=", multiplicationnumber)

#division
divisionnumber = number / secondnumber
print("- division =", number, "/", secondnumber, "=", divisionnumber)

PrintingBorder()
