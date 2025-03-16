import random

def play_rock_paper_scissors():
    """Plays a single round of Rock, Paper, Scissors."""

    # Get user input
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            break
        else:
            print("Invalid input. Please choose rock, paper, or scissors.")

    # Computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine the winner
    print(f"\nYou chose {user_choice}, the computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

# Main game loop
if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        play_rock_paper_scissors()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break
