# Can import game_state, but NOT main.py
import random
import time

from tkinter import Entry

from GUI import GameGUI
from game_state import game_state, purchase_combo, purchase_meal

paper_topic_list = ['sleep disorders', 'nuclear power',
                    "social media interaction", 'book bans']

def get_choice(options):
    print("Which do you choose?")
    for i, option in enumerate(options, 1):
        #Numbers the amount of options and makes a list for player to choose, display only
        print(f"    {i}. {option}")
    choice = input(f"Enter your choice (1-{len(options)}): ") #The actual choice players will make

    if choice.isdigit() and 1 <= int(choice) <= len(options):
        return int(choice)
    print(f"Please enter a number between 1 and {len(options)}")

def paper_topic_choice():
    """Players have the random chance of getting to pick their own paper topic."""
    if random.random() < 0.5:
        #Player chooses their own topic
        paper_topic_entry=Entry(gui,text="What do you want your paper to be on?")
        new_topic = input("What is your paper on?\n>")#The actual choice players will make
        paper_topic_list.append(new_topic)
        game_state["paper_topic"] = new_topic
    else:
        #Paper topic is assigned
        topic = random.choice(paper_topic_list)
        game_state["paper_topic"] = topic
        print(f"Oh, that's right! It was {topic}!")


def player_combo_gui(gui, after_callback):
    """Player gets to choose combo from Union Sparty's"""

    gui.display_text("Would you like to get a combo?")

    def on_yes():
        gui.display_text("Everything looks too good!\n")
        game_state["combo_purchase"] = True
        show_combo_choices()

    def on_no():
        game_state["combo_purchase"] = False
        gui.display_text("Ultimately, you decide to pass on a delicious combo.")
        after_callback(gui)

    def show_combo_choices():
        gui.show_choices({
            "A Woody's burrito, energy drink, and a bag of chips":
                lambda: select_combo("woody_combo", "A Woody's burrito combo"),
            "An instant ramen, a juice, and a cup of fruit":
                lambda: select_combo("ramen_combo", "A ramen combo"),
            "A protein drink, a bottle of water, and a small bag of trail mix":
                lambda: select_combo("protein_combo", "A protein combo"),
            "Maybe you're not hungry after all": on_no
        })

    def select_combo(combo_id, combo_name):
        gui.display_text(f"You gather your items, and bring them up to the cashier.")
        gui.display_text("They were super nice and it was a quick transaction.\n")
        purchase_combo(combo_id)
        gui.display_text(f"Added {combo_name} to your backpack!\n")
        after_callback(gui)

    # Show the yes/no buttons
    gui.show_choices({
        "Yes": on_yes,
        "No": on_no
    })

def river_restaurant():
    """Restaurant choice on Grand River"""
    restaurant_options = {
        "1": ("royal beef bulgogi bento", "kimchi_box"),
        "2": ("orange power bowl", "playa_bowl"),
        "3": ("caniac combo", "raisin_canes"),
        "4": ("double cheeseburger with a small fry", "five_guys"),
        "5": ("10 traditional wings with buffalo sauce", "dwc"),
        "6": (None, "union"),
    }

    for attempt in range(5):
        restaurant_choice = input(
            "What are you going to choose?\n"
            "  1. Kimchi Box\n"
            "  2. Playa Bowl\n"
            "  3. Raisin' Canes\n"
            "  4. Five Guys\n"
            "  5. Detroit Wing Company\n"
            "  6. Walk back to the Union\n> "
        ).strip().lower()

        if restaurant_choice in restaurant_options:
            meal_text, restaurant_id = restaurant_options[restaurant_choice]

            if restaurant_id == "union":
                from locations import union
                print("The walk back to the Union is pleasant.\n")
                union()
                return
            else:
                print(f"There are so many great choices on this menu, it's hard to pick just one!\n"
                      f"You end up picking {meal_text}.\n")
                purchase_meal(restaurant_id, meal_text)
                return
        else:
            print("Sorry, I don't understand that. Try again.\n")

    print("You couldn't decide and left the restaurant.")


def eat_riv():
    """Ask if player wants to eat at a restaurant"""
    choice = input("Are you in the mood to eat? Type 'yes' or 'no'\n> ").lower()
    if choice in ("yes", "y"):
        print("You think about the wonderful restaurants along Grand River.\n")
        river_restaurant()
    else:
        print("You decide not to eat and continue on.\n")


def sit_in_beal():
    """Eat a meal in Beal Garden - meet Tereesa"""
    game_state["sit_in_beal"] = True

    combo_type = game_state.get("combo_type")
    #Logic for each of the different combos
    if combo_type == "woody_combo":
        print("Sitting in a secluded part of the garden, you feast on your delicious "
              "Woody's burrito...\n")
    elif combo_type == "ramen_combo":
        print("Well, you didn't think that through. The noodles are raw...\n")
    elif combo_type == "protein_combo":
        print("It might not be glamorous, but it works...\n")

    time.sleep(2)
    print("You notice the tree next to you isn't really a tree at all!\n")
    print("It's a mascot!\n")

    # Import here to avoid circular import
    from dialogues import player_tereesa_ch_1
    player_tereesa_ch_1()

if __name__ == "__main__":
    gui = GameGUI()

    gui.run()