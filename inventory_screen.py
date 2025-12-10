import turtle
from game_state import *
# Screen set up
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(600, 400)
screen.title("Mascot Dating Simulator")

# Turtles
title = turtle.Turtle()
title.hideturtle()
title.speed(0)

# Functions
def window_title(btitle="Backpack"):
    """Displays the window title"""
    title.clear()
    title.penup()

    title.color("black")
    title.goto(-180.0, 170.0)
    title.write('Backpack', align="right", font=("Arial", 24, "bold"))

def combo_pic():
    #handles combo in inventory
    if game_state["combo_type"] == "woody_combo":
        pass
    elif game_state["combo_type"] == "ramen_combo":
        pass
    else:
        #this is going to be the protein combo
        pass

def meal_pic():
    if game_state["meal_name"] == "royal beef bulgogi bento":
        pass
    elif game_state["meal_name"] == "orange power bowl":
        pass
    elif game_state["meal_name"] == "caniac combo":
        pass
    elif game_state["meal_name"] == "double cheeseburger with a small fry":
        pass
    else:
        #10 traditional wings with buffalo sauce
        pass

def poster_pic():
    pass

def pamphlet_vis():
    pass


def sticker_vis():
    pass






# Test with different titles
window_title("Mascot Dating Simulator")

# You can change the title later
# window_title("Character Selection")

#dev stuff
def handle_click(x, y):
    # This function is called with the x and y coordinates of the click
    print(f"Clicked at coordinates: ({x}, {y})")
    # Optionally, you can draw something at the click point
    coord=turtle.Turtle()
    coord.clear()
    coord.teleport(x,y)
    coord.write('Backpack', align="right", font=("Arial", 24, "bold"))
    # turtle.goto(x, y)
    # turtle.dot(5, "red")
    # turtle.pendown()

# Set up the screen and turtle


turtle.speed(0) # Fastest speed for drawing

# Bind the handle_click function to mouse clicks on the screen
turtle.onscreenclick(handle_click)

# Start the main loop to listen for events
turtle.mainloop()
