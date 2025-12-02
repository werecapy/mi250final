# ============ dialogues.py ============
# COMPLETE DIALOGUE TREE - All converted to dialogue_node system
# Imports only what's needed

from dialogue import dialogue_node
from game_state import game_state

# ============ CALLBACK FUNCTIONS ============
# These are called when dialogue ends

def go_to_convention():
    """Player agrees to go to convention"""
    print("You head off to the mascot convention with Sparty!\n")
    from locations import breslin
    breslin()

def go_back_to_library():
    """Player refuses and goes back to study"""
    print("You head back to the library to study.\n")

def freeze_awkwardly():
    """Player freezes awkwardly"""
    print("Sparty looks confused. The awkward silence is deafening.\n")
    print("He shrugs and walks away.\n")

def stay_at_convention():
    """Player stays at convention after Otto's encouragement"""
    print("You decide to stick around and explore more.\n")

def leave_convention():
    """Player leaves convention"""
    print("You head back to the library.\n")

def ignore_mascot():
    """Player ignores the mascot in the garden"""
    print("You pretend the mascot doesn't exist.\n")
    print("It sighs and slowly walks away.\n")

def talk_to_mascot():
    """Player talks to mascot"""
    print("The mascot seems pleased!\n")
    game_state['meet_tereesa'] = True

def take_brochure():
    pass
    #this will have to connect back to player choices or something because the
    # brochure needs to go in the backpack



# ============ WRAPPER FUNCTIONS ============
def player_sparty_ch_1():
    """Called from library()"""
    sparty_start.display()

def player_otto_ch_1():
    """Called from breslin()"""
    otto_start.display()

def player_brutus_ch_1():
    """Called from mascot_cafe()"""
    brutus_start.display()

def player_tereesa_ch_1():
    """Called from sit_in_beal()"""
    tereesa_start.display()

# ============ SPARTY DIALOGUE TREE ============

sparty_response_to_paper = dialogue_node(
    "He stomps and puts his hands on his hips, saying, 'Come onnnnn!'\n",
    {
        ("1", "one"): (
            "'I know, I know, but it's 20% of my grade! If I don't do it, I'm screwed!'",
            go_back_to_library
        ),
        ("2", "two"): (
            "'Maybe I can take a break for today.'",
            go_to_convention
        ),
        ("3", "three"): (
            "'C'mon Sparty, you know I would go if I could!'",
            go_back_to_library
        ),
    }
)

sparty_response_to_excitement = dialogue_node(
    "He gives you an aggressive thumbs up, '-.'\n",
    {
        ("1", "one"): (
            "'I know, I'll get my paper done later.'",
            go_to_convention
        ),
        ("2", "two"): (
            "'Of course I would go to the convention for you, Sparty!'",
            go_to_convention
        ),
    }
)

sparty_start = dialogue_node(
    "Sparty taps the flyer aggressively and points to himself.\nWhat do you say?",
    {
        ("1", "one"): (
            "'Sorry Sparty, but I have to go write a 10 page paper.'",
            sparty_response_to_paper
        ),
        ("2", "two"): (
            "'You know, I should be working on my paper, but this seems a lot more exciting!'",
            sparty_response_to_excitement
        ),
        ("3", "three"): (
            "You don't say anything, freezing instead.",
            freeze_awkwardly
        ),
    }
)


# ============ OTTO DIALOGUE TREE ============

otto_ask_activities = dialogue_node(
    "Otto grins. 'There's a lot to do! We have:'\n'1. The mascot café'\n'2. An eating contest'\n'3. Artist alley with vendors'\n'4. Mascot panels'\n'5. Meet & greets'\n\nWhich interests you?",
    {
        ("1", "one"): ("'The mascot café'", stay_at_convention),
        ("2", "two"): ("'The eating contest'", stay_at_convention),
        ("3", "three"): ("'Artist alley'", stay_at_convention),
        ("4", "four"): ("'The mascot panels'", stay_at_convention),
        ("5", "five"): ("'The meet & greets'", stay_at_convention),
    }
)

