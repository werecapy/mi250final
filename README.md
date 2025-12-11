[# MI250final
# Mascot Dating Simulator

## Description
This is my MI 250 final project. It thought it would be fun to create a mascot dating simulator. Choose to interact with a few of the weird mascots selected for the project and fulfill your dream of speed dating a mascot!



## To run
To run the story part of the simulator, play main.py. For inventory, play inventory_screen. For poster_screen, play poster_screen.py.


## Installation
There should be no external libraries needed to run this game

## Code overview
    -Main.py is responsible for starting, running, saving player info, and quitting.
    -game_state.py is responsible for the different checkpoints in the game. It is a dictionary of checkpoints and has functions to handle the assignment of variables at the different checkpoints.
    -locations.py is responsible for handling the narration, for all the different locations. If a location has a choice to make, it will go to player functions.
    -player_choice_functions is responsible for handling the player choices. Most if not all the choices a player makes will be housed here and imported into another file.
    -dialogue.py is responsible for exclusively handling the logic for dialogue_node class. The class is exported into dialogues and dating show for use. Initally, this looked like one huge file with a bunch of loops like in the CYA in the beginning of the semester, but I was able to get AI to refine it to a class.
    -dialogues.py is responsible for handling the dialogue itself for most of the game.
    -dating_show.py is responsible for handling the rest of the dialouge because dialogues was getting too long.
    -validation.py validates the whole game to make sure it will all run before the player starts. This is entirely generated, however it did save a lot of time play testing.
    -inventory_screen.py is responsible for handling the visual part of the game. It is a visual inventory
    -poster_screen.py is supposed to show the player a poster.
    -Characters.py does not do anything as the scope of this project can only be so large, it was going to be for the mascots.


## Roadmap
I do want to work on this after the class ends...

## Authors and acknowledgment
Thank you, Liv Forte for testing my game.


## Project status
In hibernation, for now.