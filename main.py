import time
import os
import sys
from characters import Character as ch
from locations import union, walk_through_greenspace1, library, down_riv, breslin

# Lists of pronouns
pronouns_female = ["she", "her", "hers"]
pronouns_male = ["he", "him", "his"]
pronouns_nonbinary = ["they", "them", "theirs"]

def quit_program(prompt):
    answer = input(prompt).lower()

    if answer == "quit":
        if input("Are you sure? (yes/no) ").lower() == "yes":
            print("\nGoodbye!")
            exit()
        else:
            return quit_program(prompt)

    return answer

def greet():
    print("Welcome to Mascot Dating Simulator!")
    user_name = input("What is your name? ")
    #this is dev stuff. If 1 is entered, the dev should be able to get to any part of the game. theoretically.
    """
    if user_name == '1'  :      
        print(locations)        
        
    """

    print("Hello, " + user_name + "!")
    user_input_gender = input("What is your gender? ").strip().lower()

    if user_input_gender in ("female", "f"):
        user_input_gender_save = "female"
        user_gender = pronouns_female
    elif user_input_gender in ("male", "m"):
        user_input_gender_save = "male"
        user_gender = pronouns_male
    elif user_input_gender in ("none", "nonbinary", "nb"):
        user_input_gender_save = "nonbinary"
        user_gender = pronouns_nonbinary
    else:
        print("Gender not recognized, defaulting to neutral pronouns.")
        user_input_gender_save = "nonbinary"
        user_gender = pronouns_nonbinary

    user_age = int(input("How old are you? "))

    print(f"So your name is {user_name}, your gender is {user_input_gender_save}, and you are {user_age} years old.")
    input("Press enter to continue...")

    return user_name,user_input_gender, user_input_gender_save, user_gender, user_age


def save(user_name, user_input_gender,user_input_gender_save, user_gender, user_age):
    relative_directory = "Saves"
    os.makedirs(relative_directory, exist_ok=True)
    filename = f"{user_name}.txt"
    full_path = os.path.join(relative_directory, filename)

    with open(full_path, "a") as f:
        f.write(f"This user's name is {user_name}.\n")
        f.write(f"This user's gender is {user_input_gender_save}.\n")
        f.write(f"This user's pronouns are {user_gender}.\n")
        f.write(f"This user is {user_age} years old.\n")

    print(f"User inputs saved to {full_path}!")

def meet_the_bas(character,):
    #this should be the introduction function for whenever the
    #user needs a refresh on who someone is.

    #or if there's a way to use it in the
    # story, that's where it will be used
    print("Hi! I'm {ch.name}. I'm from {ch.location} and I work at {ch.job}.")




def intro():
    print("It's a wonderful, sunny day and you have decided to take a walk around campus before going to the library to study.\n"
          "The 1 bus is strangely full...\n"
          "You get off the bus at Abbot and GR...")
    while True:
        choice =input("Do you want to go to the Union?\n Type 'yes' or 'no'.\n").lower()
        if choice == "yes" or "y":
            union()
            break
        elif choice == "no" or "n":
            print("What would you like to do?"
                  "\n1. Go through the greenspace."
                  "\n2. Go down Grand River.")
            choice = input("\nType 1 or 2.\n")
            if choice == "1":
                walk_through_greenspace1()
                break
            elif choice == "2":
                down_riv()
                break
            else:
                print("What? Sorry, I didn't get that.")
        else:
            print("What? Sorry, I didn't get that.")




    """print("Once you cross the Red Cedar, you begin to notice a lot of people walking around!"
          "There must be an event at the {location.breslin}! ")"""

#--------start the game


user_name, user_input_gender, user_input_gender_save, user_gender, user_age = greet()
save(user_name, user_input_gender, user_input_gender_save, user_gender, user_age)
"""
there's a mascot convention in EL and you just so happen to be
a student at MSU. You need to run errands near breslin or whatever
convention center it is at and you run into all of these mascots
looking for love <3.
"""
quit_program(quit)
intro()


