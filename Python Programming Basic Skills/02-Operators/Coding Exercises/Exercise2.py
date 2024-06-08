'''Given the variables below, determine which print statement would return False.

a = True or False
b = False and True
c = False and False

print(not c and b or a)


print(a and b and c or True)


print(not b and not a or not not c)


print(a or c and not b)

The correct answer is:

print(not b and not a or not not c)

Here are the steps to resolve this expression:

print(True and not a or not not c)
print(True and False or not not c)
print(True and False or not True)
print(True and False or False)
print(False or False)
print(False)
False
Check It!
'''