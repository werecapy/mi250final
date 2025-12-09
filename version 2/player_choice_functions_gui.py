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

def paper_topic_choice(gui,after_callback):
    """Players have the random chance of getting to pick their own paper topic."""
    if random.random() < 0.5:
        # Player chooses their own topic
        gui.display_text("What is your paper on?")
        def on_topic_entered(new_topic):
            paper_topic_list.append(new_topic)

            game_state["paper_topic"] = new_topic
            gui.display_text(f"A paper on {new_topic}? Interesting choice!\n")
            after_callback(gui)
    else:
        # Paper topic is assigned
        topic = random.choice(paper_topic_list)
        game_state["paper_topic"] = topic
        gui.display_text(f"Oh, that's right! It was {topic}!\n")
        after_callback(gui)


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


def river_restaurant_gui(gui, after_callback):
    """Restaurant choice on Grand River"""
    gui.display_text("Which restaurant do you want to go to?\n")

    def select_restaurant(meal_text, restaurant_id):
        gui.display_text(f"There are so many great choices on this menu, it's hard to pick just one!")
        gui.display_text(f"You end up picking {meal_text}.\n")
        purchase_meal(restaurant_id, meal_text)
        after_callback(gui)

    def go_back_to_union():
        gui.display_text("The walk back to the Union is pleasant.\n")
        from location_gui import union_gui
        union_gui(gui)

    def skip_eating():
        gui.display_text("You decide not to eat after all.\n")
        after_callback(gui)

    gui.show_choices({
        "Kimchi Box": lambda: select_restaurant("royal beef bulgogi bento", "kimchi_box"),
        "Playa Bowl": lambda: select_restaurant("orange power bowl", "playa_bowl"),
        "Raisin' Canes": lambda: select_restaurant("caniac combo", "raisin_canes"),
        "Five Guys": lambda: select_restaurant("double cheeseburger with a small fry", "five_guys"),
        "Detroit Wing Company": lambda: select_restaurant("10 traditional wings with buffalo sauce", "dwc"),
        "Walk back to the Union": go_back_to_union,
        "Never mind": skip_eating
    })


def eat_riv():
    """Ask if player wants to eat at a restaurant"""
    choice = input("Are you in the mood to eat? Type 'yes' or 'no'\n> ").lower()
    if choice in ("yes", "y"):
        print("You think about the wonderful restaurants along Grand River.\n")
        river_restaurant_gui()
    else:
        print("You decide not to eat and continue on.\n")


def sit_in_beal(gui):
    """Eat a meal in Beal Garden - meet Tereesa"""
    game_state["sit_in_beal"] = True

    combo_type = game_state.get("combo_type")
    #Logic for each of the different combos
    if combo_type == "woody_combo":
        gui.display_text("Sitting in a secluded part of the garden, you feast on your delicious "
              "Woody's burrito...\n")
    elif combo_type == "ramen_combo":
        gui.display_text("Well, you didn't think that through. The noodles are raw...\n")
    elif combo_type == "protein_combo":
        gui.display_text("It might not be glamorous, but it works...\n")

    time.sleep(2)
    gui.display_text("You notice the tree next to you isn't really a tree at all!\n")
    gui.display_text("It's a mascot!\n")

    # Import here to avoid circular import
    from dialogues import player_tereesa_ch_1
    player_tereesa_ch_1()

if __name__ == "__main__":
    gui = GameGUI()

    gui.run()