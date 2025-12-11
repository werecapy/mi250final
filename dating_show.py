



from dialogue import dialogue_node
from game_state import game_state

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
    return f"'{game_state['player_name']}, a wonderful name! So here's how this is going to work: you'll get to talk to five mascots today and possibly go home with some phone numbers. Are you ready?'"

#---------------EMCEE----------



heck_yeah=dialogue_node(
    "'Great, let's begin! Who would you like to talk to first? Chair one, two, or three?'",
    {
        ('1',"one"):("'Um, I'd like to talk to chair number one",None),
        ('2', 'two'):("Let's do chair number two",None),
        ('3', 'three'):("I'll pick chair number three",None),

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
        ("2","two"):("Not really...", None)
    }

)

emcee_start = dialogue_node(
    "Hello! What was your name again?",
    {
        ('1', 'one'): (emcee_name_line(), intro_emcee)
    }
)



