#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# Import the random module to generate random choices
import random
def rock_paper_scissors_game(user_choice):
    """
    Play a round of Rock, Paper, Scissors.

    Args:
    - user_choice (str): The user's choice.

    Returns:
    - str: The result of the game.
    """
    # Generate a random choice for the computer
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(["rock", "paper", "scissors"])
    # Print the choices
    print(f"You chose {user_choice}, computer chose {computer_choice}.")
    # Determine the winner
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == "rock" and computer_choice == "paper":
        return "computer wins"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "user wins"
    elif user_choice == "paper" and computer_choice == "rock":
        return "user wins"
    elif user_choice == "paper" and computer_choice == "scissors":
        return "computer wins"
    elif user_choice == "scissors" and computer_choice == "rock":
        return "computer wins"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "user wins"
    else:
        raise ValueError(f"Could not determine winner from user choice {user_choice} and computer choice {computer_choice}.")
    
# Ask the user for their choice
user_choice = input("Choose rock, paper, or scissors: ")

# Validate the user's choice
if user_choice not in ["rock", "paper", "scissors"]:
    raise ValueError(f"Invalid choice {user_choice}. Must be one of 'rock', 'paper', or 'scissors'.")

# Call the game function
result = rock_paper_scissors_game(user_choice)
print(result)