

pronouns_female = ["she", "her", "hers"]
pronouns_male = ["he", "him", "his"]
pronouns_nonbinary = ["they", "them", "theirs"]

class Character:
    def __init__(self, name,likes,location,status):
        self.name = name
        self.likes= likes
        self.location = location
        self.status = status
        if status == 'bachelorette':
            pronouns = pronouns_female
        elif status == 'bachelor':
            pronouns = pronouns_male
        else:
            pronouns = pronouns_nonbinary

sparty_likes= ["list","here"]
sparty =Character("Sparty",
                  sparty_likes,
                  "East Lansing",
                  "bachelor")

tereesa_likes= ["list","here"]
tereesa =Character("Tereesa",
                   tereesa_likes,
                   "Stanford",
                   "bachelorette")

donald_likes= ["list","here"]
donald = Character(
            "Donald",
            donald_likes,
            "Eugene",
        "bachelor")

brutus_likes= ["list","here"]
brutus = Character("Brutus", brutus_likes,"Columbus", "bachelor")

otto_likes= ["list","here"]
otto = Character("Otto",
                  otto_likes,
                 "Syracuse",
                  "helor")