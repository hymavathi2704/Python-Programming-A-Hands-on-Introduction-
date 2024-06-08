'''
Problem:
Use the variable x as you write this program. x will represent a string. Write a program using the elif keyword that determines if x is a primary color (red, blue, or yellow). If yes, print _ is a primary color, where the blank is the value of x. If no, print _ is not a primary color, where the blank is the value of x.
Expected Output:
If x is red, then the output would be: red is a primary color.
If x is teal, then the output would be: teal is not a primary color.'''


#Code:
import sys
x = sys.argv[1]

########################################################
# Enter your code below
########################################################
if x == "red":
    print(x + " is a primary color")
elif x == "blue":
    print(x + " is a primary color")
elif x == "yellow":
    print(x + " is a primary color")
else:
    print(x + " is not a primary color")
