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
    choice=input("What do you say?\n "
                      f"    1. 'Sorry Sparty, but I have to go write a 10 page paper on {paper_topic}.'"
                      "     2. 'You know, I should be working on my paper, but this seems a lot more exciting!'\n"
                      "     3. You don't say anything, freezing, instead. \n").strip().lower()
    if choice == "1" or choice == "one":
        print('He stomps and puts his hands on his hips, saying, "--"\n')
        choice = input("What do you say?\n "
                           "    1. 'I know, I know, but it's 20% of my grade! If I don't do it, I'm screwed!'\n"
                           "    2. 'Maybe I can take a break for today.'\n"
                           "    3. 'C'mon Sparty, you know I would go if I could!'\n").strip().lower()

    if choice == "2" or choice == "two":

        print('He gives you an aggressive thumbs up and says, "--"')
        choice = input("What do you say?\n "
                           "    1. 'I know, I'll get my paper on {paper_topic} done later.'\n"
                           "    2. 'Of course I would go to the convention for you, Sparty!'\n"
                           "    3. ''").strip().lower()
    if choice == "3" or choice == "three":
        print("Somehow, he gets closer to you and add more here")
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

def mascot_cafe():
    pass
def eating_contest():
    pass
def artist_alley():
    pass
def mascot_panels():
    pass
def meet_n_greets():
    pass

def breslinch1(paper_topic):
    choice = input("What do you say?\n"
                        "   1. 'You know what? I've seen enough, I really need to "
                        "head back to the library.'\n"
                        "   2. 'I've seen some things, but not everything."
                        "What are some of the events happening?'\n"
                        "   3. 'What do you think I should do?'")
    if choice == "1":
        print("Awwwww, c'mon! The mascot convention only happens once a year!")
        choice = input("What do you say?\n"
                       "    1. 'Well, now that I'm here, I can see mascots really aren't my thing. Sorry Otto.'\n"
                       f"    2. 'Otto, I really have to go work on my paper. It's about {paper_topic}, a really difficult topic'\n"
                       "    3. \n"
                       "    1.\n")
    elif choice == "2":
            print("Well, there's the mascot café, eating contest, artist alley, mascot panels, meet & greets,"
                  "")
            choice = input("Which do you choose?\n"
                           "    1. The mascot café\n"
                           "    2. The eating contest\n"
                           "    3. The artist alley\n"
                           "    4. The mascot panels\n "
                           "    5. The meet & greets\n")
            if choice == "1":
                 mascot_cafe()
            elif choice == "2":
                eating_contest()
            elif choice == "3":
                artist_alley()
            elif choice == "4":
                mascot_panels()
            elif choice == "5":
                meet_n_greets()

    elif choice == "3":
        pass

