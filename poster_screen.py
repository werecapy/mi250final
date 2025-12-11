import turtle
"""
def poster_pic():
    #shows poster in window
    poster_window= turtle.Screen()
    poster_window.register_shape('poster.gif')
    poster_window.title("Mascot Dating Simulator")
    poster_window.bgpic("poster.gif")
    poster_window.exitonclick()

    poster_window.mainloop()"""


def poster_pic():
    """Shows poster in window"""
    poster_window = turtle.Screen()
    poster_window.title("Mascot Convention Poster")

    try:
        poster_window.register_shape('poster.gif')
        poster_window.bgpic('poster.gif')
    except:
        pass  # Image not found

    # Close on click
    def close_window(x, y):
        poster_window.bye()

    poster_window.onclick(close_window)

    try:
        poster_window.mainloop()
    except:
        pass