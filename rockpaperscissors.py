import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_player_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    return choice

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "player"
    else:
        return "computer"

def play_game():
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose {player_choice}, computer chose {computer_choice}.")
        
        winner = determine_winner(player_choice, computer_choice)
        if winner == "tie":
            print("oh...It's a tie!")
        elif winner == "player":
            print("nice...you win...!")
            player_score += 1
        else:
            print("oops, you loose!")
            computer_score += 1
        
        print(f"Score: Player {player_score}, Computer {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")
    print(f"Final Score: Player {player_score}, Computer {computer_score}")

if __name__ == "__main__":
    play_game()
