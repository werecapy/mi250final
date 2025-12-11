import turtle
from game_state import *
# inventory screen set up
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(600, 400)
screen.title("Mascot Dating Simulator")

# Turtles
title = turtle.Turtle()
title.hideturtle()
title.speed(0)
combo_turtle = turtle.Turtle()
#images
screen.register_shape('combo.gif')
screen.register_shape('five_guys.gif')
screen.register_shape('playa_bowl.gif')
screen.register_shape('rasing.gif')
screen.register_shape('kimchi.gif')
screen.register_shape('dwc.gif')
screen.register_shape('sticker1.gif')
screen.register_shape('sticker2.gif')
screen.register_shape('coolsticker.gif')


# Functions
def window_title():
    """Displays the window title"""
    title.clear()
    title.penup()

    title.color("black")
    title.goto(-180.0, 170.0)
    title.write('Backpack', align="right", font=("Arial", 24, "bold"))

def combo_pic():
    #handles combo in inventory
    if game_state["combo_purchase"]:
        combo_turtle.penup()
        combo_turtle.goto(-248.0, 134.0)
        combo_turtle.shape('combo.gif')
        combo_turtle.showturtle()

def meal_pic():
    #handles meal picture in inventory
    combo_turtle.hideturtle()
    combo_turtle.teleport(-139.0, 129.0)
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


def pamphlet_vis():
    pass


def sticker_vis():
    if game_state["sticker"] == "s1":
        pass
    elif game_state["sticker"] == "s2":
        pass
    else:
         pass


def update_inventory():
    """Updates all items in inventory"""
    window_title()
    combo_pic()
    meal_pic()
    sticker_vis()









#dev stuff
def handle_click(x, y):
    # This function is called with the x and y coordinates of the click
    print(f"Clicked at coordinates: ({x}, {y})")
    # Optionally, you can draw something at the click point
    coord=turtle.Turtle()
    coord.clear()
    coord.teleport(x,y)


# Set up the screen and turtle


turtle.speed(0) # Fastest speed for drawing
window_title()
# Bind the handle_click function to mouse clicks on the screen
turtle.onscreenclick(handle_click)

# Start the main loop to listen for events
turtle.mainloop()
