from tkinter import Tk, Label, Button, Frame, Entry, StringVar, Radiobutton, messagebox
import tkinter as tk


class GameGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Mascot Dating Simulator")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        # Store player data
        self.player_data = {}

        self.show_main_menu()

    def clear_window(self):
        """Clear all widgets from the window"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        """Show the main menu screen"""
        self.clear_window()

        Label(self.root, text="Welcome to Mascot Dating Simulator!",
              font=("Calibri", 18, "bold")).pack(pady=40)

        Button(self.root, text="Start Game", command=self.show_greet_screen,
               bg="green", fg="white", font=("Calibri", 12),
               width=15, height=2).pack(pady=10)

        Button(self.root, text="Quit", command=self.root.quit,
               bg="red", fg="white", font=("Calibri", 12),
               width=15, height=2).pack(pady=10)

    def show_greet_screen(self):
        """Show character creation screen (replaces greet() function)"""
        self.clear_window()

        frame = Frame(self.root)
        frame.pack(pady=30)

        # Title
        Label(frame, text="Character Creation",
              font=("Calibri", 16, "bold")).pack(pady=10)

        # Name
        Label(frame, text="What is your name?",
              font=("Calibri", 12)).pack(pady=5)

        self.name_var = StringVar()
        Entry(frame, textvariable=self.name_var,
              font=("Calibri", 12), width=30).pack(pady=5)

        # Gender
        Label(frame, text="What is your gender?",
              font=("Calibri", 12)).pack(pady=10)

        self.gender_var = StringVar(value="nonbinary")

        gender_frame = Frame(frame)
        gender_frame.pack(pady=5)

        Radiobutton(gender_frame, text="Female",
                    variable=self.gender_var, value="female",
                    font=("Calibri", 10)).pack(side=tk.LEFT, padx=10)
        Radiobutton(gender_frame, text="Male",
                    variable=self.gender_var, value="male",
                    font=("Calibri", 10)).pack(side=tk.LEFT, padx=10)
        Radiobutton(gender_frame, text="Non-binary",
                    variable=self.gender_var, value="nonbinary",
                    font=("Calibri", 10)).pack(side=tk.LEFT, padx=10)

        # Age
        Label(frame, text="How old are you?",
              font=("Calibri", 12)).pack(pady=10)

        self.age_var = StringVar()
        Entry(frame, textvariable=self.age_var,
              font=("Calibri", 12), width=10).pack(pady=5)

        # Submit button
        Button(frame, text="Create Character", command=self.process_greet,
               bg="blue", fg="white", font=("Calibri", 12),
               width=15, height=2).pack(pady=20)

    def process_greet(self):
        """Process the character creation data (replaces return from greet())"""
        name = self.name_var.get()
        gender = self.gender_var.get()
        age_text = self.age_var.get()

        # Validate inputs
        if not name:
            messagebox.showerror("Error", "Please enter your name!")
            return

        try:
            age = int(age_text)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age!")
            return

        # Store player data
        self.player_data = {
            'name': name,
            'gender': gender,
            'age': age
        }

        # Show confirmation
        self.clear_window()
        confirmation = (
            f"So your name is {name}, your gender is {gender}, "
            f"and you are {age} years old.\n\n"
            "Press Continue to start your adventure!"
        )

        Label(self.root, text=confirmation,
              font=("Calibri", 12), wraplength=400,
              justify="center").pack(pady=50)

        Button(self.root, text="Continue", command=self.start_game,
               bg="green", fg="white", font=("Calibri", 12),
               width=15, height=2).pack(pady=10)

    def start_game(self):
        """Start the actual game"""
        self.clear_window()

        # Here you would show your first game scene
        Label(self.root, text=f"Welcome, {self.player_data['name']}!",
              font=("Calibri", 16, "bold")).pack(pady=30)

        Label(self.root, text="The game would continue here...",
              font=("Calibri", 12)).pack(pady=20)

        # Example choice
        Button(self.root, text="Go to Union",
               command=lambda: self.show_scene("union"),
               bg="lightblue", font=("Calibri", 11)).pack(pady=5)

        Button(self.root, text="Go to Greenspace",
               command=lambda: self.show_scene("greenspace"),
               bg="lightgreen", font=("Calibri", 11)).pack(pady=5)

    def show_scene(self, scene_name):
        import locations

        """Example method to show different scenes"""
        self.clear_window()

        scenes = {
            union: "You're at the Union. It's busy with students.",
            : "You're in the greenspace. It's peaceful."
        }

        Label(self.root, text=scenes.get(scene_name, "Unknown location"),
              font=("Calibri", 12), wraplength=400).pack(pady=50)

        Button(self.root, text="Back", command=self.start_game,
               bg="gray", fg="white").pack(pady=20)

    def run(self):
        """Start the application"""
        self.root.mainloop()


# Run the game
if __name__ == "__main__":
    game = GameGUI()
    game.run()