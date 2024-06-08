'''
Problem:
Write a program that takes a list of integers called numbers and replaces each element greater than 10 with a '*'. Print the new version of numbers.
Expected Output:
If numbers = [30, 1, 20, 4] then you will print ['*', 1, '*', 4]
If numbers = [5, 9, 11, 23] then you will print [5, 9, '*', '*']
Hint:
Using the iteration variable alone is not sufficient to change the element of a list. You need to be able to access the index of the iteration variable to modify the element.
Important
Do not edit the code in the top section. This code is necessary for the auto-grader to work. Add your code in the section below.
'''

#Code:
'''
for number in numbers:
    if number > 10:
        numbers[numbers.index(number)] = '*'

print(numbers)
'''