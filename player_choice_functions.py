import random
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
    combo_choice = input("Would you like to get combo?\n "
                         "Type yes or no:\n ")
    if combo_choice == "yes" or combo_choice == "y":
        print("Everything looks too good!\n")
        combo_combo = input("What are you in the mood for?\n"
                            "     1. A Woody's burrito, energy drink, and a bag of chips\n"
                            "     2. An instant ramen, a juice, and a cup of fruit\n"
                            "     3. A protein drink, a bottle of water, and a small bag of trail mix\n"
                            "     4. Maybe you're not hungry after all.")
        if combo_combo == "1" or combo_combo == "one":
            # add object(s) to the backpack
            print("You gather your items and bring them up to the cashier.\n"
                  "They were super nice and it was a quick transaction.\n"
                  "Onward! (Press enter to continue)")
        if combo_combo == "2" or combo_combo == "two":
            # add object(s) to the backpack
            print("You gather your items and bring them up to the cashier.\n"
                  "They were super nice and it was a quick transaction.\n"
                  "Onward! (Press enter to continue)")
        if combo_combo == "3" or combo_combo == "three":
            # add object(s) to the backpack
            print("You gather your items and bring them up to the cashier.\n"
                  "They were super nice and it was a quick transaction.\n"
                  "Onward! (Press enter to continue)")
        if combo_combo == "4" or combo_combo == "four":
            # add object(s) to the backpack
            print("You gather your items and bring them up to the cashier.\n"
                  "They were super nice and it was a quick transaction.\n"
                  "Onward! (Press enter to continue)")
        else:
            print("Sorry, I don't understand that.")
    else:
        print("Ultimately, you decide to pass on a delicious combo.")


def player_sparty_ch_1():
    sparty_ch_1=input("What do you say?\n "
                      f"1. 'Sorry Sparty, but I have to go write a 10 page paper on {paper_topic}.'"
                      "2. 'You know, I should be working on my paper, but this seems a lot more exciting!'\n"
                      "3. You don't say anything, freezing, instead. \n").strip().lower()
    if sparty_ch_1 == "1" or sparty_ch_1 == "one":
        pass
    if sparty_ch_1 == "2" or sparty_ch_1 == "two":
        pass
    if sparty_ch_1 == "3" or sparty_ch_1 == "three":
        print("Somehow, he gets closer to you and add more here")
    else:
        print("Sorry, I don't understand that.")