# Can import game_state, but NOT main.py
import random
import time

from game_state import game_state, purchase_combo, purchase_meal

paper_topic_list = ['sleep disorders', 'nuclear power',
                    "social media interaction", 'book bans']
#print(paper_topic_list)
def get_choice(options):
    print("Which do you choose?")
    for i, option in enumerate(options, 1):
        print(f"    {i}. {option}")
    choice = input(f"Enter your choice (1-{len(options)}): ")

    if choice.isdigit() and 1 <= int(choice) <= len(options):
        return int(choice)
    print(f"Please enter a number between 1 and {len(options)}")

def paper_topic_choice():
    if random.random() < 0.5:
        new_topic = input("What is your paper on?\n>")
        paper_topic_list.append(new_topic)
        game_state["paper_topic"] = new_topic
    else:
        topic = random.choice(paper_topic_list)
        game_state["paper_topic"] = topic
        print(f"Oh, that's right! It was {topic}!")


def player_combo():
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

    if combo_type == "woody_combo":
        print("Sitting in a secluded part of the garden, you feast on your delicious "
              "Woody's burrito... \n The tree next to you is beautiful.\n")
    elif combo_type == "ramen_combo":
        print("You find a secluded part of Beal garden to sit in to eat. You didn't think that through. The noodles are raw... Thankfully, you're sitting next to a tree.\n")
    elif combo_type == "protein_combo":
        print("Thankfully, you found a place to sit in beal It might not be glamorous, but it works...\n The tree next to you is beautiful.\n")

    time.sleep(2)
    print("You notice the tree next to you isn't really a tree at all!\n")


    # Import here to avoid circular import
    from dialogues import player_tereesa_ch_1
    player_tereesa_ch_1()

def pick_sticker():
    sticker_options = ["s1", "s2", "s3"]

    chosen_sticker = random.choice(sticker_options)
    game_state["sticker"] = chosen_sticker
    if game_state["sticker"] == "s3":
        print("Woah! you got a cool sticker...\n")
    else:
        print("Well that was kind of a let down...\n")
    return chosen_sticker

def convention_activities():
    #List of activities not done
    available=[]

    if not game_state.get("mascot_cafe_visit"):
        available.append("1. Mascot Cafe")
    if not game_state.get("eating_contest_visit"):
        available.append("2. Eating Contest")
    if not game_state.get("artist_alley_visit"):
        available.append("3. Artist Alley")
    if not game_state.get("mascot_panel_visit"):
        available.append("4. Mascot Panels")
    if not game_state.get("meet_n_greets_visit"):
        available.append("5. Meet & Greets")
    #ask player what they want
    print("What do you want to do?")
    for option in available:
        print(option)
    #get choice
    while True:
        choice = input("> ").lower()
        if choice in ("1", "one") and not game_state.get("mascot_cafe_visit"):
            from locations import mascot_cafe
            mascot_cafe()
        elif choice in ("2","two") and not game_state.get("eating_contest_visit"):
            from locations import eating_contest
            eating_contest()
        elif choice in ("3","three") and not game_state.get("artist_alley_visit"):
            from locations import artist_alley
            artist_alley()
        elif choice in ("4","four") and not game_state.get("mascot_panel_visit"):
            from locations import mascot_panels
            mascot_panels()
        elif choice in ("5","five") and not game_state.get("mascot_cafe_visit"):
            from locations import mascot_cafe
            mascot_cafe()
        else:
            print("Sorry, I don't understand that. Try again.\n")


def dating_show_pick():
    #final pick for dating show
    game_state["dating_show_pick"] = True
    mascot_list = ["brutus", "sparty", "tereesa"]
    print("Who do you want to pick?")
    #For loop display
    for i, name in enumerate(mascot_list, start=1):
        print(f"{i}. {name.capitalize()}")

    while True:
        choice = input("> ").lower().strip()

        # number choice
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(mascot_list):
                chosen = mascot_list[index]
            else:
                print("Not a valid number.")
                continue

        # name choice
        else:
            if choice in mascot_list:
                chosen = choice
            else:
                print("Type a valid number or the name.")
                continue

        # run dialogue
        if chosen == "brutus":
            print("Brutus is very pleased. 'I'll take you out somewhere nice in Ohio!'")
            break

        elif chosen == "sparty":
            print("Sparty is very pleased. He gives you a huge thumbs up.")
            break

        elif chosen == "tereesa":
            print("Tereesa is very pleased. You can see her leaves shaking.")
            break


def dating_show_choices():
    # People not talked to yet
    available = []

    if not game_state.get("brutus_talk"):
        available.append("brutus")
    if not game_state.get("sparty_talk"):
        available.append("sparty")
    if not game_state.get("tereesa_talk"):
        available.append("tereesa")

    # For loop display
    print("Who do you want to talk to?")
    for i, name in enumerate(available, start=1):
        print(f"{i}. ???")

    while True:
        choice = input("> ").lower().strip()

        # Numeration
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(available):
                chosen = available[index]
            else:
                print("Not a valid number.")
                continue

        # Name choices
        else:
            if choice in available:
                chosen = choice
            else:
                print("Type the number or the name of the character.")
                continue

        # Run the dialogue
        if chosen == "brutus":
            from dialogues import read_brutus
            read_brutus()
            game_state["brutus_talk"] = True

        elif chosen == "sparty":
            from dialogues import read_sparty
            read_sparty()
            game_state["sparty_talk"] = True

        elif chosen == "tereesa":
            from dialogues import read_tereesa
            read_tereesa()
            game_state["tereesa_talk"] = True

        # Check if all mascots have been talked to
        if (game_state.get("brutus_talk") and
            game_state.get("sparty_talk") and
            game_state.get("tereesa_talk")):
            dating_show_pick()
            break
        else:
            dating_show_choices()
            break







