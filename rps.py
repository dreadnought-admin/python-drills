import random

play = input(("Let's play Rock, Paper, Scissors! Select 'Rock', 'Paper', or 'Scissors:\n"))
computer_moves = ["rock", "paper", "scissors"]
computer_choice_index = random.randint(0, len(computer_moves)-1)
computer_choice = computer_moves[computer_choice_index]

def rock_paper_scissors(player_move, computer_choice):
    player_response = str(player_move).lower()
    print(player_response + " " + computer_choice)
    if player_response  == computer_choice:
        print(f"Player chose: {player_response}\nComputer chose: {computer_choice}\nIt's a tie!")
    elif player_response == "scissors" and computer_choice == "rock":
        print(f"Player chose: {player_response}\nComputer chose: {computer_choice}\nComputer won!")
    elif player_response == "scissors" and computer_choice == "paper":
         print(f"Player Chose: {player_response}\nComputer Chose: {computer_choice}\nPlayer won!")
    elif player_response == "paper" and computer_choice == "rock":
         print(f"Player chose: {player_response}\nComputer chose: {computer_choice}\nPlayer won!")
    elif player_response == "paper" and computer_choice == "scissors":
         print(f"Player chose: {player_response}\nComputer chose: {computer_choice}\nComputer won!")
    elif player_response == "rock" and computer_choice == "scissors":
        print(f"Player chose: {player_response}\nComputer chose: {computer_choice}\nPlayer won!")
    elif player_response == "rock" and computer_choice == "paper":
        print(f"Player chose: {player_response}\nComputer chose: {computer_choice}\nComputer won!")
    else:
        print("That's not a valid choice.")
    
rock_paper_scissors(play, computer_choice)