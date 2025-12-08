# Can import game_state, but NOT main.py
import random
import time

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
        new_topic = input("What is your paper on?\n>")#The actual choice players will make
        paper_topic_list.append(new_topic)
        game_state["paper_topic"] = new_topic
    else:
        #Paper topic is assigned
        topic = random.choice(paper_topic_list)
        game_state["paper_topic"] = topic
        print(f"Oh, that's right! It was {topic}!")


def player_combo():
    """Player gets to choose combo from Union Sparty's"""
    combo = "none"
    combo_options = {
        "1": ("A Woody's burrito, energy drink, and a bag of chips", "woody_combo"),
        "one": ("A Woody's burrito, energy drink, and a bag of chips", "woody_combo"),
        "2": ("An instant ramen, a juice, and a cup of fruit", "ramen_combo"),
        "two": ("An instant ramen, a juice, and a cup of fruit", "ramen_combo"),
        "3": ("A protein drink, a bottle of water, and a small bag of trail mix", "protein_combo"),
        "three": ("A protein drink, a bottle of water, and a small bag of trail mix", "protein_combo"),
        "4": ("Maybe you're not hungry after all.", None),
        "four": ("Maybe you're not hungry after all.", None)
    }

    choice = input("Would you like to get a combo?\nType yes or no:\n> ").lower()

    if choice in ("yes", "y"):
        print("Everything looks too good!\n")
        for attempt in range(3):
            choice_combo = input(
                "What are you in the mood for?\n"
                "  1. A Woody's burrito, energy drink, and a bag of chips\n"
                "  2. An instant ramen, a juice, and a cup of fruit\n"
                "  3. A protein drink, a bottle of water, and a small bag of trail mix\n"
                "  4. Maybe you're not hungry after all.\n> "
            ).lower()

            if choice_combo in ("4", "four"):
                print("Ultimately, you decide to pass on a delicious combo.")
                return

            if choice_combo in combo_options:
                combo_text, combo_id = combo_options[choice_combo]
                print(f"You gather your items, and bring them up to the cashier.\n"
                      "They were super nice and it was a quick transaction.\n")
                if combo_id:
                    purchase_combo(combo_id)
                return
            else:
                print("Sorry, I don't understand that. Try again.")
    else:

        print("Ultimately, you decide to pass on a delicious combo.")


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
