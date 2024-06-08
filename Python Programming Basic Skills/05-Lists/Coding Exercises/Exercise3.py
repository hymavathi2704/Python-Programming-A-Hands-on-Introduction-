'''
Problem:
Write a program that takes a list called strings that contains a random selection of strings. Your program should print the first string when arranged in alphabetical order.
Expected Output:
If strings = ['luck', 'cat', 'kid', 'house'] then you will print cat
If strings = ['duck', 'dddd', 'mouse', 'kite'] then you will print dddd'''

#Code:

########################################################
# DO NOT EDIT THE CODE IN THE SECTION BELOW
########################################################
import sys

strings = sys.argv[1:]

########################################################
# Enter your code below
########################################################
strings.sort()
print(strings.pop(0))
print(min(strings))