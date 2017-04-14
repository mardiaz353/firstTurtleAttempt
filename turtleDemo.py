#import the turtle library

import turtle

#Now, create the pen function from the turtle module
t = turtle.Pen()

help(turtle.color)

#Try to move the turtle
#This code will make a box
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)


#To erase the canvas and put
#turtle back at the starting position
t.reset()

#Clears screen and leaves turtle
#everyday
t.clear()

#with up and down function, you can
#pick the pen up and down
t.reset()
t.backward(100)
t.up()
t.right(90)
t.forward(20)
t.left(90)
t.down()
t.forward(100)

