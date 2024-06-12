# import random

# class DiceRollGame:
#     def __init__(self, target_score, max_tries):
#         self.target_score = target_score
#         self.max_tries = max_tries
#         self.current_score = 0
#         self.tries = 0

#     def roll_dice(self, sides):
#         return random.randint(1, sides)

#     def play_game(self):
#         print(f"Welcome to the Dice Roll Game!")
#         print(f"Your goal is to reach a score of {self.target_score} within {self.max_tries} tries.")
        
#         while self.tries < self.max_tries and self.current_score < self.target_score:
#             print("\nChoose a dice to roll:")
#             print("1. 6-sided dice")
#             print("2. 8-sided dice")
#             print("3. 12-sided dice")
#             choice = input("Enter the number of your choice: ")
            
#             if choice == '1':
#                 sides = 6
#             elif choice == '2':
#                 sides = 8
#             elif choice == '3':
#                 sides = 12
#             else:
#                 print("Invalid choice, please select again.")
#                 continue
            
#             roll = self.roll_dice(sides)
#             self.current_score += roll
#             self.tries += 1
            
#             print(f"You rolled a {roll}. Your current score is {self.current_score}. You have {self.max_tries - self.tries} tries left.")
        
#         if self.current_score >= self.target_score:
#             print(f"Congratulations! You've reached the target score of {self.target_score} in {self.tries} tries.")
#         else:
#             print(f"Game Over! You've used all {self.max_tries} tries and didn't reach the target score. Your final score is {self.current_score}.")

# # Game setup
# target_score = 50
# max_tries = 10

# # Start the game
# game = DiceRollGame(target_score, max_tries)
# game.play_game()


# import tkinter as tk
# from tkinter import messagebox
# import random

# class DiceRollGame:
#     def __init__(self, root):
#         self.target_score = 50
#         self.max_tries = 10
#         self.current_score = 0
#         self.tries = 0

#         self.root = root
#         self.root.title("Dice Roll Game")

#         self.label = tk.Label(root, text="Welcome to the Dice Roll Game!")
#         self.label.pack()

#         self.score_label = tk.Label(root, text=f"Current Score: {self.current_score}")
#         self.score_label.pack()

#         self.tries_label = tk.Label(root, text=f"Tries Left: {self.max_tries - self.tries}")
#         self.tries_label.pack()

#         self.dice_label = tk.Label(root, text="Choose a dice to roll:")
#         self.dice_label.pack()

#         self.six_sided_button = tk.Button(root, text="6-sided dice", command=lambda: self.roll_dice(6))
#         self.six_sided_button.pack()

#         self.eight_sided_button = tk.Button(root, text="8-sided dice", command=lambda: self.roll_dice(8))
#         self.eight_sided_button.pack()

#         self.twelve_sided_button = tk.Button(root, text="12-sided dice", command=lambda: self.roll_dice(12))
#         self.twelve_sided_button.pack()

#     def roll_dice(self, sides):
#         if self.tries < self.max_tries and self.current_score < self.target_score:
#             roll = random.randint(1, sides)
#             self.current_score += roll
#             self.tries += 1

#             self.score_label.config(text=f"Current Score: {self.current_score}")
#             self.tries_label.config(text=f"Tries Left: {self.max_tries - self.tries}")

#             if self.current_score >= self.target_score:
#                 messagebox.showinfo("Congratulations!", f"You've reached the target score of {self.target_score} in {self.tries} tries!")
#                 self.reset_game()
#             elif self.tries == self.max_tries:
#                 messagebox.showinfo("Game Over", f"You've used all {self.max_tries} tries and didn't reach the target score. Your final score is {self.current_score}.")
#                 self.reset_game()

#     def reset_game(self):
#         self.current_score = 0
#         self.tries = 0
#         self.score_label.config(text=f"Current Score: {self.current_score}")
#         self.tries_label.config(text=f"Tries Left: {self.max_tries - self.tries}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     game = DiceRollGame(root)
#     root.mainloop()

# import random
# import tkinter as tk
# from tkinter import messagebox

