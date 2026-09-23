import turtle

window = turtle.Screen()
window.setup(400, 200) 
colors = ["red","green","blue","cyan","yellow","magenta"] 

# Setting UP t1 
t1 = turtle.Turtle()
t1.pensize(3)                 # set the width of her pen

# Step 0:  Move to the left
t1.up()
t1.backward(120)
t1.down()

# Basic Block: Drawing triangle 1 with t1
t1.color(colors[0])
t1.forward(40)
t1.left(120)
t1.forward(40)
t1.left(120)
t1.forward(40)
t1.left(120)
t1.up()
t1.forward(40)
t1.down()

# Challenge 1:
# Replicate and modify the Basic Block to draw a new shape
t1.color(colors[1])
t1.forward(60)
t1.left(45)
t1.forward(40)
t1.left(45)
t1.forward(40)
t1.left(45)
t1.forward(40)
t1.left(45)
t1.forward(40)
t1.left(45)
t1.forward(40)
t1.left(45)
t1.forward(40)
t1.left(45)
t1.forward(40)
t1.left(45)
t1.up()
t1.forward(40)
t1.down()
# Challenge 2:
# Draw 6 copies of your new shape, one in each color

# Challenge 3 (time permitting):
# What else can you draw?