import tkinter as tk
from tkinter import scrolledtext


class GameGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Mascot Dating Simulator")
        self.window.geometry("800x600")

        # Text display area (for game narrative)
        self.text_display = scrolledtext.ScrolledText(
            self.window,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=("Arial", 11)
        )
        self.text_display.pack(pady=10, padx=10)
        self.text_display.config(state=tk.DISABLED)  # Read-only

        # Button frame (for choices)
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(pady=10)

        # Input frame (for text entry like name, age)
        self.input_frame = tk.Frame(self.window)
        self.input_frame.pack(pady=10)

        self.input_label = tk.Label(self.input_frame, text="")
        self.input_entry = tk.Entry(self.input_frame, width=40)
        self.input_button = tk.Button(self.input_frame, text="Submit")

    def display_text(self, text):
        """Add text to the display"""
        self.text_display.config(state=tk.NORMAL)
        self.text_display.insert(tk.END, text + "\n")
        self.text_display.see(tk.END)  # Auto-scroll to bottom
        self.text_display.config(state=tk.DISABLED)

    def clear_buttons(self):
        """Remove all existing buttons"""
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def show_choices(self, choices_dict):
        """
        Show multiple choice buttons
        choices_dict format: {label: callback_function}
        """
        self.clear_buttons()

        for label, callback in choices_dict.items():
            btn = tk.Button(
                self.button_frame,
                text=label,
                command=callback,
                width=50,
                height=2
            )
            btn.pack(pady=5)

    def hide_input(self):
        """Hide the input field"""
        self.input_label.pack_forget()
        self.input_entry.pack_forget()
        self.input_button.pack_forget()

    def show_input(self, prompt, callback):
        """
        Show text input field
        callback will be called with the entered text
        """
        self.hide_input()

        self.input_label.config(text=prompt)
        self.input_label.pack(side=tk.LEFT, padx=5)
        self.input_entry.pack(side=tk.LEFT, padx=5)
        self.input_button.pack(side=tk.LEFT, padx=5)

        # When button clicked, call the callback with the entry value
        def on_submit():
            value = self.input_entry.get()
            self.input_entry.delete(0, tk.END)  # Clear the field
            self.hide_input()
            callback(value)

        self.input_button.config(command=on_submit)

        # Also allow Enter key to submit
        self.input_entry.bind('<Return>', lambda e: on_submit())
        self.input_entry.focus()

    def run(self):
        """Start the GUI event loop"""
        self.window.mainloop()