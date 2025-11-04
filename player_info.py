from main import user_name, user_input_gender_save, user_age, user_gender

player_dict = {

}



class PlayerInfo:
    def __init__(self):
        self.player_name = user_name
        self.player_gender = user_input_gender_save
        self.player_age = user_age
        self.player_pronouns = user_gender




def add_player(user_name,user_input_gender, user_input_gender_save, user_gender, user_age):
    """Creates a PlayerInfo object and stores it in the dictionary."""
    player = PlayerInfo(user_name,user_input_gender, user_input_gender_save, user_gender, user_age)
    player_dict[user_name] = player
#this should handle multiple players having data
def multiple_players():
    """Displays info for all players in the dictionary."""
    for name, player in player_dict.items():
        print(f"\nPlayer: {user_name}")
        print(f"  Gender: {player.user_input_gender_save}")
        print(f"  Age: {player.user_age}")
        print(f"  Pronouns: {', '.join(player.user_gender)}")


backpack=[]