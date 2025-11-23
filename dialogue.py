class dialouge_node:
    def __init__(self,text, options,on_enter=None):
        """


        :param text: prompt to show player
        :param options: Dict of {choice_keys: (response_text, next_node_key_or_function)}
        :param on_enter: optional function that will be called when the user enters the dialogue
        """
        self.text = text
        self.options = options
        self.on_enter = on_enter

    def display(self):
        #shows this dialogue node
        if self.on_enter:
            self.on_enter()
        prompt = self.text + "\n"
        for i, (choice_keys, (response, _)) in enumerate(self.options.items(),1):
            prompt += f"     {i}. {response}\n"
            prompt += ">"
            choice = input(prompt).strip().lower()

        for choice_keys, (response, next_node) in self.options.items():
            if choice in choice_keys or str(len(choice_keys)) in choice:
                print(response + "\n")

                if callable(next_node):
                    next_node()
                elif next_node:
                    next_node.display()
                return

        print("Sorry, I don't understand that.\n")
        self.display()

#========== My dialogue=======
union_dialouge = dialouge_node(
"You continue through the union...",
    {
        ("1","one"): ("Walk to the library",)
    }

)



#========AI example========

# Example usage:
sparty_ending = dialouge_node(
    "Sparty walks away",
    {("1", "one"): ("You feel regretful", None)}
)

sparty_choice_1 = dialouge_node(
    "What do you say?",
    {
        ("1", "one"): ("'I know, I know...'", sparty_ending),
        ("2", "two"): ("'Maybe I can take a break'", sparty_ending),
        ("3", "three"): ("'C'mon Sparty!'", sparty_ending),
    }
)

sparty_start = dialouge_node(
    "What do you say?",
    {
        ("1", "one"): ("'Sorry Sparty, I have a paper...'", sparty_choice_1),
        ("2", "two"): ("'This seems exciting!'", sparty_choice_1),
        ("3", "three"): ("You freeze silently", None),
    }
)

# Then just call:
# sparty_start.display()