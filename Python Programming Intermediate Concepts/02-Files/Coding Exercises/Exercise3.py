'''
Problem:
Write a program that reads a text file and prints the contents in reverse order.
Expected Output:
The first two lines of your code must look like this:
import sys

test_file = sys.argv[1]
This allows for different text files to be sent to your program for testing. Hint, to open the file use with open(test_file, "r".... The TRY IT button below will send a test file to your program. You should see the following output:
The child still struggled and loaded me with epithets which carried despair to my heart; I grasped his throat to silence him, and in a moment he lay dead at my feet.
‘Frankenstein! you belong then to my enemy—to him towards whom I have sworn eternal revenge; you shall be my first victim.’
‘Hideous monster! Let me go. My papa is a syndic—he is M. Frankenstein—he will punish you. You dare not keep me.’
‘Boy, you will never see your father again; you must come with me.’
He struggled violently. ‘Let me go,’ he cried; ‘monster! Ugly wretch! You wish to eat me and tear me to pieces. You are an ogre. Let me go, or I will tell my papa.’'''

#Code:
import sys

test_file = sys.argv[1]

with open(test_file, "r") as input_file:
    lines = input_file.readlines()
    lines.reverse()
    for line in lines:
        print(line)