# class DiceRollGame:
#     def __init__(self, root):
#         self.max_tries = 10
#         self.current_score = 0
#         self.tries = 0

#         self.root = root
#         self.root.title("Dice Roll Game")

#         self.label = tk.Label(root, text="Welcome to the Dice Roll Game!")
#         self.label.pack()

#         self.target_score_label = tk.Label(root, text="Enter your target score:")
#         self.target_score_label.pack()

#         self.target_score_entry = tk.Entry(root)
#         self.target_score_entry.pack()

#         self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
#         self.start_button.pack()

#         self.score_label = tk.Label(root, text=f"Current Score: {self.current_score}")
#         self.score_label.pack()
#         self.score_label.pack_forget()

#         self.tries_label = tk.Label(root, text=f"Tries Left: {self.max_tries - self.tries}")
#         self.tries_label.pack()
#         self.tries_label.pack_forget()

#         self.dice_label = tk.Label(root, text="Choose a dice to roll:")
#         self.dice_label.pack()
#         self.dice_label.pack_forget()

#         self.six_sided_button = tk.Button(root, text="6-sided dice", command=lambda: self.roll_dice(6))
#         self.six_sided_button.pack()
#         self.six_sided_button.pack_forget()

#         self.eight_sided_button = tk.Button(root, text="8-sided dice", command=lambda: self.roll_dice(8))
#         self.eight_sided_button.pack()
#         self.eight_sided_button.pack_forget()

#         self.twelve_sided_button = tk.Button(root, text="12-sided dice", command=lambda: self.roll_dice(12))
#         self.twelve_sided_button.pack()
#         self.twelve_sided_button.pack_forget()

#     def start_game(self):
#         try:
#             self.target_score = int(self.target_score_entry.get())
#             if self.target_score <= 0:
#                 raise ValueError("The target score must be a positive integer.")
#         except ValueError as e:
#             messagebox.showerror("Invalid Input", "Please enter a valid positive integer for the target score.")
#             return

#         self.current_score = 0
#         self.tries = 0
#         self.target_score_label.pack_forget()
#         self.target_score_entry.pack_forget()
#         self.start_button.pack_forget()

#         self.score_label.config(text=f"Current Score: {self.current_score}")
#         self.score_label.pack()

#         self.tries_label.config(text=f"Tries Left: {self.max_tries - self.tries}")
#         self.tries_label.pack()

#         self.dice_label.pack()
#         self.six_sided_button.pack()
#         self.eight_sided_button.pack()
#         self.twelve_sided_button.pack()

#     def roll_dice(self, sides):
#         if self.tries < self.max_tries and self.current_score < self.target_score:
#             roll = random.randint(1, sides)
#             self.current_score += roll
#             self.tries += 1

#             self.score_label.config(text=f"Current Score: {self.current_score}")
#             self.tries_label.config(text=f"Tries Left: {self.max_tries - self.tries}")

#             if self.current_score >= self.target_score:
#                 messagebox.showinfo("Congratulations!", f"You've reached the target score of {self.target_score} in {self.tries} tries!")
#                 self.reset_game()
#             elif self.tries == self.max_tries:
#                 messagebox.showinfo("Game Over", f"You've used all {self.max_tries} tries and didn't reach the target score. Your final score is {self.current_score}.")
#                 self.reset_game()

#     def reset_game(self):
#         self.current_score = 0
#         self.tries = 0
#         self.score_label.pack_forget()
#         self.tries_label.pack_forget()
#         self.dice_label.pack_forget()
#         self.six_sided_button.pack_forget()
#         self.eight_sided_button.pack_forget()
#         self.twelve_sided_button.pack_forget()

#         self.target_score_label.pack()
#         self.target_score_entry.pack()
#         self.start_button.pack()

# if __name__ == "__main__":
#     root = tk.Tk()
#     game = DiceRollGame(root)
#     root.mainloop()

import tkinter as tk
from tkinter import messagebox
import random

