import turtle

"""def poster_pic():
    #shows poster in window
    poster_window= turtle.Screen()
    poster_window.register_shape('poster.gif')
    poster_window.title("Mascot Dating Simulator")
    poster_window.bgpic("poster.gif")
    poster_window.exitonclick()

    poster_window.mainloop() first attempt..."""



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

    # Create turtle
    poster = turtle.Turtle()
    poster.hideturtle()

    # Register shape

    screen.register_shape("poster.gif")
    poster.shape("poster.gif")


    # Close on click
    def close_window(x, y):
        screen.bye()

    screen.onclick(close_window)

    turtle.mainloop()   # event loop

