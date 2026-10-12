import random
points = 0
comp = 0
while True:
    user_actoin = input("Enter a choice (rock, paper, scissors) : ")
    possible_actions = [ "rock","paper","scissors"]
    computer_action = random.choices(possible_actions)
    print(f"\nYou chose {user_actoin},computer chose {computer_action}.\n")
    if user_actoin == "rock" and computer_action ==['rock'] or user_actoin == "paper" and computer_action ==['paper'] or user_actoin == "scissors" and computer_action ==['scissors']:
        print(f"Both the players selected {user_actoin}.It's a tie")
    elif user_actoin == "rock":
        if computer_action == ['scissors']:
            print("Rock smashes scissors. You won")
            points = points + 1
        else:
            print("Paper covers rock! You lost.")
            comp = comp + 1
    elif user_actoin == "paper":
            if computer_action == ['rock']:
                print("Paper covers rock. You won!")
                points = points + 1
            else:
                print("Scissor cuts paper! You lost.")
                comp = comp + 1
    elif user_actoin == "scissors":
            if computer_action == ['paper']:
                print("Scissor cuts paper! You won.")
                points = points + 1
            else:
                print("Rock smashes scissors. You lost")
                comp = comp + 1
    else:
        print("INVALID ANSWER")
        continue         
    play_again = input("Play again? (y/n):")
    if play_again != "y":
         break
print(f"You won {points} times!")
print(f"Computer won {points} times.")