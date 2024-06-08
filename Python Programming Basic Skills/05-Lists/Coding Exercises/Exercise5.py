'''
Problem:
Write a program that accepts a 2D list of zeros. Print the 2D list in rows and columns without the square brackets and commas. Moving diagonally from the top-left to the bottom right, replace each 0 with a 1. The IDE already declares the variable number and the 2D list data. Use number to represent the number of rows and columns, and data to represent the 2D list of zeros.'''

'''What does `sys.argv[1]` mean?
You are expected to iterate over a 2D list with a specific number of rows and columns. However, we do not want you to know what that number is. Using sys.argv[1] allows us to send your program a "hidden" number. That number is the used to make a 2D list of zeros. Your code will be tested three times, each time with a different number of rows and columns.'''

'''
Expected Output
Input:
          [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
          ]
    
Output:

        1 0 0
        0 1 0
        0 0 1


Input:
          [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
          ]
             
Output:
        1 0 0 0
        0 1 0 0
        0 0 1 0
        0 0 0 1
      '''


#Code:

########################################################
# DO NOT EDIT THE CODE IN THE SECTION BELOW
########################################################
import sys

number = int(sys.argv[1])
data = [[0 for i in range(number)] for j in range(number)]

########################################################
# Enter your code below
########################################################
for row in range(number):
  for column in range(number):
    if row == column:
      data[row][column] = 1
    print(f"{data[row][column]} ", end="")
  print()


