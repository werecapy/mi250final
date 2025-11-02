from player_info import backpack
import random

#list of locations for saves
#list of paper topics
paper_topic_list = ['sleep disorders',
                    'nuclear power',
                    "social media interaction",
                    'book bans']


def union():
    print("The union is as busy as ever!\n"
          "Every table has as at least one student sitting at it."
          "Passing through the Sparty's, you think about getting a combo.")
    combo_choice = input("Would you like to get combo?\n "
                         "Type yes or no:\n ")
    if combo_choice == "yes":
        print("Everything looks too good!\n"
              "What are you in the mood for?\n"
              "1. A Woody's burrito, energy drink, and a bag of chips\n"
              "2. An instant ramen, a juice, and a cup of fruit\n"
              "3. A protein drink, a bottle of water, and a small bag of trail mix\n"
              "4. Maybe you're not hungry after all.")


    else:
        print("Ultimately, you decide to pass on a delicious combo.")

def paper_topic_choice():
    global paper_topic_list
    if random.random() < 0.5:

        new_topic = input("What is your paper on?")
        paper_topic_list.append(new_topic)
        paper_topic=new_topic
    else:
        paper_topic = random.choice(paper_topic_list)
        print(f"Oh, that's right! It was {paper_topic}!")


def walk_through_greenspace1():
    print("Wow, it *really* is a great day! There's a perfect amount of cloud cover"
          "and a light enough breeze to not feel too chilly. Squirrels are bounding about,\n"
          "living their best furry lives. You get jealous of them because you think about\n"
          f"the 10 page paper you have to complete before next week about... what was it again?\n")
    paper_topic_choice()
    input("Press enter to continue...")
    print("Walking through the green space, you finally get to the front of the library."
          "")




def down_riv():
    pass