otto_response_to_no = dialogue_node(
    "'Awwww, c'mon! The mascot convention only happens once a year!'\n",
    {
        ("1", "one"): (
            "'Well, now that I'm here, mascots really aren't my thing. Sorry Otto.'",
            leave_convention
        ),
        ("2", "two"): (
            "'Otto, I really have to go work on my paper. It's pretty important.'",
            leave_convention
        ),
    }
)

otto_start = dialogue_node(
    "'Hi, I'm Otto! Have you been to any of the events yet?'\n",
    {
        ("1", "one"): (
            "'Not yet, what do you recommend?'",
            otto_ask_activities
        ),
        ("2", "two"): (
            "'I've seen some things, but not everything.'",
            otto_ask_activities
        ),
        ("3", "three"): (
            "'You know what? I've seen enough. I really need to head back.'",
            otto_response_to_no
        ),
    }
)


# ============ BRUTUS DIALOGUE TREE ============

brutus_start = dialogue_node(
    "'Hi, I'm Brutus. I'll be taking care of you today. What can I get you?'\n",
    {
        ("1", "one"): ("'.'", None),
        ("2", "two"): ("'.'", None),
        ("3", "three"): ("'.'", None),
    }
)


# ============ TEREESA (GARDEN MASCOT) DIALOGUE TREE ============
redirect = dialogue_node(
    "'I'm supposed to give this to you,' she says while sliding a paper toward you on the bench.\n",
    { ("1", "one"): (
        "You're not thrilled someone is giving you a piece of paper. 'Thanks,' you say, taking the paper.",
    )}
)
prune_yourself = dialogue_node(
    "'Wow... that can be surprisingly deep if you think about it long enough.'\n",
    { ("1", "one"): (
        "'Yeah, I guess it can. Anyway, was there a reason you were hiding?'",
            None),
    ("2", "two"): ("'Let's not get too deep into that, I need to go to the library.'",
                   None),
    ('3', 'three'): ("You both stare at eachother for a minute before Tereesa breaks the silence.",redirect)




},
)

shuffling = dialogue_node(
    "'Ugh, I knew I should have pruned those extra branches!' She begins to try and tame the wildness.",
{("1","one"):(
        "'I think if you pruned brances, then you would look even more out of place.'",
            None ),
        ("2", "two"): (
        "'You good amazing just the way you are, don't prune yourself to fit in.'",
            prune_yourself)
 },


)
watched = dialogue_node(
    "Well I suppose there's nothing I could have done about that\n",
    {('1','one'):(
    "'No, not really. Is there any reason you're trying to hide out in public?'",
        NEXT DIALOGUES
),
    ("2", "two"): (
        "'INSERT'",
                   NEXT DIALOGUES
                   ),

 }

)
gave_away = dialogue_node(
    "What gave me away?\n",
    {("1", "one"): (
        "'You're not tall enough to be a real tree.' The mascot "
                "doesn't look anything like the other trees around.",
                    NEXT DIALOGUES),
    ("2", "two"): (
        "'I could hear you shuffling.'",
                   shuffling
                   ),
     ("3", "three"): (
         "I felt like I was being watched.",
         watched
     )

 }

    )
blew_cover = dialogue_node(
    "So I blew my own cover again, that really sucks!",
    {("1", "one"): (
    '\'It\'s okay, you tried your best.\'',
                NEXT DIALOGUES)
    ,
    ("2", "two"): ("'You were trying to be covert?'",
                   NEXT DIALOGUES
                   ),
    ("3", "three"): (
            "What are you doing?",
            NEXT DIALOGUES
        ),
}
    )

tereesa_start = dialogue_node(
    "It jumps back in surprise! 'Darn it! You noticed me!'\n",
    {
        ("1", "one"): (
            "'Um, yeah I noticed.' It was incredibly obvious.",
            gave_away
        ),
        ("2", "two"): (
            "'No I didn't! Not until you said something. I don't have my glasses on.'",
            blew_cover
        ),
        ("3", "three"): (
            "You totally ignore it. Maybe it will go away.",
            ignore_mascot
        ),
    }
)


