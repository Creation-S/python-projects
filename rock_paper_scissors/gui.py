import tkinter as tk
from game_logic import play_round

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.resizable(False, False)


def handle_click(player):
    player_choice, computer_choice, result = play_round(player)

    if player_choice is None:
        result_label.config(text=result)
        return

    player_label.config(text=f"You chose: {player_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)


title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title.pack(pady=10)

player_label = tk.Label(root, text="You chose: ", font=("Arial", 12))
player_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
computer_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)


frame = tk.Frame(root)
frame.pack(pady=20)

tk.Button(frame, text="Rock", width=10, command=lambda: handle_click(0)).grid(
    row=0, column=0, padx=10
)
tk.Button(frame, text="Paper", width=10, command=lambda: handle_click(1)).grid(
    row=0, column=1, padx=10
)
tk.Button(frame, text="Scissors", width=10, command=lambda: handle_click(2)).grid(
    row=0, column=2, padx=10
)


root.mainloop()
