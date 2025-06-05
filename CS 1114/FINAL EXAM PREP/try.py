# QUESTION 1:

# Problem 2: Expression Analyzer

# Write a program that allows the user to enter a simple two operand expression (e.g. 5 + 4) to be
# solved. To make it interesting, allow the user to enter either in-fix notation (5 + 4), prefix notation
# (+ 5 4), or postfix notation (5 4 +).

# The program should obtain the user's input, and analyze it to determine which type expression
# the user entered. It will then either print the type of expression and the solution, or a message
# indicating that the operator (support the following: + - / *) is invalid.

# Use functions in your solution and incorporate at least one exception handling statement AND
# one exception raising statement in your program.



userinput=input("Enter any opperation to be solved :")
modinput=userinput[0]+" "+userinput[1]+" "+userinput[2]
operation=modinput.split()

sign=""
for items in operation:
    if items.isdigit()==False:
        sign=operation.pop(operation.index(items))

num1=operation[0]
num2=operation[1]

if num1.isdigit()==False:
    raise Exception (num1, "is not a digit")

if num2.isdigit()==False:
    raise Exception (num2, "is not a digit")

num1=int(num1)
num2=int(num2)

if sign=="+":
    print(num1+num2)
elif sign=="*":
    print(num1*num2)
elif sign=="/":
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("You can not divide by zero")
elif sign =="-":
    print(num1-num2)
else:
    print("you did not enter a valid operation")









            