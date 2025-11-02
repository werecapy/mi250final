
#-----dict------
PRONOUNS = {
    "female": ["she", "her", "hers"],
    "male": ["he", "him", "his"],
    "nonbinary": ["they", "them", "theirs"]
}




#-----classes
class Character:
    def __init__(self, name,likes,location,status,job,exes):
        self.name = name
        self.job = job
        self.ex = exes
        self.likes= likes
        self.location = location
        self.status = status.lower()
        # Assign pronouns based on status
        if self.status == "bachelorette":
            self.pronouns = PRONOUNS["female"]
        elif self.status == "bachelor":
            self.pronouns = PRONOUNS["male"]
        else:
            self.pronouns = PRONOUNS["nonbinary"]


#------Characters--------
sparty_exes =["list","here","lifting","creatine powder"]
sparty_likes= ["list","here","lifting","creatine powder"]
sparty =Character("Sparty",
                  sparty_likes,
                  "East Lansing",
                  "bachelor",
                  "mascot", sparty_exes)
tereesa_exes = ["list","here"]
tereesa_likes= ["list","here"]
tereesa =Character("Tereesa",
                   tereesa_likes,
                   "Stanford",
                   "bachelorette"
                   ,"mascot"
                   ,tereesa_exes)

brutus_exes = ["list","here", "Animal the  muppet"]
brutus_likes= ["list","here"]
brutus = Character("Brutus",
                   brutus_likes,
                   "Columbus",
                   "bachelor",
                  "mascot"
                   ,brutus_exes)
otto_exes = ["list","here", "Animal the  muppet"]
otto_likes= ["list","here"]
otto = Character("Otto",
                  otto_likes,
                 "Syracuse",
                  "bachelorx",
                  "mascot",
                 otto_exes)
keggy_exes = ["list","here"]
keggy_likes= ["list","here","stickers"]
keggy = Character("Keggy",
                  keggy_likes,
                  "Hanover",
                  "bachelor",
                  "mascot",
                  keggy_exes)

gritty_exes = ["list","here", "Animal the  muppet"]
gritty_likes= ["list","here", ]
gritty = Character("Gritty",
                  gritty_likes,
                  "Hanover",
                  "bachelor",
                  "mascot",
                gritty_exes)

blue_likes= ["list","here"]
blue = Character("blue",
                  blue_likes,
                  "Hanover",
                  "bachelor",
                  "mascot",
                 gritty_exes)


willy_likes= ["list","here"]
willy = Character("Willy the wave",
                  willy_likes,
                  "Hanover",
                  "bachelor",
                  "mascot",
                 gritty_exes)
#--------functions-----------