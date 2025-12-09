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

    def display(self, gui):
        """Show this dialogue node in GUI"""
        if self.on_enter:
            self.on_enter()

        # Display the main dialogue text
        gui.display_text(self.text)

        # Convert options to GUI button choices
        choices = {}
        for i, (choice_keys, (response_text, next_node)) in enumerate(self.options.items(), 1):
            # Create a callback for each choice
            def make_callback(response, next_n):
                def callback():
                    gui.display_text(f"\n{response}\n")

                    if next_n is None:
                        return  # End of dialogue
                    elif isinstance(next_n, dialogue_node):
                        # Call next dialogue node
                        next_n.display(gui)
                    elif callable(next_n):
                        # Call function (make sure it accepts gui)
                        next_n(gui)

                return callback

            # Add button with numbered label
            choices[f"{i}. {response_text}"] = make_callback(response_text, next_node)

        # Show all choices as buttons
        gui.show_choices(choices)