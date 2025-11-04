import random

from locations import union
from player_info import backpack

global paper_topic
#list of paper topics to choose from
paper_topic_list = ['sleep disorders',
                    'nuclear power',
                    "social media interaction",
                    'book bans']


#this is the paper topic chooser function
def paper_topic_choice():
    global paper_topic_list

    if random.random() < 0.5:

        new_topic = input("What is your paper on?")
        paper_topic_list.append(new_topic)
        paper_topic=new_topic
    else:
        paper_topic = random.choice(paper_topic_list)
        print(f"Oh, that's right! It was {paper_topic}!")


#this is the first combo
def player_combo():
    combo_options = {
        "1":"A Woody's burrito, energy drink, and a bag of chips",'one':"A Woody's burrito, energy drink, and a bag of chips",
        '2': 'An instant ramen, a juice, and a cup of fruit', 'two':'An instant ramen, a juice, and a cup of fruit',
        '3': 'A protein drink, a bottle of water, and a small bag of trail mix','three':'A protein drink, a bottle of water, and a small bag of trail mix',
        '4': "Maybe you're not hungry after all.",'four': "Maybe you're not hungry after all."
    }
    combo_choice = input("Would you like to get combo?\n "
                         "Type yes or no:\n ")
    if combo_choice == "yes" or combo_choice == "y":
        print("Everything looks too good!\n")
        for attempt in range(3):
            combo_combo = input("What are you in the mood for?\n"
                            "     1. A Woody's burrito, energy drink, and a bag of chips\n"
                            "     2. An instant ramen, a juice, and a cup of fruit\n"
                            "     3. A protein drink, a bottle of water, and a small bag of trail mix\n"
                            "     4. Maybe you're not hungry after all.")

            if combo_options == "4" or combo_combo == "four":
                print("Ultimately, you decide to pass on a delicious combo.")
            else:
                combo = combo_options[combo_combo]
                # add object(s) to the backpack
                print(f"You gather your items: ({combo}), and bring them up to the cashier.\n"
                      "They were super nice and it was a quick transaction.\n"
                      "Onward! (Press enter to continue)")
                combo.split(",")
                backpack.append(combo) # make sure the combo variable is split into 3 separate items when put into the backpack

        else:
            print("Sorry, I don't understand that. Try again.")
    else:
        print("Ultimately, you decide to pass on a delicious combo.")



def player_sparty_ch_1():
    sparty_ch_1=input("What do you say?\n "
                      f"    1. 'Sorry Sparty, but I have to go write a 10 page paper on {paper_topic}.'"
                      "     2. 'You know, I should be working on my paper, but this seems a lot more exciting!'\n"
                      "     3. You don't say anything, freezing, instead. \n").strip().lower()
    if sparty_ch_1 == "1" or sparty_ch_1 == "one":
        print('He stomps and puts his hands on his hips, saying, "--"\n')
        sparty_ch2 = input("What do you say?\n "
                           "    1. 'I know, I know, but it's 20% of my grade! If I don't do it, I'm screwed!'\n"
                           "    2. 'Maybe I can take a break for today.'\n"
                           "    3. 'C'mon Sparty, you know I would go if I could!'\n").strip().lower()

    if sparty_ch_1 == "2" or sparty_ch_1 == "two":
        print('He gives you an aggressive thumbs up and says, "--"')
        sparty_ch3 = input("What do you say?\n "
                           "    1. 'I know, I'll get my paper on {paper_topic} done later.'\n"
                           "    2. 'Of course I would go to the convention for you, Sparty!'\n"
                           "    3. ''").strip().lower()
    if sparty_ch_1 == "3" or sparty_ch_1 == "three":
        print("Somehow, he gets closer to you and add more here")
    else:
        print("Sorry, I don't understand that.")

def river_restaurant():
    player_lunch= {
        "kimchi_box" : "royal beef bulgogi bento",
        "playa_bowl" : "orange power",
        "raisin_canes" : "caniac combo",
        "five_guys" : "double cheeseburger with a small fry",
        "dwc" : "10 traditional wings with buffalo sauce"

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
                                  "     1. Kimchi Box\n"
                                  "     2. Playa Bowl\n"
                                  "     3. Raisin' Canes\n"
                                  "     4. Five Guys\n"
                                  "     5. Detroit Wing company\n"
                                  "     6. Walk back the the Union, a combo sounds like a much better idea./n"
                                  ).strip().lower()
        if restaurant_choice in options:
            if options[restaurant_choice] == "union":
                print("The walk back to the Union is pleasant.\n")
                union()
            else:
                meal = player_lunch[options[restaurant_choice]]
                print(f"There are so many great choices on this menu, it's hard to pick just one!\n"
                      f"You end up picking {meal}.")
        else:
            print("That’s not a valid choice. Try again!\n")


        















        
        
        

def eat_riv():
    eat_river= input("Are you in the mood to eat?")
    if eat_river == "yes" or eat_river == "y":
        print("You think about the wonderful restaurants along Grand River.\n")
    river_restaurant()