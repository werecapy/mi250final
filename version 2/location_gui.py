# Can import game_state and player_choice_functions, but NOT main.py
import time
import random

from GUI import GameGUI
from game_state import game_state
from player_choice_functions import (
    player_combo,
    paper_topic_choice,


    eat_riv,
    sit_in_beal

)

# Import dialogue functions
from dialogues import (
    player_sparty_ch_1,
    player_otto_ch_1,
    player_brutus_ch_1,
    player_tereesa_ch_1
)
def union_gui(gui):
    """Union location - buy combos"""
    gui.display_text("The union is as busy as ever!\n"
          "Every table has at least one student sitting at it. "
          "\n")

    if not game_state["combo_purchase"]:
        gui.display_text("Passing through the Sparty's, you think about getting a combo.\n")
        player_combo()
    if game_state["combo_purchase"] == True:
        gui.display_text("As fun as getting another combo would be, you have to wait 15 minutes.\n")
    gui.display_text("You continue through the union...\n")
    choice = input("What do you want to do next?\n"
                   "    1. Walk to the library\n"
                   "    2. Eat your combo.\n> ").strip().lower()

    if choice == "1":
        walk_through_greenspace1_gui(gui)
    elif choice == "2":
        if game_state["combo_purchase"]:
            sit_in_beal()
        else:
            gui.display_text("You silly goose, you never bought a combo! Would you like to?\n")
            choice = input("Enter 'yes' or 'no':\n> ").lower()
            if choice in ("yes", "y"):
                player_combo(gui)


def walk_through_greenspace1_gui(gui):
    """Walk to library through greenspace"""
    gui.display_text("Wow, it *really* is a great day! There's a perfect amount of cloud cover "
          "and a light enough breeze to not feel too chilly. The green space is indeed green! "
          "Squirrels are bounding about, living their best furry lives. You get jealous of them "
          "because you think about the 10 page paper you have to complete before next week about... "
          "what was it again?\n")

    paper_topic_choice()
    input("Press enter to continue...\n")
    library_gui(gui)

def walk_through_greenspace2_gui(gui):
    """Second green space sequence"""
    gui.display_text("The sun is not quitting and neither are you! As you walk to the nearest bench"
          "to eat your combo, you notiv")


def library_gui(gui):
    """Meet Sparty at the library"""
    game_state["meet_sparty"] = True #Saves whether player has met Sparty or not
    gui.display_text("Walking through the green space, you finally get to the front of the library. "
          "An interesting flyer catches your attention on the way to your usual study spot.\n")

    input("Press enter to continue...\n")
    gui.display_text("That was... interesting?\n"
          "You feel a presence behind you.")

    time.sleep(2)
    gui.display_text("..... Sparty!\n"
          "He stands there, hands on his hips, face close to yours.\n"
          "Then he starts aggressively tapping the flyer and then pointing to himself.\n"
          "Oh! He's asking if you're going to the convention.\n")

    # Call the dialogue
    player_sparty_ch_1(gui)


def down_riv_gui(gui):
    """Down the river location - restaurants"""
    gui.display_text("There are a TON of cars, even though it's usually not this busy!\n"
          "Even the sign trucks are slowly crawling amongst the crowd of vehicles.\n")

    if game_state["meal_purchased"]:
        meal_name = game_state["meal_name"] #Saves whether the player has had a combo or not
        gui.display_text(f"You're carrying your {meal_name}.\n") #inserts the type of combo
    else:
        eat_riv(gui)


def breslin_gui(gui):
    """Meet Otto at Breslin - enter convention"""
    game_state["meet_otto"] = True #Saves whether the player has met Otto or not
    minutes = random.randint(5, 15) #Minute chooser variable

    gui.display_text("There's so many people here!\n"
          f"It takes about {minutes} minutes to get in.\n" #Chooses how long the player has been standing in line
          "Inside, there's more people than you could have imagined.\n"
          "But it's not just people...")

    time.sleep(2)
    gui.display_text("There are plenty of mascots, as to be expected. "
          "Walking around, you see a giant orange ball. It comes up to you and introduces itself.\n")

    # Call Otto's dialogue
    player_otto_ch_1(gui)


def mascot_cafe_gui(gui):
    """Meet Brutus at the mascot cafe"""
    game_state["meet_brutus"] = True #Saves whether player has met Brutus or not
    gui.display_text("Wandering over to the mascot cafe, it looks just as busy "
          "as the rest of the convention. People are sitting at tables and being "
          "waited on by mascots that you don't know.\n"
          "Upon sitting down, a mascot comes up to you.\n")

    # Call Brutus's dialogue
    player_brutus_ch_1(gui)


def eating_contest_gui(gui):
    gui.display_text("When you get to the stall you can't help but notice CONTINUE")


def eating_contest_watch_gui(gui):
    pass



def sticker_booth_gui(gui):
    """Sticker booth at artist alley"""
    gui.display_text("A few dozen boxes of stickers lay before you on the vendor's table.\n")

    if game_state['meet_otto'] is True:
        gui.display_text("You recognize Sparty and Otto stickers, plus many others!\n")
    elif game_state['meet_otto'] and  game_state['meet_tereesa'] is True :
        gui.display_text("You see Sparty, Otto, and Tereesa among all the stickers.")

    else:
        gui.display_text("You recognize Sparty stickers and many others!\n")

    choice = input("Would you like to buy a sticker? Type 'yes' or 'no'\n> ").lower()
    if choice in ("yes", "y"):
        game_state["get_stickers"] = True
        gui.display_text("You got some awesome stickers!\n")


def artist_alley_gui(gui):
    """Artist alley at convention"""
    gui.display_text("Wow! There's so much good art here! Vendors have traveled here from all over "
          "with their own mascots. Some of the mascots are ones you've never seen before.\n")

    choice = input("The sticker booth on your left seems promising, do you want to check it out? "
                   "Type 'yes' or 'no'\n> ").lower()

    if choice in ("yes", "y"):
        sticker_booth_gui(gui)
    else:
        print("You continue browsing the art.\n")


def mascot_panels_gui(gui):
    """Mascot panels at convention"""
    gui.display_text("You find the panel discussion. Mascots are talking about their experiences.\n")


def meet_n_greets_gui(gui):
    """Meet & greets at convention"""
    gui.display_text("Looking across the room, you observe the many different mascots waiting to meet you!\n")

if __name__ == "__main__":
    gui = GameGUI()

    gui.run()