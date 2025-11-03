from player_info import backpack
import random
import time
from player_choice_functions import paper_topic_choice, player_combo, player_sparty_ch_1
#list of locations for saves




def union():
    print("The union is as busy as ever!\n"
          "Every table has as at least one student sitting at it."
          "Passing through the Sparty's, you think about getting a combo.")
    player_combo()






def walk_through_greenspace1():
    print("Wow, it *really* is a great day! There's a perfect amount of cloud cover"
          "and a light enough breeze to not feel too chilly. Squirrels are bounding about,"
          "living their best furry lives. You get jealous of them because you think about\n"
          f"the 10 page paper you have to complete before next week about... what was it again?\n")
    paper_topic_choice()
    input("Press enter to continue...")
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
    input("Are you in the mood to eat?")