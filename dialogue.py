# ============ dialogue.py (FIXED) ============


class dialogue_node:
    def __init__(self, text, options, on_enter=None):
        """
        text: The prompt to show the player
        options: Dict of {choice_keys: (response_text, next_node)}

        next_node can be:
            - Another DialogueNode (will call .display())
            - A function (will call the function)
            - None (ends dialogue)

        on_enter: Optional function to call when entering this node
        """
        self.text = text
        self.options = options
        self.on_enter = on_enter

    def display(self):
        """Show this dialogue node"""
        if self.on_enter:
            self.on_enter()

        prompt = self.text + "\n"
        for i, (choice_keys, (response, _)) in enumerate(self.options.items(), 1):
            prompt += f"    {i}. {response}\n"
        prompt += "> "

        choice = input(prompt).strip().lower()

        for choice_keys, (response, next_node) in self.options.items():
            if choice in choice_keys or str(len(choice_keys)) in choice:
                print(response + "\n")

                if next_node is None:
                    return
                elif isinstance(next_node, dialogue_node):
                    next_node.display()
                elif callable(next_node):
                    next_node()

                return

        print("Sorry, I don't understand that.\n")
        self.display()