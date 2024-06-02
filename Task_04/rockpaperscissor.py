import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x500")

        self.user_choice = ""
        self.computer_choice = ""
        self.result_var = tk.StringVar()

        self.user_wins = 0
        self.computer_wins = 0
        self.user_wins_var = tk.StringVar(value=f"User Wins: {self.user_wins}")
        self.computer_wins_var = tk.StringVar(value=f"Computer Wins: {self.computer_wins}")

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Rock Paper Scissors", font=("Arial", 24))
        title_label.pack(pady=20)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 18), command=lambda: self.play("Rock"))
        paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 18), command=lambda: self.play("Paper"))
        scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 18), command=lambda: self.play("Scissors"))

        rock_button.grid(row=0, column=0, padx=10)
        paper_button.grid(row=0, column=1, padx=10)
        scissors_button.grid(row=0, column=2, padx=10)

        result_label = tk.Label(self.root, textvariable=self.result_var, font=("Arial", 18))
        result_label.pack(pady=20)

        score_frame = tk.Frame(self.root)
        score_frame.pack(pady=20)

        user_wins_label = tk.Label(score_frame, textvariable=self.user_wins_var, font=("Arial", 16))
        computer_wins_label = tk.Label(score_frame, textvariable=self.computer_wins_var, font=("Arial", 16))

        user_wins_label.grid(row=0, column=0, padx=20)
        computer_wins_label.grid(row=0, column=1, padx=20)

    def play(self, user_choice):
        self.user_choice = user_choice
        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner()
        self.result_var.set(result)
        self.update_score(result)

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            return f"Tie! Both chose {self.user_choice}"
        elif (self.user_choice == "Rock" and self.computer_choice == "Scissors") or \
             (self.user_choice == "Paper" and self.computer_choice == "Rock") or \
             (self.user_choice == "Scissors" and self.computer_choice == "Paper"):
            return f"You win! {self.user_choice} beats {self.computer_choice}"
        else:
            return f"You lose! {self.computer_choice} beats {self.user_choice}"

    def update_score(self, result):
        if "win" in result:
            self.user_wins += 1
            self.user_wins_var.set(f"User Wins: {self.user_wins}")
        elif "lose" in result:
            self.computer_wins += 1
            self.computer_wins_var.set(f"Computer Wins: {self.computer_wins}")

if __name__ == "__main__":
    root = tk.Tk()
    rps_game = RockPaperScissors(root)
    root.mainloop()
