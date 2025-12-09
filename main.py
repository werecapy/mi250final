

from validation import run_all_validations, print_validation_results

from tkinter import *
import sys




# Run silent validation first
print("Initializing game...", end=" ", flush=True)
validation_errors = run_all_validations(verbose=False)

if not print_validation_results(validation_errors):
    exit(1)

# Only continue if validation passed
# main.py CAN import from other modules
import time
import os

from locations import union, walk_through_greenspace1, down_riv
from game_state import set_player_data, set_paper_topic, game_state

pronouns_female = ["she", "her", "hers"]
pronouns_male = ["he", "him", "his"]
pronouns_nonbinary = ["they", "them", "theirs"]


def quit_program(prompt):
    #Allows player to quit program
    choice = input(prompt).lower()
    if choice == "quit":
        if input("Are you sure? (yes/no) ").lower() == "yes":
            print("\nGoodbye!")
            thanks()
        else:
            return quit_program(prompt)
    return choice


def greet():
    #Starts game, greets player, and asks for info

    print("="*50)
    print("Welcome to Mascot Dating Simulator!\n")
    print("=" * 50)
    user_name = input("What is your name? ")
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

    return user_name, user_input_gender_save, user_gender, user_age


def save(user_name, user_input_gender_save, user_gender, user_age):
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


def intro():
    print(
        "It's a wonderful, sunny day and you have decided to take a walk around campus before going to the library to study.\n"
        "The 1 bus is strangely full...\n"
        "You get off the bus at Abbot and GR...\n")

    while True:
        choice = input("Do you want to go to the Union?\nType 'yes' or 'no'.\n> ").lower()
        if choice in ("yes", "y"):
            union()
            break
        elif choice in ("no", "n"):
            print("What would you like to do?"
                  "\n1. Go through the greenspace."
                  "\n2. Go down Grand River.")
            choice = input("\nType 1 or 2.\n> ").strip()
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

def thanks():

    print("Thanks for playing!")
    time.sleep(9)
    return


greet()
thanks()
if __name__ == "__main__":


    user_name, user_input_gender_save, user_gender, user_age = greet()
    save(user_name, user_input_gender_save, user_gender, user_age)

    # Store player data in shared state
    set_player_data(user_name, user_input_gender_save, user_gender, user_age)




