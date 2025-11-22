from player_info import backpack
import random
import time
from main import meet_the_bas
from player_choice_functions import *


#list of locations for saves




def union():
    print("The union is as busy as ever!\n"
          "Every table has as at least one student sitting at it."
          "Passing through the Sparty's, you think about getting a combo.")
    player_combo()






def walk_through_greenspace1():
    print("Wow, it *really* is a great day! There's a perfect amount of cloud cover"
          "and a light enough breeze to not feel too chilly. Squirrels are bounding about,"
          "living their best furry lives. You get jealous of them because you think about"
          "the 10 page paper you have to complete before next week about... what was it again?\n")
    paper_topic_choice()
    input("Press enter to continue...")
    library()

def library():
    print("Walking through the green space, you finally get to the front of the library."
          "An interesting flyer catches your attention on the way to your usual study spot.\n")
    #This is where the turtle function that shows the poster goes.
    input("Press enter to continue...")
    print("That was... interesting?\n"
          "You feel a presence behind you.")
    time.sleep(5)
    print("..... Sparty!\n"
          "He stands there, hands on his hips, face close to yours.\n"
          "Then he starts aggressively tapping the flyer and then pointing to himself.\n"
          "Oh! He's asking if you're going to the convention.")
    player_sparty_ch_1()







def down_riv():
    print("There are a TON of cars, even though it's usually not this busy!\n"
          "Even the sign trucks are slowly crawling amongst the crowd of vehicles.\n")
    eat_riv()


def breslin(minutes):
    minutes.randint(100)
    print("There's so many people here!\n"
          f"It takes about {minutes} minutes to get in.\n"
          "Inside, there's more people that you could have imagined.\n"
          "But it's not just people...")
    time.sleep(5)
    print("There are plenty of mascots, as to be expected."
          "Walking around, you see a giant orange ball. It comes up to you and introduces itself."
          )
    print("'Hi, I'm Otto! Have you been to any of the events yet?'")
    breslinch1()





