import turtle
from turtle import *
import textwrap
speed(0)
main_screen = Screen()
main_screen.screensize(400, 300)

dialogue_window= turtle.Turtle()
dialogue_window.hideturtle()
def make_DW(text,font_size=16,padding=20):
    """Makes dialogue box that will autosize to whatever text"""
    #Wraps lines
    max_char=50
    lines = textwrap.wrap(text, max_char)
    #Calcuates dimensions
    char_width = font_size*.6 #character width
    line_height = font_size*1.5 #line spacing

    box_width = max_char+10
    box_height = len(lines)*line_height+padding*2
class dialogue_box:
    def __init__(self, font_size=16,padding=20):
        self.font_size=font_size
        self.padding=padding
        #Set up screen
        self.screen =turtle.Screen()
        self.screen.screensize(800, 600)
        self.screen.bgcolor("white")
        self.screen.title("Mascot Dating Simulator")
        #Set up turtle
        self.t = turtle.Turtle()
        self.t.hideturtle()
    def clear(self):
        """Clears the box for next text"""
        self.t.clear()
    def draw_box(self,text,font_size=16,padding=20):
        """Draws self fitting box"""
        self.clear()
        # Wraps lines
        max_char = 50
        lines = textwrap.wrap(text, max_char)
        # Calcuates dimensions
        char_width = font_size * .6  # character width
        line_height = font_size * 1.5  # line spacing

        box_width = max_char + 10
        box_height = len(lines) * line_height + padding * 2
        #Makes auto sizing box
        self.t.penup()
        self.t.goto(-box_width/2, -box_height/2)
        self.t.pendown()
        self.t.pensize(4)
        self.t.fillcolor("white")
        self.t.begin_fill()
        self.t.end_fill()

        #Write dialogue nodes
        self.t.penup()
        #Starting coordinate
        start_y= box_height/2 -padding- line_height/2
        self.t.goto(start_y, -box_height/2)
        for i,line in enumerate(lines):
            y_pos= start_y+i*line_height
            self.t.goto(0, y_pos)
            self.t.write(line, align="center", font=("Arial", font_size, "bold"))











done()