class DiceRollGame:
    def __init__(self, root):
        self.max_tries = 10
        self.current_score = 0
        self.tries = 0

        self.root = root
        self.root.title("Dice Roll Game")

        self.label = tk.Label(root, text="Welcome to the Dice Roll Game!")
        self.label.pack()

        self.target_score_label = tk.Label(root, text="Enter your target score:")
        self.target_score_label.pack()

        self.target_score_entry = tk.Entry(root)
        self.target_score_entry.pack()

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.score_label = tk.Label(root, text=f"Current Score: {self.current_score}")
        self.score_label.pack()
        self.score_label.pack_forget()

        self.tries_label = tk.Label(root, text=f"Tries Left: {self.max_tries - self.tries}")
        self.tries_label.pack()
        self.tries_label.pack_forget()

        self.dice_label = tk.Label(root, text="Choose a dice to roll:")
        self.dice_label.pack()
        self.dice_label.pack_forget()

        self.six_sided_button = tk.Button(root, text="6-sided dice", command=lambda: self.roll_dice(6))
        self.six_sided_button.pack()
        self.six_sided_button.pack_forget()

        self.eight_sided_button = tk.Button(root, text="8-sided dice", command=lambda: self.roll_dice(8))
        self.eight_sided_button.pack()
        self.eight_sided_button.pack_forget()

        self.twelve_sided_button = tk.Button(root, text="12-sided dice", command=lambda: self.roll_dice(12))
        self.twelve_sided_button.pack()
        self.twelve_sided_button.pack_forget()

        self.canvas = tk.Canvas(root, width=200, height=200)
        self.canvas.pack()
        self.canvas.pack_forget()

    def start_game(self):
        try:
            self.target_score = int(self.target_score_entry.get())
            if self.target_score <= 0:
                raise ValueError("The target score must be a positive integer.")
        except ValueError as e:
            messagebox.showerror("Invalid Input", "Please enter a valid positive integer for the target score.")
            return

        self.current_score = 0
        self.tries = 0
        self.target_score_label.pack_forget()
        self.target_score_entry.pack_forget()
        self.start_button.pack_forget()

        self.score_label.config(text=f"Current Score: {self.current_score}")
        self.score_label.pack()

        self.tries_label.config(text=f"Tries Left: {self.max_tries - self.tries}")
        self.tries_label.pack()

        self.dice_label.pack()
        self.six_sided_button.pack()
        self.eight_sided_button.pack()
        self.twelve_sided_button.pack()

        self.canvas.pack()

    def roll_dice(self, sides):
        if self.tries < self.max_tries and self.current_score < self.target_score:
            self.animate_dice_roll(sides)
            roll = random.randint(1, sides)
            self.current_score += roll
            self.tries += 1

            self.score_label.config(text=f"Current Score: {self.current_score}")
            self.tries_label.config(text=f"Tries Left: {self.max_tries - self.tries}")

            if self.current_score >= self.target_score:
                messagebox.showinfo("Congratulations!", f"You've reached the target score of {self.target_score} in {self.tries} tries!")
                self.reset_game()
            elif self.tries == self.max_tries:
                messagebox.showinfo("Game Over", f"You've used all {self.max_tries} tries and didn't reach the target score. Your final score is {self.current_score}.")
                self.reset_game()

    def animate_dice_roll(self, sides):
        self.canvas.delete("all")
        x, y = 100, 100
        for _ in range(10):
            self.canvas.delete("dice")
            roll = random.randint(1, sides)
            self.canvas.create_text(x, y, text=str(roll), font=("Helvetica", 48), tags="dice")
            self.canvas.update()
            self.canvas.after(100)

    def reset_game(self):
        self.current_score = 0
        self.tries = 0
        self.score_label.pack_forget()
        self.tries_label.pack_forget()
        self.dice_label.pack_forget()
        self.six_sided_button.pack_forget()
        self.eight_sided_button.pack_forget()
        self.twelve_sided_button.pack_forget()
        self.canvas.pack_forget()

        self.target_score_label.pack()
        self.target_score_entry.pack()
        self.start_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    game = DiceRollGame(root)
    root.mainloop()
