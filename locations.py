# Can import game_state and player_choice_functions, but NOT main.py
import time
import random
from game_state import game_state
from player_choice_functions import (
    player_combo,
    paper_topic_choice,
    player_sparty_ch_1,
    breslinch1,
    eat_riv,
    sit_in_beal

)

def union():
    global combo_type
    print("The union is as busy as ever!\n"
          "Every table has at least one student sitting at it. "
          "Passing through Sparty's, you think about getting a combo.\n")
    if game_state["combo_purchase"]:
        combo_type = game_state["combo_type"]
        #this should all pass because it is only get
        if combo_type is not None:
            pass

    else:
        print("Passing through the Sparty's, you think about getting a combo.\n")
        player_combo()
    print("You continue through the union...\n")
    choice = input("What do you want to do next?\n"
                   "    1. Walk to the library\n"
                   "    2. Eat your combo.\n").strip().lower()
    if choice == "1":
        walk_through_greenspace1()
    if choice == "2":
        if combo_type == "woody_combo":
            pass
        elif combo_type == "ramen combo":
            pass
        elif combo_type == "protein_combo":
            pass
        else:
            print("You silly goose, you never bought a combo! Would you like to?\n")
            choice = input("Enter 'yes' or 'no':\n>")
            if choice == "yes":
                player_combo()
                choice = input("What do you want to do next?\n"             
                               "    1. Walk to the library\n"               
                               "    2. Eat your combo.\n").strip().lower()
                if choice == "1":
                    walk_through_greenspace1()
                if choice == "2":
                    sit_in_beal()
                    if combo_type == "woody_combo":
                        pass
                    elif combo_type == "ramen combo":
                        pass
                    elif combo_type == "protein_combo":
                        pass











def walk_through_greenspace1():
    print("Wow, it *really* is a great day! There's a perfect amount of cloud cover "
          "and a light enough breeze to not feel too chilly. The green space is indeed green!"
          " Squirrels are bounding about, "
          "living their best furry lives. You get jealous of them because you think about "
          "the 10 page paper you have to complete before next week about... what was it again?\n")
    paper_topic_choice()
    input("Press enter to continue...\n")
    library()

def walk_through_greenspace2():
    print("The sun is not quitting and neither are you! As you walk to the nearest bench"
          "to eat your combo, you notiv")

def library():
    game_state["meet_sparty"] = True
    print("Walking through the green space, you finally get to the front of the library. "
          "An interesting flyer catches your attention on the way to your usual study spot.\n")
    input("Press enter to continue...")
    print("That was... interesting?\n"
          "You feel a presence behind you.")
    time.sleep(2)
    print("..... Sparty!\n"
          "He stands there, hands on his hips, face close to yours.\n"
          "Then he starts aggressively tapping the flyer and then pointing to himself.\n"
          "Oh! He's asking if you're going to the convention.")
    player_sparty_ch_1()


def down_riv():
    """Down the river location - checks if meal was purchased"""
    print("There are a TON of cars, even though it's usually not this busy!\n"
          "Even the sign trucks are slowly crawling amongst the crowd of vehicles.\n")

    # Check if player already bought a meal
    if game_state["meal_purchased"]:
        meal_name = game_state["meal_name"]
        meal_type = game_state["meal_type"]

        if meal_type == "kimchi_box":
            print(f"You're carrying your {meal_name}.\n"
                  )

        elif meal_type == "playa_bowl":
            print(f"You're carrying your {meal_name}.\n"
                  )

        elif meal_type == "raisin_canes":
            print(f"You're carrying your {meal_name}.\n"
                  )

        elif meal_type == "five_guys":
            print(f"You're carrying your {meal_name}.\n"
                  )

        elif meal_type == "dwc":
            print(f"You're carrying your {meal_name}.\n"
                  )

    else:
        # Player hasn't bought a meal, offer the option
        eat_riv()

def breslin():
    game_state["meet_otto"] = True
    minutes = random.randint(5, 15)
    print("There's so many people here!\n"
          f"It takes about {minutes} minutes to get in.\n"
          "Inside, there's more people than you could have imagined.\n"
          "But it's not just people...")
    time.sleep(2)
    print("There are plenty of mascots, as to be expected. "
          "Walking around, you see a giant orange ball. It comes up to you and introduces itself.\n")
    print("'Hi, I'm Otto! Have you been to any of the events yet?'")
    breslinch1()


def sticker_booth():
    if game_state['meet_sparty'] and game_state['meet_otto'] == True:
        # make some game save logic for if the player has and has not met certain mascots
        print("A few dozen boxes of stickers lay before you on the vendor's table. "
              "You only recognize Sparty and Otto by name, but the other stickers look pretty cool too."
              "")

    elif game_state['meet_sparty'] == True and game_state['meet_otto'] == False:
        print("A few dozen boxes of stickers lay before you on the vendor's table. "
              "You only recognize Sparty.")
    # add the rest of the mascots to this logic

    choice = input("Would you like to buy a sticker? Type 'yes' or 'no'\n")
    if choice == ("yes", "y"):
        game_state["get_stickers"] = True
        # maybe add some turtle logic here? let the player see the stickers


def mascot_cafe():
    game_state["meet_brutus"] = True
    print("Wandering over to the mascot cafe, it looks just as busy"
          "as the rest of the convention. People are sitting at tables and being"
          "waited on by mascots that you don't know.\n"
          "Upon sitting down, a mascot comes up to you.\n"
          "'Hi, I'm Brutus. I'll be taking care of you today. what can I get you?")


def eating_contest():
    print("When you get to the stall you can't help but notice CONTINUE")


def eating_contest_watch():
    pass


def artist_alley():
    print("Wow! There's so much good art here! Vendors have traveled here from all over"
          "with their own mascots. Some of the mascots are ones you've never seen before.")
    choice = input("The sticker booth on your left seems promising, do you want to check it out?"
                   "\nType 'yes' or 'no'\n> ").lower()
    if choice == ("yes", "y"):
        sticker_booth()
    else:
        pass


def mascot_panels():
    pass


def meet_n_greets():
    print("Looking across the room, you observe the many different ")