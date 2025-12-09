# ============ validation.py ============
"""
Silent validation system that checks all components without user seeing it
Run this before the game starts
"""

import sys
import io
from contextlib import redirect_stdout, redirect_stderr

from game_state import set_player_data


def validate_imports():
    """Check if all modules can be imported"""
    errors = []

    modules_to_check = [
        ("game_state", "from game_state import game_state"),
        ("characters", "from characters import Character"),
        ("locations", "from locations import union, walk_through_greenspace1, down_riv, breslin"),
        ("player_choice_functions", "from player_choice_functions import player_combo, paper_topic_choice"),




    ]

    for module_name, import_statement in modules_to_check:
        try:
            exec(import_statement)
        except ImportError as e:
            errors.append(f"❌ {module_name}: {str(e)}")
        except Exception as e:
            errors.append(f"❌ {module_name}: Unexpected error: {str(e)}")

    return errors


def validate_game_state():
    """Check if game_state has all required keys"""
    from game_state import game_state

    required_keys = [
        "player_name",
        "player_gender",
        "player_pronouns",
        "player_age",
        "paper_topic",
        "backpack",
        "meet_sparty",
        "meet_otto",
        "combo_purchase",
        "combo_type",
        "meet_brutus",
        "meal_name"  ,
        "meal_type"  ,
        "meet_tereesa",

    ]

    errors = []
    for key in required_keys:
        if key not in game_state:
            errors.append(f"❌ Missing game_state key: '{key}'")

    return errors


def validate_functions():
    """Check if all critical functions exist and are callable"""
    from locations import union, walk_through_greenspace1, library, down_riv, breslin, walk_through_greenspace2, sit_in_beal,eating_contest_watch, mascot_cafe, mascot_panels, sticker_booth,eating_contest,artist_alley,meet_n_greets
    from player_choice_functions import player_combo, paper_topic_choice, eat_riv,get_choice
    from game_state import set_player_data, set_paper_topic,add_to_backpack,purchase_meal,purchase_combo,add_stickers,get_game_state
    from dialogues import go_to_convention,go_back_to_library,write_paper,stay_at_convention,leave_convention,ignore_mascot,talk_to_mascot,take_brochure

    functions = [
        ("union", union),
        ("walk_through_greenspace1", walk_through_greenspace1),
        ("library", library),
        ("down_riv", down_riv),
        ("breslin", breslin),
        ("player_combo", player_combo),
        ("paper_topic_choice", paper_topic_choice),
        ("eat_riv", eat_riv),
        ("eating_contest",eating_contest),
        ("artist_alley",artist_alley),
        ("meet_n_greets", meet_n_greets),
        ("mascot_cafe", mascot_cafe),
        ("mascot_panels", mascot_panels),
        ("sticker_booth", sticker_booth),
        ("set_player_data", set_player_data)  ,
        ("set_paper_topic",set_paper_topic ) ,
        ("add_to_backpack", add_to_backpack )  ,
        ("purchase_meal" ,purchase_meal)   ,
        ("purchase_combo", purchase_combo)   ,
        ("add_stickers",add_stickers  )   ,
        ("get_game_state" ,get_game_state ) ,
        ('walk_through_greenspace2', walk_through_greenspace2),
        ("sit_in_beal", sit_in_beal),
        ("eating_contest_watch", eating_contest_watch),
        ("get_choice",get_choice) ,
        ("go_to_convention", go_to_convention) ,
        ("go_back_to_library", go_back_to_library) ,
        ("write_paper", write_paper) ,
        ("stay_at_convention", stay_at_convention) ,
        ("leave_convention", leave_convention) ,
        ("ignore_mascot",ignore_mascot) ,
        ("talk_to_mascot",talk_to_mascot) ,
        ("take_brochure", take_brochure) ,




    ]

    errors = []
    for func_name, func in functions:
        if not callable(func):
            errors.append(f"❌ {func_name} is not callable")

    return errors


def validate_characters():
    """Check if character definitions work"""
    from characters import Character, PRONOUNS

    errors = []

    # Check PRONOUNS dict
    required_pronouns = ["female", "male", "nonbinary"]
    for pronoun_type in required_pronouns:
        if pronoun_type not in PRONOUNS:
            errors.append(f"❌ Missing pronoun type: '{pronoun_type}'")

    # Try to create a test character
    try:
        test_char = Character(
            name="TestChar",
            likes=["test"],
            location="TestLoc",
            status="bachelor",
            job="tester",
            exes=[]
        )
        if not hasattr(test_char, 'pronouns'):
            errors.append("❌ Character missing 'pronouns' attribute")
    except Exception as e:
        errors.append(f"❌ Error creating test character: {str(e)}")

    return errors


def run_all_validations(verbose=False):
    """
    Run all validation checks
    verbose=True shows detailed output (for debugging)
    verbose=False runs silently
    """

    all_errors = []

    # Suppress output if not verbose
    if not verbose:
        # Create a null sink to suppress print statements
        null_sink = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = null_sink

    try:
        # Run all validations
        import_errors = validate_imports()
        all_errors.extend(import_errors)

        if not import_errors:  # Only continue if imports work
            state_errors = validate_game_state()
            all_errors.extend(state_errors)

            func_errors = validate_functions()
            all_errors.extend(func_errors)

            char_errors = validate_characters()
            all_errors.extend(char_errors)

    finally:
        # Restore stdout
        if not verbose:
            sys.stdout = old_stdout

    return all_errors


def print_validation_results(errors):
    """Print validation results only if there are errors"""
    if not errors:
        print("✓ All systems operational. Starting game...\n")
        return True
    else:
        print("\n" + "=" * 50)
        print("⚠️  VALIDATION ERRORS FOUND:")
        print("=" * 50)
        for error in errors:
            print(error)
        print("=" * 50)
        print("\nPlease fix the errors above before running the game.\n")
        return False