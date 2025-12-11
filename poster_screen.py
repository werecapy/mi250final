import turtle

def poster_pic():
    #shows poster in window
    poster_window= turtle.Screen()
    poster_window.register_shape('poster.gif')
    poster_window.title("Mascot Dating Simulator")
    poster_window.bgpic("poster.gif")
    turtle.exitonclick()

    poster_window.mainloop()