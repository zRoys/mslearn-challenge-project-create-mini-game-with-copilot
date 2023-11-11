import random

def play_rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    emojis = {
        "rock": "🪨",
        "paper": "📄",
        "scissors": "✂️"
    }
    player_score, computer_score = 0, 0

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        
        if player_choice not in options:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)
        print(f"You chose: {emojis[player_choice]}")
        print(f"Computer chose: {emojis[computer_choice]}")

        if player_choice == computer_choice:
            print("It's a tie!🙅")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("🎊You win!🎊")
            player_score += 1
        else:
            print("🤖You lose!")
            computer_score += 1

        print(f"Score: Player {player_score}, Computer {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
        
    print(f"Final Score: Player {player_score}, Computer {computer_score}")
    if player_score > computer_score:
        print("🎊🎊🎊You are the winer!🎊🎊🎊")
    elif player_score < computer_score:
        print("🤖You lose!Go home!😪")
    else:
        print("It's a tie!🙅")

play_rock_paper_scissors()
