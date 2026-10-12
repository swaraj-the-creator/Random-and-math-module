import random
while True:
    user_actoin = input("Enter a choice(rock, paper, scissors): ")
    possible_actions = [ "rock","paper","scissors"]
    computer_action = random.choices(possible_actions)
    print(f"\nYou chose {user_actoin},computer chose {computer_action}.\n")
    if user_actoin == computer_action:
        print(f"Both the players selected {user_actoin}.It's a tie")
    elif user_actoin == "rock":
        if computer_action == ['scissors']:
            print("Rock smashes scissors. You won")
        else:
            print("Paper covers rock! You lost.")
    elif user_actoin == "paper":
            if computer_action == ['rock']:
                print("Paper covers rock. You won!")
            else:
                print("Scissor cuts paper! You lost.")
    elif user_actoin == "scissors":
            if computer_action == ['paper']:
                print("Scissor cuts paper! You won.")
            else:
                print("Rock smashes scissors. You lost")
    else:
        print("INVALID ANSWER")
        continue
    play_again = input("Play again? (y/n)")
    if play_again != "y":
         break
   