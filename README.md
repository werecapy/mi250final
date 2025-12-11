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
## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
