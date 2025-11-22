# Can import game_state, but NOT main.py
import random
from game_state import game_state, purchase_combo

paper_topic_list = ['sleep disorders', 'nuclear power',
                    "social media interaction", 'book bans']


def paper_topic_choice():
    if random.random() < 0.5:
        new_topic = input("What is your paper on? ")
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
                print(f"You gather your items: {combo}, and bring them up to the cashier.\n"
                      "They were super nice and it was a quick transaction.\n")
                if combo_id:
                    purchase_combo(combo_id)
                return
            else:
                print("Sorry, I don't understand that. Try again.")
    else:

        print("Ultimately, you decide to pass on a delicious combo.")


def player_sparty_ch_1():
    paper_topic = game_state["paper_topic"]
    choice = input(f"What do you say?\n"
                   f"  1. 'Sorry Sparty, but I have to go write a 10 page paper on {paper_topic}.'\n"
                   f"  2. 'You know, I should be working on my paper, but this seems exciting!'\n"
                   f"  3. You don't say anything, freezing instead.\n> ").strip().lower()

    if choice in ("1", "one"):
        print('He stomps and puts his hands on his hips, saying, "--"\n')
    elif choice in ("2", "two"):
        print('He gives you an aggressive thumbs up and says, "--"')
    elif choice in ("3", "three"):
        print("Somehow, he gets closer to you and...")
    else:
        print("Sorry, I don't understand that.")


def river_restaurant():
    player_lunch = {
        "kimchi_box": "royal beef bulgogi bento",
        "playa_bowl": "orange power",
        "raisin_canes": "caniac combo",
        "five_guys": "double cheeseburger with a small fry",
        "dwc": "10 traditional wings with buffalo sauce"
    }
    options = {
        "1": "kimchi_box", "one": "kimchi_box",
        "2": "playa_bowl", "two": "playa_bowl",
        "3": "raisin_canes", "three": "raisin_canes",
        "4": "five_guys", "four": "five_guys",
        "5": "dwc", "five": "dwc",
        "6": "union", "six": "union"
    }

    for attempt in range(5):
        restaurant_choice = input("What are you going to choose?\n"
                                  "  1. Kimchi Box\n"
                                  "  2. Playa Bowl\n"
                                  "  3. Raisin' Canes\n"
                                  "  4. Five Guys\n"
                                  "  5. Detroit Wing company\n"
                                  "  6. Walk back to the Union\n> ").strip().lower()

        if restaurant_choice in options:
            if options[restaurant_choice] == "union":
                print("The walk back to the Union is pleasant.\n")
                from locations import union
                union()
            else:
                meal = player_lunch[options[restaurant_choice]]
                print(f"You end up picking {meal}.")
            return
        else:
            print("That's not a valid choice. Try again!\n")


def eat_riv():
    choice = input("Are you in the mood to eat? Type 'yes' or 'no'\n> ").lower()
    if choice in ("yes", "y"):
        print("You think about the wonderful restaurants along Grand River.\n")
        river_restaurant()


def breslinch1():
    paper_topic = game_state["paper_topic"]
    choice = input("What do you say?\n"
                   "  1. 'I really need to head back to the library.'\n"
                   "  2. 'What events are happening?'\n"
                   "  3. 'What do you think I should do?'\n> ").strip().lower()

    if choice in ("1", "one"):
        print("Awwwww, c'mon! The mascot convention only happens once a year!")
    elif choice in ("2", "two"):
        print("Well, there's the mascot café, eating contest, artist alley, mascot panels, meet & greets...")
    elif choice in ("3", "three"):
        print("Otto waits for a response...")