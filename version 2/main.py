

from validation import run_all_validations, print_validation_results

from tkinter import *
import sys
from gui import *

from location_gui import *


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
from game_state import  game_state

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


def greet_gui(gui):
    gui.display_text("=" * 50)
    gui.display_text("Welcome to Mascot Dating Simulator!")
    gui.display_text("=" * 50)

    # Step 1: Ask for name
    def on_name_entered(name):
        game_state["player_name"] = name
        gui.display_text(f"Hello, {name}!")

        # Step 2: Ask for gender
        gui.display_text("What is your gender?")
        gui.show_choices({
            "Female": lambda: on_gender_selected("female"),
            "Male": lambda: on_gender_selected("male"),
            "Nonbinary": lambda: on_gender_selected("nonbinary")
        })

    def on_gender_selected(gender):
        # Set pronouns based on gender
        if gender == "female":
            pronouns = ["she", "her", "hers"]
        elif gender == "male":
            pronouns = ["he", "him", "his"]
        else:
            pronouns = ["they", "them", "theirs"]

        game_state["player_gender"] = gender
        game_state["player_pronouns"] = pronouns

        # Step 3: Ask for age
        def on_age_entered(age):
            game_state["player_age"] = int(age)

            # Show summary
            gui.display_text(f"\nSo your name is {game_state['player_name']}, "
                             f"your gender is {gender}, and you are {age} years old.\n")

            # Save and continue
            save_gui(gui)
            intro_gui(gui)

        gui.show_input("How old are you?", on_age_entered)

    gui.show_input("What is your name?", on_name_entered)


def intro_gui(gui):
    gui.display_text(
        "It's a wonderful, sunny day and you have decided to take a walk "
        "around campus before going to the library to study.\n"
        "The 1 bus is strangely full...\n"
        "You get off the bus at Abbot and GR...\n"
    )

    gui.display_text("Do you want to go to the Union?")
    gui.show_choices({
        "Yes, go to the Union": lambda: union_gui(gui),
        "No, go through the greenspace": lambda: walk_through_greenspace1_gui(gui),
        "No, go down Grand River": lambda: down_riv_gui(gui)
    })


def save_gui(gui):
    """Save player data from game_state"""
    user_name = game_state["player_name"]
    user_gender = game_state["player_gender"]
    user_pronouns = game_state["player_pronouns"]
    user_age = game_state["player_age"]

    relative_directory = "Saves"
    os.makedirs(relative_directory, exist_ok=True)
    filename = f"{user_name}.txt"
    full_path = os.path.join(relative_directory, filename)

    with open(full_path, "a") as f:
        f.write(f"This user's name is {user_name}.\n")
        f.write(f"This user's gender is {user_gender}.\n")
        f.write(f"This user's pronouns are {user_pronouns}.\n")
        f.write(f"This user is {user_age} years old.\n")

    gui.display_text(f"✓ Progress saved!\n")


def intro_gui(gui):
    gui.display_text(
        "It's a wonderful, sunny day and you have decided to take a walk "
        "around campus before going to the library to study.\n"
        "The 1 bus is strangely full...\n"
        "You get off the bus at Abbot and GR...\n"
    )

    gui.display_text("Do you want to go to the Union?")
    gui.show_choices({
        "Yes, go to the Union": lambda: union_gui(gui),
        "No, go through the greenspace": lambda: walk_through_greenspace1_gui(gui),
        "No, go down Grand River": lambda: down_riv_gui(gui)
    })

def thanks():

    print("Thanks for playing!")
    time.sleep(9)
    return



if __name__ == "__main__":
    gui = GameGUI()

    gui.run()

    """
    user_name, user_input_gender_save, user_gender, user_age = greet()
    save(user_name, user_input_gender_save, user_gender, user_age)

    # Store player data in shared state
    set_player_data(user_name, user_input_gender_save, user_gender, user_age)
"""



