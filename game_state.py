# This holds all shared data - NO imports from main.py
game_state = {
    "player_name": None,
    "player_gender": None,
    "player_pronouns": None,
    "player_age": None,
    "paper_topic": None,
    "backpack": [],
    "combo_purchased": False,
    "combo_type": None,
    "visited_union": False
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

def purchase_combo(combo_type):
    game_state["combo_purchase"] = True
    game_state["combo_type"] = combo_type
    print(f"Added {combo_type} to backpack.")
    add_to_backpack(combo_type)

def get_game_state():
    return game_state

