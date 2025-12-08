# ============ dialogue.py (FIXED) ============


class dialogue_node:
    def __init__(self, text, options, on_enter=None):
        """
        text: The prompt to show the player
        options: Dict of {choice_keys: (response_text, next_node)}



        on_enter: Goes to next dialogue node or to a function, if nothing is
        given, the program will end
        """
        self.text = text
        self.options = options
        self.on_enter = on_enter
    #Displays dialogue node
    def display(self):
        """Show this dialogue node"""
        if self.on_enter:
            self.on_enter()

        prompt = self.text + "\n"
        for i, (choice_keys, (response, _)) in enumerate(self.options.items(), 1):
            prompt += f"    {i}. {response}\n" #Choice enumeration for display
        prompt += "> "

        choice = input(prompt).strip().lower() #actual choice
        #Displays possible options from dialogue node class and figures
        #whether there is a self.on_enter
        for choice_keys, (response, next_node) in self.options.items():
            if choice in choice_keys or str(len(choice_keys)) in choice:
                print(response + "\n")

                if next_node is None:
                    return
                elif isinstance(next_node, dialogue_node):
                    #Calls next dialogue node if it exists
                    next_node.display()
                elif callable(next_node):
                    #Calls if a function is called
                    next_node()

                return

        print("Sorry, I don't understand that.\n") #Calls if the player does something unexpected
        self.display()