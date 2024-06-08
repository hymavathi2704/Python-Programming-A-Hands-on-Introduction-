'''Turtle graphic
Rearrange the code blocks below so that their output would be the image above. If you need to practice, use the code editor to the left and press the TRY IT button to see your output in the tab entitled Preview https:/.... Note: it is not important that your colors match.'''
#Code:

import turtle # keep this line of code

t = turtle.Turtle() # keep this line of code

# Your code goes here
for outer_loop in range(4):
    for inner_loop in range(4):
        t.forward(50)
        t.rt(90)
    t.forward(100)
for last_loop in range(4):
        t.forward(50)
        t.rt(90)


turtle.mainloop() #keep this line of code