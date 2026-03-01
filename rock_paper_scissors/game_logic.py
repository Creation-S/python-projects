"""
MAKING ROCK PAPER SCISSORS
USING MATHEMATHICS
MATRIX
ROCK=0
PAPER=1
SCISSORS=2
THEN
             R P S
COMPUTER=    0 1 2
PLAYER=  R 0 D L W
         P 1 W D L
         S 2 L W D

"""

import random

choices = ["Rock", "Paper", "Scissors"]


def play_round(player):
    if player not in [0, 1, 2]:
        return None, None, "Invalid Choice!"

    computer = random.randint(0, 2)

    result = (player - computer + 3) % 3

    if result == 0:
        result_text = "Draw 🤝"
    elif result == 1:
        result_text = "You Win 🎉"
    else:
        result_text = "You Lose 😢"

    return choices[player], choices[computer], result_text
