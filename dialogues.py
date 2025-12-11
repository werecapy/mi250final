# ============ dialogues.py (FIXED) ============



from dialogue import dialogue_node
from game_state import game_state



# ============ CALLBACK FUNCTIONS ============
# These are called when dialogue ends

def go_to_convention():
    """Player agrees to go to convention"""
    print("You head off to the mascot convention!\n")
    from locations import breslin
    breslin()

def write_paper(paper_topic=game_state["paper_topic"]):
    """Player sits down to write the paper"""
    go_back_to_library(paper_topic)
    import random
    hours = random.randint(1, 5)
    breaks = random.randint(1, 5)
    print(f"The space is clean and quiet. While it does"
          f" take a while, you bang out your paper in "
          f"{hours} hours and take {breaks} breaks. The"
          f"walk back feels glorious and the playlist "
          f"in your headphones lifts your spirits.\n")

def go_back_to_library(paper_topic=game_state["paper_topic"]):
    """Player refuses and goes back to study"""
    print(f"You head back to the library to write paper on {paper_topic}. The fourth floor is pretty quiet and you find a space quite easily.\n")
    choice = input("Would you like to see if the convention is still going on? Type 'yes' or 'no'.\n")
    if choice == 'yes':

        print("Miraculously, the convention is still going on! You can't believe your luck.")
        go_to_convention()
    else:
        print("You head back to your apartment after a long homework session. It wasn't fun, but you got all of your homework done for the next two weeks!"
              "You treat yourself to some takeout and call it a night.")
def stay_at_convention():
    """Player stays at convention after Otto's encouragement"""
    print("You decide to stick around and explore more.\n")

def leave_convention():
    """Player leaves convention"""
    print("You head back to the library to work on your paper. You don't finish it, but you make great progress!\n")

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

def pamph():
    from inventory_screen import pamphlet_vis
    pamphlet_vis()
def go_to_dating_show():

    from locations import mascot_panels
    #Still gritty talking
    print("'Now hold on to your horses, I think you need to come with me to the mascot panel I'm about to be in. It'll be great!\n"
          "He drags you with him as he walks to the panels. You can't begin to emagine the ")
    mascot_panels()

def different_activity():
    from player_choice_functions import convention_activities
    convention_activities()

# ============ WRAPPER FUNCTIONS ============
#These functions belong here, but are imported to other places
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

def player_gritty_ch_1():
    """Called from artist_alley"""
    gritty_start.display()
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
    "He gives you an aggressive thumbs up, '-.'",
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

blurt_2 = dialogue_node(
    "'Oh my gosh, I don't know why I did that. What you trying to tell me?' You say.",
    {
        ("1", "continue"): ("Press enter to continue...", None)
    }
)

blurt = dialogue_node(
    "'--'",
    {
        ("1", "one"): (
            f"The mascot convention? Sparty, I'd love to, but I have to write a paper on {game_state['paper_topic']}.",
            sparty_response_to_paper
        )
    }
)

taps = dialogue_node(
    "He turns around, giving you his full attention.",
    {
        ("1", "one"): (
            "'Sorry' You blurt, 'I didn't know what to say. Of course I would go to the convention for you, Sparty!'",
            blurt
        ),
        ("2", "two"): (
            "You pull your hand back like you've been burned. 'Oh my gosh, I don't know why I did that. What you trying to tell me?'",
            blurt_2
        )
    }
)

freeze_awkwardly = dialogue_node(
    "The awkward silence is deafening.\nHe shrugs and walks away.\n",
    {
        ("1", "one"): (
            "You find a table on the fourth floor.",
            write_paper
        ),
        ("2", "two"): (
            "You rush after him, tapping him on the shoulder",
            taps
        )
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
        ("3", "three"): (
            "'Maybe I should stick around.' Seeing everyone else here is making you more excited by the second. 'What is there to do around here?'",
            otto_ask_activities
        )
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
        ("1", "one"): ("'Can I get a water?'", None),
        ("2", "two"): ("'I'd like a pop, please.'", None),
        ("3", "three"): ("'.'", None),
    }
)


# ============ TEREESA (GARDEN MASCOT) DIALOGUE TREE ============

pamphlet = dialogue_node(
    "not finished, should show player pamphlet and let the player react to it.",
    {
        ("1", "one"): ("pass", pamph)
    }
)

redirect = dialogue_node(
    "'I'm supposed to give this to you,' she says while sliding a paper toward you on the bench.\n",
    {
        ("1", "one"): (
            "You're not thrilled someone is giving you a piece of paper. 'Thanks,' you say, taking the paper.",
            None
        ),
        ("2", "two"): (
            "You take the paper, looking it over. It's for a mascot convention?",
            pamphlet
        )
    }
)

