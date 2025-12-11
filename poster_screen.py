import turtle

"""def poster_pic():
    #shows poster in window
    poster_window= turtle.Screen()
    poster_window.register_shape('poster.gif')
    poster_window.title("Mascot Dating Simulator")
    poster_window.bgpic("poster.gif")
    poster_window.exitonclick()

    poster_window.mainloop()"""


"""
def poster_pic():
    #Shows poster in window
    poster_window = turtle.Screen()
    poster_window.title("Mascot Convention Poster")
    #make poster show up
    poster_turt = turtle.Turtle()
    poster_window.register_shape('poster.gif')
    poster_turt.hideturtle()
    poster_turt.shape('poster.gif')
    poster_turt.shapesize(50)
    try:

        poster_window.bgpic('poster.gif')
    except:
        print("poster.gif not found")

    # Close on click
    def close_window(x, y):
        poster_window.bye()

    poster_window.onclick(close_window)

    try:
        poster_window.mainloop()
    except:
        pass
poster_pic()"""
def poster_pic():
    # Shows poster in window
    screen = turtle.Screen()
    screen.title("Mascot Convention Poster")

    # Try to load background
    try:
        screen.bgpic("poster.gif")     # Background image
    except turtle.TurtleGraphicsError:
        print("poster.gif not found")
        return

    # Create turtle (not necessary for bgpic but kept)
    poster = turtle.Turtle()
    poster.hideturtle()

    # Register shape safely
    try:
        screen.register_shape("poster.gif")
        poster.shape("poster.gif")
    except turtle.TurtleGraphicsError:
        pass

    # Close on click
    def close_window(x, y):
        screen.bye()

    screen.onclick(close_window)

    turtle.mainloop()   # event loop

