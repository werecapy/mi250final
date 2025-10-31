import time
import os

# Lists of pronouns
pronouns_female = ["she", "her", "hers"]
pronouns_male = ["he", "him", "his"]
pronouns_nonbinary = ["they", "them", "theirs"]

def greet():
    print("Welcome to Mascot Dating Simulator!")
    name = input("What is your name? ")
    print("Hello, " + name + "!")
    gender = input("What is your gender? ").strip().lower()

    if gender in ("female", "f"):
        user_gender = pronouns_female
    elif gender in ("male", "m"):
        user_gender = pronouns_male
    elif gender in ("none", "nonbinary", "nb"):
        user_gender = pronouns_nonbinary
    else:
        print("Gender not recognized, defaulting to neutral pronouns.")
        user_gender = pronouns_nonbinary

    user_age = int(input("How old are you? "))

    print(f"So your name is {name}, your gender is {user_gender}, and you are {user_age} years old.")
    input("Press enter to continue...")

    return name, gender, user_gender, user_age

def save(name, gender, user_gender, user_age):
    relative_directory = "Saves"
    os.makedirs(relative_directory, exist_ok=True)
    filename = f"{name}.txt"
    full_path = os.path.join(relative_directory, filename)

    with open(full_path, "a") as f:
        f.write(f"This user's name is {name}.\n")
        f.write(f"This user's gender is {gender}.\n")
        f.write(f"This user's pronouns are {user_gender}.\n")
        f.write(f"This user is {user_age} years old.\n")

    print(f"User inputs saved to {full_path}")

# Run the game
name, gender, user_gender, user_age = greet()
save(name, gender, user_gender, user_age)
