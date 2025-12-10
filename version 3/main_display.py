import turtle

import turtle
window = turtle.Screen()
window.bgcolor("white") #sets background color
#Turtles
title = turtle.Turtle()


#display functions
def title():

    title.speed(0)
    title.color("black")
    title.penup()
    title.hideturtle()
    title.goto(0, 0)
    title.setheading(90)
    title.pendown()
    title.write('Mascot Dating Simulator',align='center',font=('Arial',25,'bold') )




turtle.done()