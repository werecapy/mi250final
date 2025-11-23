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

}
def set_player_data(name, gender, pronouns, age):
    game_state["player_name"] = name
    game_state["player_gender"] = gender
    game_state["player_pronouns"] = pronouns
    game_state["player_age"] = age

def set_paper_topic(topic):
    game_state["paper_topic"] = topic

def add_to_backpack(item):
    game_state["backpack"].append(item)
def purchase_meal(meal_type, meal_name):
    """Mark that player purchased a meal"""
    game_state["meal_purchased"] = True
    game_state["meal_type"] = meal_type
    game_state["meal_name"] = meal_name
    print(f"Added {meal_name} to your backpack")
    add_to_backpack(meal_name)
def purchase_combo(combo_type):
    game_state["combo_purchase"] = True
    game_state["combo_type"] = combo_type
    print(f"Added {combo_type} to backpack.")
    add_to_backpack(combo_type)

def add_stickers(sticker):
    game_state["stickers"].append(sticker)
    add_to_backpack(sticker)

def get_game_state():
    return game_state

