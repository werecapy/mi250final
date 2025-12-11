# This holds all shared data - NO imports from main.py
game_state = {
    "player_name": None,
    "player_gender": None,
    "player_pronouns": None,
    "player_age": None,
    "paper_topic": None,
    "backpack": [],
    "combo_purchase": False,
    "combo_type": None,
    "visited_union": False,
    "meet_sparty": False,
    "meet_otto": False,
    "get_stickers": False,
    "stickers": [],
    "meet_brutus": False,
    "meal_purchased" : False,
    "meal_type":None,
    "meal_name":None,
    'meet_tereesa': False,
    "sticker" : None,
    "eating_contest_visit": False,
    "food_contest_save": None,
    "eating_contest_win": False,
    "mascot_cafe_visit": False,
    "sticker_booth_visit": False,
    "artist_alley_visit": False,
"mascot_panel_visit": False,
"meet_n_greets_visit": False,
    "brutus_talk": False,
    "sparty_talk": False,
    "tereesa_talk": False,
"dating_show_pick": None

}
def set_player_data(user_name, user_input_gender_save,user_gender, user_age):
    """How all personal information is saved"""
    game_state["player_name"] = user_name
    game_state["player_gender"] = user_input_gender_save
    game_state["player_pronouns"] = user_gender
    game_state["player_age"] = user_age

def set_paper_topic(topic):
    """How paper topic is saves"""
    game_state["paper_topic"] = topic

def add_to_backpack(item):
    """How things are added to backpack/inventory"""
    game_state["backpack"].append(item)
def purchase_meal(meal_type, meal_name):
    """Mark that player purchased a meal and what kind"""
    game_state["meal_purchased"] = True
    game_state["meal_type"] = meal_type
    game_state["meal_name"] = meal_name
    print(f"Added {meal_name} to your backpack")
    add_to_backpack(meal_name)
def purchase_combo(combo_type):
    """Mark that player purchased a combo and what kind"""
    game_state["combo_purchase"] = True
    game_state["combo_type"] = combo_type
    print(f"Added {combo_type} to backpack.")
    add_to_backpack(combo_type)

def add_stickers(sticker):
    """Mark that player purchased a sticker and what kind"""
    game_state["stickers"].append(sticker)
    add_to_backpack(sticker)

def get_game_state():
    return game_state



