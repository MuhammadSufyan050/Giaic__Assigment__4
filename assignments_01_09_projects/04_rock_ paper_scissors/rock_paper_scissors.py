import random

choices = ["rock", "paper", "scissors"]

player_choice = input("Enter rock, paper, or scissors: ").lower()

computer_choice = random.choice(choices)

if player_choice == computer_choice:
    print(f"choice {player_choice}")

elif player_choice == "rock" and computer_choice == "scissors":
    print(f"Players wins {player_choice} beats {computer_choice}")
     
elif player_choice == "paper" and computer_choice == "rock":
    print(f"Players wins {player_choice} beats {computer_choice}")

elif player_choice == "scissors" and computer_choice == "paper":
    print(f"Players wins {player_choice} beats {computer_choice}")

else:
    print(f"Computers win.{computer_choice} beat {player_choice}")