prune_yourself = dialogue_node(
    "'Wow... that can be surprisingly deep if you think about it long enough.'\n",
    {
        ("1", "one"): (
            "'Yeah, I guess it can. Anyway, was there a reason you were hiding?'",
            None
        ),
        ("2", "two"): (
            "'Let's not get too deep into that, I need to go to the library.'",
            None
        ),
        ("3", "three"): (
            "You both stare at each other for a minute before Tereesa breaks the silence.",
            redirect
        )
    }
)

shuffling = dialogue_node(
    "'Ugh, I knew I should have pruned those extra branches!' She begins to try and tame the wildness.",
    {
        ("1", "one"): (
            "'I think if you pruned branches, then you would look even more out of place.'",
            None
        ),
        ("2", "two"): (
            "'You look amazing just the way you are, don't prune yourself to fit in.'",
            prune_yourself
        )
    }
)

watched = dialogue_node(
    "Well I suppose there's nothing I could have done about that\n",
    {
        ("1", "one"): (
            "'No, not really. Is there any reason you're trying to hide out in public?'",
            pamphlet
        ),
        ("2", "two"): (
            "'INSERT'",
            None
        )
    }
)

gave_away = dialogue_node(
    "What gave me away?\n",
    {
        ("1", "one"): (
            "'You're not tall enough to be a real tree.' The mascot doesn't look anything like the other trees around.",
            None
        ),
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
    "'So I blew my own cover again, that really sucks!'",
    {
        ("1", "one"): (
            "'It's okay, you tried your best.'",
            None
        ),
        ("2", "two"): (
            "'You were trying to be covert?'",
            None
        ),
        ("3", "three"): (
            "What are you doing?",
            None
        )
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

# ============ gritty DIALOGUE TREE ============

need_curtain = dialogue_node(
    "'It's really nothing worth looking at, you should check out the other activities.' His eyes are telling you that he doesn't want you behind the curtain, so maybe it's for the best if you don't.",
    {
        ("1", "one"): ("'I'll go check out the other activities, I guess,' you reply.",different_activity())
    }

)



before_show =dialogue_node(

        "'Now hold on to your horses,' he says.' I think you need to come with me to the mascot panel I'm about to be in. It'll be great!\n"
        "He drags you with him as he walks to the panels. You can't begin to imagine what is about to happen.",
    {
        ("1", 'one'):("You let him drag you to the panels. It might be fun!",go_to_dating_show())
    }
)
look_lost = dialogue_node(
    "'Well the only way not to fit in here is to look lost. Just try to have some fun and you'll totally forget it's your first time!'",
{
    ("1", "one"): ("That was pretty deep. He walks away before you can manage to get his name. His retreating fuzzy form melts into the crowd.",different_activity())
}
)
weird_guy=dialogue_node(
    "Hey! Didn't anyone ever tell you not to ask that at a mascot convention? It looks like your first time, so I'll let it slide...'",
    {
        ("1", "one"): ("You look to the floor with embarrassment. 'I'm glad you noticed, I feel so out of place here.",look_lost),
        ("2", "two"): ("'This convention is getting a bit ridiculous at this point.' You turn to walk off.", before_show)
    }
)
here_and_there = dialogue_node(
    "'They're here and there.' He says,' I gotta run, but you should check out the other activities.'",
    {
        ("1", "one"): ("'Ok!'",different_activity())
    }
)
gritty_name= dialogue_node(
    "'The names' gritty! I'm a mascot for the Philly Flyers!'",
    {
        ("1", "one"): ("'Sorry, but what are you?' He looks like a giant monster to you. Maybe there's a type of monster you haven't heard of yet.",weird_guy),
        ("2", "two"): ("You feel wowed. 'A professional league mascot! That's cool. Are any of your friends here?'",here_and_there)
    }
)
curtains= dialogue_node(
    "'There's nothing interesting back there!' He asserts.",
    {
        ("1", "one"): ("'Oh, well... ok. What's your name again?' you ask",gritty_name),
        ("2", "two"): ("Your eyebrow raises. 'Something about you telling me not to go back there is making me *want* to go back there.' He seems really dead set on you *not* going behind the curtain.",need_curtain)
    }
)
gritty_start = dialogue_node(
    "Woah there, partner! Where do you think you're headed? The rest of the convention is over here!'\n"
    "You turn around and see a giant orange monster.",
    {
        ("1", "one"): ("'I was going to check out the curtained area,' you reply.",curtains),
        ("2", "two"):("This mascot is pretty weird. 'What are you supposed to be?' you ask.",weird_guy),
    }
)