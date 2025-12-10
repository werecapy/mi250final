import turtle

import turtle
window = turtle.Screen()
window.bgcolor("white") #sets background color
#Turtles
title = turtle.Turtle()
screen = turtle.Screen()

#display functions
def main_title():

    title.speed(0)
    title.color("black")
    title.penup()
    title.hideturtle()
    title.goto(0, 0)
    title.setheading(90)
    title.pendown()
    title.write('Mascot Dating Simulator',align='center',font=('Arial',25,'bold') )
    title.penup()

def rectangle_shape(buttons=0):
    r_length = 140
    r_width = 70
    rectangle = turtle.Turtle()

    rectangle.teleport(-101.0,-85.0)
    rectangle.speed(0)
    rectangle.forward(r_length)  # length
    rectangle.left(90)  # Turn left 90 degrees
    rectangle.forward(r_width)  # width
    rectangle.left(90)
    rectangle.forward(r_length)  # length
    rectangle.left(90)
    rectangle.forward(r_width)  #width
    rectangle.left(90)  #90 degrees original direction
    rectangle.penup()
    #rectangle.hideturtle()
    rectangle.left(90)
    rectangle.forward(35)
    rectangle.left(-90)
    rectangle.forward(70)
    rectangle.left(-90)
    rectangle.forward(10)
    if buttons ==0:
        rectangle.write("start", align='center',font=('Arial',25,'bold') )

# dev stuff

def on_screen_click(x,y):
    print(f"({x},{y})")
screen.onscreenclick(on_screen_click)
main_title()
rectangle_shape()
turtle.done()