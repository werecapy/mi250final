# Can import game_state, but NOT main.py
import random
from game_state import game_state, purchase_combo, purchase_meal

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
    """Restaurant choice function - similar structure to player_combo"""

    restaurant_options = {
        "1": ("royal beef bulgogi bento", "kimchi_box"),
        "one": ("royal beef bulgogi bento", "kimchi_box"),
        "2": ("orange power", "playa_bowl"),
        "two": ("orange power", "playa_bowl"),
        "3": ("caniac combo", "raisin_canes"),
        "three": ("caniac combo", "raisin_canes"),
        "4": ("double cheeseburger with a small fry", "five_guys"),
        "four": ("double cheeseburger with a small fry", "five_guys"),
        "5": ("10 traditional wings with buffalo sauce", "dwc"),
        "five": ("10 traditional wings with buffalo sauce", "dwc"),
        "6": (None, "union"),
        "six": (None, "union")
    }

    for attempt in range(5):
        restaurant_choice = input("What are you going to choose?\n"
                                  "  1. Kimchi Box\n"
                                  "  2. Playa Bowl\n"
                                  "  3. Raisin' Canes\n"
                                  "  4. Five Guys\n"
                                  "  5. Detroit Wing company\n"
                                  "  6. Walk back to the Union\n> ").strip().lower()

        if restaurant_choice in restaurant_options:
            meal_text, restaurant_id = restaurant_options[restaurant_choice]

            # Check if they want to go back to union
            if restaurant_id == "union":
                print("The walk back to the Union is pleasant.\n")
                from locations import union
                union()
                return

            # Otherwise they purchased a meal
            else:
                print(f"There are so many great choices on this menu, it's hard to pick just one!\n"
                      f"You end up picking {meal_text}.\n")
                purchase_meal(restaurant_id, meal_text)
                return

        else:
            print("Sorry, I don't understand that. Try again.\n")

    # If they didn't choose after 5 attempts
    print("You couldn't decide and left the restaurant.")


def eat_riv():
    """Wrapper function to ask if player wants to eat"""
    choice = input("Are you in the mood to eat? Type 'yes' or 'no'\n> ").lower()
    if choice in ("yes", "y"):
        print("You think about the wonderful restaurants along Grand River.\n")
        river_restaurant()
    else:
        print("You decide not to eat and continue on.\n")
def sticker_booth():
    if game_state['meet_sparty'] and game_state['meet_otto'] == True:
    #make some game save logic for if the player has and has not met certain mascots
        print("A few dozen boxes of stickers lay before you on the vendor's table. "
          "You only recognize Sparty and Otto by name, but the other stickers look pretty cool too."
          "")

    elif game_state['meet_sparty'] == True and game_state['meet_otto'] == False:
        print("A few dozen boxes of stickers lay before you on the vendor's table. "
              "You only recognize Sparty.")
    #add the rest of the mascots to this logic

    choice = input("Would you like to buy a sticker? Type 'yes' or 'no'\n")
    if choice ==("yes", "y"):
        game_state["get_stickers"] = True
        #maybe add some turtle logic here? let the player see the stickers

def mascot_cafe():
    game_state["meet_brutus"] = True
    print("Wandering over to the mascot cafe, it looks just as busy"
          "as the rest of the convention. People are sitting at tables and being"
          "waited on by mascots that you don't know.\n"
          "Upon sitting down, a mascot comes up to you.\n"
          "'Hi, I'm Brutus. I'll be taking care of you today. what can I get you?")
def eating_contest():
    print("When you get to the stall you can't help but notice CONTINUE")

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
                       "    4.\n")
        if choice == "1":
            pass
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
            if game_state["combo_purchase"] == True:
               print("You already have food in your bag...")
            eating_contest()
        elif choice == "3":
            artist_alley()
        elif choice == "4":
            mascot_panels()
        elif choice == "5":
            meet_n_greets()

    elif choice == "3":
        pass

