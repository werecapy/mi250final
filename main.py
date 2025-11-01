import time
import os
from characters import Character as ch

# Lists of pronouns
pronouns_female = ["she", "her", "hers"]
pronouns_male = ["he", "him", "his"]
pronouns_nonbinary = ["they", "them", "theirs"]

def greet():
    print("Welcome to Mascot Dating Simulator!")
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

def meet_the_bas(self):
    #this should be the introduction function for whenever the
    #user needs a refresh on who someone is.
    pass




#--------start the game


user_name, user_input_gender, user_input_gender_save, user_gender, user_age = greet()
save(user_name, user_input_gender, user_input_gender_save, user_gender, user_age)
"""
there's a mascot convention in EL and you just so happen to be
a student at MSU. You need to run errands near breslin or whatever
convention center it is at and you run into all of these mascots
looking for love <3.
"""


