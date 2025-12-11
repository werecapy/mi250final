# Can import game_state and player_choice_functions, but NOT main.py
import time

import random
from game_state import game_state
from poster_screen import poster_pic
from player_choice_functions import (
    player_combo,
    paper_topic_choice,

    eat_riv,
    sit_in_beal, pick_sticker

)

# Import dialogue functions
from dialogues import (
    player_sparty_ch_1,
    player_otto_ch_1,
    player_brutus_ch_1,

)
def union():
    """Union location - buy combos"""
    print("The union is as busy as ever!\n"
          "Every table has at least one student sitting at it. "
          "\n")

    if not game_state["combo_purchase"]:
        print("Passing through the Sparty's, you think about getting a combo.\n")
        player_combo()
    if game_state["combo_purchase"] == True:
        print("As fun as getting another combo would be, you have to wait 15 minutes.\n")
    print("You continue through the union...\n")
    choice = input("What do you want to do next?\n"
                   "    1. Walk to the library\n"
                   "    2. Eat your combo.\n> ").strip().lower()

    if choice == "1":
        walk_through_greenspace1()
    elif choice == "2":
        if game_state["combo_purchase"]:
            sit_in_beal()
        else:
            print("You silly goose, you never bought a combo! Would you like to?\n")
            choice = input("Enter 'yes' or 'no':\n> ").lower()
            if choice in ("yes", "y"):
                player_combo()


def walk_through_greenspace1():
    """Walk to library through greenspace"""
    print("Wow, it *really* is a great day! There's a perfect amount of cloud cover "
          "and a light enough breeze to not feel too chilly. The green space is indeed green! "
          "Squirrels are bounding about, living their best furry lives. You get jealous of them "
          "because you think about the 10 page paper you have to complete before next week about... "
          "what was it again?\n")

    paper_topic_choice()
    input("Press enter to continue...\n")
    library()

def walk_through_greenspace2():
    """Second green space sequence"""
    print("The sun is not quitting and neither are you! As you walk to the nearest bench"
          "to eat your combo, you notiv")


def library():

    """Meet Sparty at the library"""
    game_state["meet_sparty"] = True #Saves whether player has met Sparty or not
    print("Walking through the green space, you finally get to the front of the library. "
          "An interesting flyer catches your attention on the way to your usual study spot.\n")


    input("Press enter to continue...\n")
    print("That was... interesting?\n"
          "You feel a presence behind you.")

    time.sleep(2)
    print("..... Sparty!\n"
          "He stands there, hands on his hips, face close to yours.\n"
          "Then he starts aggressively tapping the flyer and then pointing to himself.\n"
          "Oh! He's asking if you're going to the convention.\n")

    # Call the dialogue
    player_sparty_ch_1()


def down_riv():
    """Down the river location - restaurants"""
    print("There are a TON of cars, even though it's usually not this busy!\n"
          "Even the sign trucks are slowly crawling amongst the crowd of vehicles.\n")

    if game_state["meal_purchased"]:
        meal_name = game_state["meal_name"] #Saves whether the player has had a meal or not
        print(f"You're carrying your {meal_name}.\n") #inserts the type of meal
    else:
        eat_riv()


def breslin():
    """Meet Otto at Breslin - enter convention"""
    game_state["meet_otto"] = True #Saves whether the player has met Otto or not
    minutes = random.randint(5, 15) #Minute chooser variable

    print("There's so many people here!\n"
          f"It takes about {minutes} minutes to get in.\n" #Chooses how long the player has been standing in line
          "Inside, there's more people than you could have imagined.\n"
          "But it's not just people...")

    time.sleep(2)
    print("There are plenty of mascots, as to be expected. "
          "Walking around, you see a giant orange ball. It comes up to you and introduces itself.\n")

    # Call Otto's dialogue
    player_otto_ch_1()


def mascot_cafe():
    game_state["mascot_cafe_visit"]= True
    """Meet Brutus at the mascot cafe"""
    game_state["meet_brutus"] = True #Saves whether player has met Brutus or not
    print("Wandering over to the mascot cafe, it looks just as busy "
          "as the rest of the convention. People are sitting at tables and being "
          "waited on by mascots that you don't know.\n"
          "Upon sitting down, a mascot comes up to you.\n")

    # Call Brutus's dialogue
    player_brutus_ch_1()


def eating_contest():
    game_state["eating_contest_visit"] = True
    print("When you get to the stall you can't help but notice there's still a lot of people for it being a mascot convention."
          "The emcee is looking around in the crowd for their last participant...")
    if random.randint(0, 1) == 0:
        print("Oh no! He spotted you and pointed you out. It kind of feels like you have to go up there now...\n")
        time.sleep(5)
        print("What were they eating again?")
        food_choices=["pie","cake","hot dogs","pizza"]
        food_contest=random.choice(food_choices)
        game_state["food_contest_save"]=food_contest
        print(f"Oh no! It's {food_contest}!\n"
              f"That's so filling, you'll never win!")
        time.sleep(5)
        if random.randint(0, 20) == 0:
            print("Holy moly! You did it! You out ate all the other competitors!")
            game_state["eating_contest_win"] = True
        else:
            print("It turned out just like you thought it would. While you weren't last place, you were far from first.")

    else:
        print("Thankfully, the emcee's gaze passes right over you. Eternally grateful, you get out of there before he has the chance to lay his eyes on you again.\n"
              "To your right, you see the mascot meet and greets. What a fine escape plan!")







def sticker_booth():
    """Sticker booth at artist alley"""
    game_state["sticker_booth_visit"] = True
    print("A few dozen boxes of envelopes lay before you on the vendor's table. Each envelope contains one sticker.\n")

    choice = input("Would you like to buy a envelope? Type 'yes' or 'no'\n> ").lower()
    if choice in ("yes", "y"):

        game_state["get_stickers"] = True


        pick_sticker()
        print("You got some awesome stickers!\n")


def artist_alley():
    """Artist alley at convention"""
    game_state["artist_alley_visit"] = True
    print("Wow! There's so much good art here! Vendors have traveled here from all over "
          "with their own mascots. Some of the mascots are ones you've never seen before.\n")

    choice = input("The mystery sticker booth on your left seems promising, do you want to check it out? "
                   "Type 'yes' or 'no'\n> ").lower()

    if choice in ("yes", "y"):
        sticker_booth()
    else:
        print("You continue browsing the art.\n")
    print("You see a curtained off area. Upon trying to go investigate, a mascot comes up to you.\n")


def mascot_panels():
    """Mascot panels at convention"""
    game_state["mascot_panel_visit"] = True
    print("It's a very lively area with a stage set up. There's two parts to the set, the left has two stools, the right has five.\n"
          "All five stools are filled with various mascots, some you've seen, some not. On the right, the emcee is looking into the crowd.\n"
          "There's a sign above it all that reads 'Mascot Speed Dating!' Oh no! What have you gotten yourself into! Before you can hightail it out of Breslin, the emcee spots you.\n"
          "While wishing for a giant bird mascot to swoop down and rescue you from this fate, the crowd seems to have a mind of it's own!\n"
          "It pushes you to the stage where you're shove up the side stairs. There's no going back, so you take the last seat on the stage. ")



def meet_n_greets():
    """Meet & greets at convention"""
    game_state["meet_n_greets_visit"] = True
    print("Looking across the room, you observe the many different mascots waiting to meet you!\n"
          "It's wayyyy too crowded, so you find something else to do.")