'''
Problem:
Use the variable x as you write this program. x will represent a string. Write a program that determines if x is a vowel (a, e, i, o, and u ). If yes, print _ is a vowel, where the blank is the value of x. If no, print _ is not a vowel, where the blank is the value of x.
Expected Output:
If x is a, then the output would be: a is a vowel.
If x is z, then the output would be: z is not a vowel.'''


#Code:
import sys
x = sys.argv[1]

########################################################
# Enter your code below
########################################################
if x == "a" or x == "e" or x =="i" or x == "o" or x == "u":
    print(x + " is a vowel")
else:
    print(x + " is not a vowel")