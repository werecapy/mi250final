



from dialogue import dialogue_node
from game_state import game_state
from player_choice_functions import dating_show_choices

# ============ CALLBACK FUNCTIONS ============
# These are called when dialogue ends


# ============ WRAPPER FUNCTIONS ============
#These functions belong here, but are imported to other places
player_name =game_state.get("player_name")
def start_show():
    emcee_start.display()
def emcee_name_line():
    #seperate because of the called game_state
    return f"'It's uh, um, {game_state['player_name']}'"
def emcee_line2():
    return f"'{game_state['player_name']}, a wonderful name! So here's how this is going to work: you'll get to talk to three mascots today and possibly go home with some phone numbers. We asked them 3 questions and they've prepared some pretty interesting responses. Are you ready?'"



def read_lines(mascot):
    filename=f"{mascot}.txt"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
def read_tereesa():
    game_state["tereesa_talk"] = True
    read_lines("tereesa")
def readsparty():
    game_state['sparty_talk'] = True
    read_lines("sparty")
def readbrutus():
    game_state['brutus_talk'] = True
    read_lines("brutus")

def dating_show_choose():
    dating_show_choices()


#---------------EMCEE----------



heck_yeah=dialogue_node(
    "'Great, let's begin! Who would you like to talk to first? Chair one, two, or three?'",
    {
        ('1',"one"):("Press 1 to continue",dating_show_choose)
    }

)

not_really= dialogue_node(
    "'Well it's too late for that kind of negativity! Let's get started!",
    {
        ('1',"one"):("The crowd and loud music drown you out when you protest. You decide to give in because this day has already been so weird.",heck_yeah)
    }
)
intro_emcee=dialogue_node(
    emcee_line2(),
    {
        ('1',"one"): ("Heck yeah I am!",heck_yeah),
        ("2","two"):("Not really...", not_really)
    }

)

emcee_start = dialogue_node(
    "Hello! What was your name again?",
    {
        ('1', 'one'): (emcee_name_line(), intro_emcee)
    }
)



