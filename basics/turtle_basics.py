from turtle import * # import all turtle objects


# Create a window/screen
screen = Screen()
screen.bgcolor("lightblue")  # Optional: Set background color

# forward(100)
# left(90)
# forward(100)

# # Lift the pen
# penup()
# # Move the turtle without drawing
# forward(100)
# # Put the pen down to start drawing again
# pendown()
# # Draw a line
# forward(100)


# pencolor('blue')
# pensize(10)
# forward(100)
# left(90)
# forward(100)

# speed("fastest")
# circle(50)

## Trangle
# forward(100)
# left(90)
# forward(100)
# right(45)
# backward(140)
# for _ in range(4):
#     forward(100)
#     left(90)

# begin_fill()
# for _ in range(4):
#     forward(100)
#     left(90)
# end_fill()

color('green')
begin_fill()
for _ in range(4):
    forward(100)
    left(90)
end_fill()


# penup()
# goto(400,0)
# pendown()

# backward(100)
# right(90)
# backward(100)
# left(45)
# forward(150)
# pendown()

# penup()
# goto(-400,0)
# pendown()

# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)
# left(45)
# forward(100)

# forward(100)
# left(60)
# forward(50)
# left(120)
# forward(100)
# left(60)
# forward(50)

# penup()
# goto(-400,0)
# pendown()
# fillcolor('blue')
# begin_fill()
# for _ in range(8):
#     forward(100)
#     left(45)
# end_fill()

# penup()
# goto(200,0)
# pendown()
# forward(100)
# right(145)
# forward(100)
# right(145)
# forward(100)
# right(145)
# forward(100)
# right(143)
# forward(100)


# color('blue')
# home()
# backward(150)
# left(90)
# forward(100)
# left(58)
# backward(175)

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         color(c)
#         forward(steps)
#         right(30)

# color('red')
# fillcolor('yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()


screen = Screen()
screen.bgcolor("white")

# # Create a turtle object
# pen = Turtle()
# pen.color("black")
# pen.pensize(5)

# # Function to draw the letter P
# def draw_P():
#     pen.penup()
#     pen.goto(-200, 0)
#     pen.pendown()
#     pen.left(90)
#     pen.forward(100)
#     pen.right(90)
#     pen.circle(-25, 180)
#     pen.penup()
#     pen.goto(-200, 0)
#     pen.pendown()

# # Function to draw the letter H
# def draw_H():
#     pen.penup()
#     pen.goto(-150, 0)
#     pen.pendown()
#     pen.left(90)
#     pen.forward(100)
#     pen.backward(50)
#     pen.right(90)
#     pen.forward(50)
#     pen.left(90)
#     pen.forward(50)
#     pen.backward(100)

# # Function to draw the letter Y
# def draw_Y():
#     pen.penup()
#     pen.goto(-50, 100)
#     pen.pendown()
#     pen.right(30)
#     pen.forward(50)
#     pen.backward(50)
#     pen.right(120)
#     pen.forward(50)
#     pen.backward(50)
#     pen.left(60)
#     pen.forward(50)
#     pen.right(90)
#     pen.forward(50)

# # Function to draw the letter T
# def draw_T():
#     pen.penup()
#     pen.goto(0, 100)
#     pen.pendown()
#     pen.right(90)
#     pen.forward(100)
#     pen.backward(50)
#     pen.left(90)
#     pen.forward(50)

# # Function to draw the letter O
# def draw_O():
#     pen.penup()
#     pen.goto(100, 0)
#     pen.pendown()
#     pen.circle(50)

# # Function to draw the letter N
# def draw_N():
#     pen.penup()
#     pen.goto(200, 0)
#     pen.pendown()
#     pen.left(90)
#     pen.forward(100)
#     pen.right(135)
#     pen.forward(140)
#     pen.left(135)
#     pen.forward(100)

# # Draw the letters
# draw_P()
# draw_H()
# draw_Y()
# draw_T()
# draw_O()
# draw_N()

# # Hide the turtle and display the window
# pen.hideturtle()

# from random import random

# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     right(angle)
#     fd(steps)


# color('blue')
# width(10)
# penup()
# goto(-200, 0)
# pendown()
# left(90)
# forward(100)
# right(90)
# circle(-25, 180)
# penup()
# goto(-200, 0)
# pendown()

# color('green')
# circle(50)

# goto(20,0)

# color('blue')
# circle(50)

# goto(-20,0)

# color('red')
# circle(50)



# Set up the turtle
# # Turtle()
# speed(10)

# # Function to draw a ring
# def draw_ring(ring_color, x, y):
#     penup()
#     goto(x, y)
#     pendown()
#     color(ring_color)
#     circle(50)

# # Draw the Olympic rings
# ring_colors = ['blue', 'black', 'red', 'yellow', 'green']
# positions = [(-120, 0), (0, 0), (120, 0), (-60, -50), (60, -50)]

# for color, position in zip(ring_colors, positions):
#     draw_ring(ring_colors, position[0], position[1])

# Hide the turtle and display the window
#hideturtle()



done()